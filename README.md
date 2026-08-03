# rixl

[![PyPI](https://img.shields.io/pypi/v/rixl.svg)](https://pypi.org/project/rixl/)

The official Python client for the [Rixl](https://rixl.com) API.

Rixl handles the media side of your product — uploading and delivering images and
videos, organising them into feeds and posts, and reporting on how people engage
with them. It also covers the account layer around that: users and organisations,
sign-in, subscriptions and invoices. This SDK gives you all of it from Python, as
a fluent request builder that mirrors the URL structure of the API, with a
dataclass for every request and response.

The client is generated with [Kiota](https://learn.microsoft.com/openapi/kiota/)
and is async throughout — every call is a coroutine you `await`. It needs Python
3.10 or later, and pulls in `microsoft-kiota-bundle` for the HTTP transport,
serializers and request adapter.

## Installation

```bash
pip install rixl
```

## Getting started

Here is the whole thing — build a client, list the images in a project:

```python
import asyncio
import os

from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from rixl_sdk.rixl_client import RixlClient


async def main():
    auth = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header,
        api_key=os.environ["RIXL_API_KEY"],
        parameter_name="X-API-Key",
    )
    adapter = HttpxRequestAdapter(auth, base_url="https://api.rixl.com")
    client = RixlClient(adapter)

    page = await client.media.v1.projects.by_project_id(
        os.environ["RIXL_PROJECT_ID"]
    ).images.get()

    for image in page.images or []:
        print(image.id, image.width, image.height)


asyncio.run(main())
```

Always pass `base_url` to the adapter. The client builds every URL from
`{+baseurl}`, so without it requests go nowhere useful.

You navigate to an endpoint by chaining properties that spell out its path, then
call the HTTP verb: `client.media.v1.projects.by_project_id(pid).images.get()` is
`GET /media/v1/projects/{project_id}/images`. Path segments that take an ID are
`by_*` methods. Responses come back as dataclasses; there is no dict to dig
through.

## Authentication

There are two ways to identify yourself, and they answer different questions.

### API keys — your backend calling as itself

An API key represents your organisation. Use it for work your own systems do:
importing a catalogue, running a nightly report, reconciling invoices. Create one
in the [Rixl dashboard](https://rixl.com), keep it out of source control, and read
it from the environment:

```python
auth = ApiKeyAuthenticationProvider(
    key_location=KeyLocation.Header,
    api_key=os.environ["RIXL_API_KEY"],
    parameter_name="X-API-Key",
)
```

Note the argument order — `key_location` comes first — so pass them by keyword.

The key travels as the `X-API-Key` header. Anyone holding it can do anything your
organisation can, so it belongs on a server, never in anything you ship to users.

### Client credentials — acting on behalf of one of your users

If you are building on top of Rixl and your own users each need their own slice of
it, use client credentials. You exchange a client ID and secret for a short-lived
token scoped to a single end user, so one customer can never read another's media.

First create the credential. The response carries a secret that is returned
**once**:

```python
from rixl_sdk.models.clientauth.v1.create_client_credential_request import (
    CreateClientCredentialRequest,
)

request = CreateClientCredentialRequest()
request.name = "Production backend"

created = await admin.platform.clientauth.v1.credentials.post(request)
print(created.credential.client_id, created.client_secret)
```

Then, in the service that handles your users' requests, exchange it for a token.
`subject` is your own identifier for that person — whatever your database calls
them:

```python
from rixl_sdk.models.clientauth.v1.mint_client_token_request import (
    MintClientTokenRequest,
)

mint = MintClientTokenRequest()
mint.client_id = os.environ["RIXL_CLIENT_ID"]
mint.client_secret = os.environ["RIXL_CLIENT_SECRET"]
mint.subject = user_id
mint.project_id = os.environ["RIXL_PROJECT_ID"]

token = await client.platform.clientauth.v1.token.post(mint)
```

Minting needs no credentials of its own — the ID and secret are in the body — so
an anonymous client will do. You get back `access_token`, `token_type` and
`expires_at`. Use the token by building a second client whose authentication
provider sends it as a bearer token:

```python
from kiota_abstractions.authentication.base_bearer_token_authentication_provider import (
    BaseBearerTokenAuthenticationProvider,
)
from kiota_abstractions.authentication.access_token_provider import AccessTokenProvider
from kiota_abstractions.authentication.allowed_hosts_validator import AllowedHostsValidator


class StaticToken(AccessTokenProvider):
    def __init__(self, token: str):
        self._token = token
        self._validator = AllowedHostsValidator(["api.rixl.com"])

    async def get_authorization_token(self, uri, additional_authentication_context={}):
        return self._token

    def get_allowed_hosts_validator(self):
        return self._validator


user_adapter = HttpxRequestAdapter(
    BaseBearerTokenAuthenticationProvider(StaticToken(token.access_token)),
    base_url="https://api.rixl.com",
)
user_client = RixlClient(user_adapter)
```

Tokens last at most 15 minutes and there is no refresh token: when one expires,
mint another. Nothing here caches or renews for you, so if you are serving many
requests, hold each user's token until `expires_at` and mint again after that. Set
`mint.ttl_minutes` if you want something shorter than the maximum.

To retire a credential, revoke it with
`client.platform.clientauth.v1.credentials.by_credential_id(id).revoke.post()`.
New tokens stop immediately, and any already issued expire within 15 minutes.

### Public endpoints

Some reads need no credentials at all — fetching a public image or video, reading
a public feed, listing supported languages. Build the adapter with the anonymous
provider:

```python
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider,
)

adapter = HttpxRequestAdapter(
    AnonymousAuthenticationProvider(), base_url="https://api.rixl.com"
)
public = RixlClient(adapter)

image = await public.media.v1.images.by_image_id(image_id).get()
posts = await public.posts.v1.feeds.by_feed_id(feed_id).get()
languages = await public.media.v1.languages.get()
```

The public set is: the sign-in flows under `/auth/v1/`, `GET /media/v1/images/*`,
`GET /media/v1/videos/*`, `GET /media/v1/languages`, `GET /posts/v1/feeds/*`, and
the token endpoints under `/platform/`. Everything else needs a key or a token.

## What you can do

The client's top-level properties split the API by path prefix. The API itself is
organised into six areas:

**Authentication** — `client.auth`, plus `client.organizations`. Sign-in flows
including passkeys and one-time codes, user profiles, organisation membership and
roles, access policies, custom domains, transactional email and blog broadcasts.

**Media** — `client.media`. Images, videos, audio tracks, chapters, subtitles,
supported languages, and the image and video conversion pipelines. Upload and
deliver files, attach audio and captions to a video, and convert media into the
formats and sizes you serve.

**Analytics** — `client.analytics`. Dashboards, raw events, post and video and
feed metrics, funnels, heatmaps and live activity.

**Billing** — `client.billing`. Plans, subscriptions, payments, invoices, metered
usage and sales records.

**Content** — `client.posts` and `client.feeds`. Group media into posts and feeds.
A project is the container everything else hangs off, which is why so many builder
chains start with `by_project_id`.

**Platform** — `client.platform`. API keys, platform auth, and the client
credentials above.

There is also `client.internal`, which covers storage-event callbacks the platform
makes to itself. You will not need it.

## Working with resources

Builders follow the same shape, so once you have used one you have used all of
them:

```python
project = client.media.v1.projects.by_project_id(project_id)

page = await project.images.get()
image = await client.media.v1.images.by_image_id(image_id).get()
await project.images.by_image_id(image_id).delete()
```

Note the asymmetry: reading a single image is a public, project-free route
(`/media/v1/images/{image_id}`), while listing and deleting are scoped to a
project. The builder chain always tells you which.

Calls that send data take a request dataclass. Construct it empty and assign
fields — every field is optional and defaults to `None`, so anything you leave
alone is omitted from the JSON:

```python
from rixl_sdk.media.v1.projects.item.images.upload.upload_post_request_body import (
    UploadPostRequestBody,
)

body = UploadPostRequestBody()
body.name = "photo.jpg"
```

Response fields are optional too — the API omits what it has nothing to say about
— so guard with `or []` and `is not None` rather than assuming a value is there.

## Uploading files

Uploads happen in two steps. You ask Rixl for a URL, then send the bytes straight
to storage — they never pass through the API, so large files stay fast:

```python
import httpx

body = UploadPostRequestBody()
body.name = "photo.jpg"

upload = await project.images.upload.post(body)

async with httpx.AsyncClient() as http:
    await http.put(
        upload.upload_url,
        content=image_bytes,
        headers={"Content-Type": "image/jpeg"},
    )
```

Videos work the same way, except you get two URLs back — one for the video, one
for its poster image:

```python
from rixl_sdk.media.v1.projects.item.videos.upload.upload_post_request_body import (
    UploadPostRequestBody as VideoUploadBody,
)

body = VideoUploadBody()
body.name = "clip.mp4"

upload = await project.videos.upload.post(body)

async with httpx.AsyncClient() as http:
    await http.put(upload.video_upload_url, content=video_bytes,
                   headers={"Content-Type": "video/mp4"})
    await http.put(upload.poster_upload_url, content=poster_bytes,
                   headers={"Content-Type": "image/jpeg"})
```

There is no "finish" call to make. Storage tells Rixl when the object lands and
the image or video becomes available on its own. The URLs expire — `expires_at`
tells you when — so upload promptly rather than stashing them.

## Pagination

List calls take a limit and an offset through a per-builder query-parameters
class, wrapped in a `RequestConfiguration`:

```python
from kiota_abstractions.base_request_configuration import RequestConfiguration
from rixl_sdk.media.v1.projects.item.images.images_request_builder import (
    ImagesRequestBuilder,
)

limit, offset = 50, 0

while True:
    params = ImagesRequestBuilder.ImagesRequestBuilderGetQueryParameters(
        pagination_limit=limit,
        pagination_offset=offset,
    )
    page = await project.images.get(
        request_configuration=RequestConfiguration(query_parameters=params)
    )

    images = page.images or []
    for image in images:
        print(image.id)

    if len(images) < limit:
        break
    offset += limit
```

Stop when a page comes back shorter than the limit. The generated list responses
carry `limit`, `offset` and `sort_*` but no total, so counting is the only signal
you have. The SDK does not paginate for you — there is no iterator and no
automatic page fetching. Write the loop.

## Handling errors

Anything that is not a 2xx raises `APIError`, which carries the status code and
the response headers:

```python
from kiota_abstractions.api_error import APIError

try:
    image = await client.media.v1.images.by_image_id(image_id).get()
except APIError as err:
    print(f"rixl returned {err.response_status_code}: {err.message}")
```

What the codes mean:

| Status | What happened | What to do |
| --- | --- | --- |
| 400 | The request was malformed or failed validation | Fix the request; retrying will not help |
| 401 | The key or token is missing, expired or invalid | Check the credential |
| 403 | The credential is valid but not allowed to do this | Check the policies on it |
| 404 | No such resource, or it belongs to another organisation | Check the ID and the project |
| 429 | You are going too fast | Back off and retry |
| 5xx | Something broke on our side | Retry with backoff |

The spec declares no typed error bodies, so `APIError` is what you get for every
failing status — switch on `response_status_code` rather than on the exception
type. Connection failures and timeouts raise `httpx` exceptions instead.

## Timeouts

The SDK does not impose a timeout and does not retry. It uses the `httpx`
`AsyncClient` you give it, so the behaviour stays yours to control:

```python
import httpx

adapter = HttpxRequestAdapter(
    auth,
    http_client=httpx.AsyncClient(timeout=30.0),
    base_url="https://api.rixl.com",
)
```

The same client is where an `httpx` event hook goes if you want tracing headers on
every outbound request.

## Versioning

This package follows [SemVer](https://semver.org/spec/v2.0.0.html). New API
operations arrive in minor releases; renamed or removed ones only in major ones.
If an upgrade breaks you unexpectedly, please open an issue — we would rather hear
about it.

## Support

Bugs and feature requests:
[github.com/rixlhq/rixl-python/issues](https://github.com/rixlhq/rixl-python/issues).
