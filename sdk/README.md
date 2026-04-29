# RIXL Python SDK

The official Python client for the [RIXL](https://rixl.com) API.

[![PyPI](https://img.shields.io/pypi/v/rixl-python.svg)](https://pypi.org/project/rixl-python/)
[![Python](https://img.shields.io/pypi/pyversions/rixl-python.svg)](https://pypi.org/project/rixl-python/)

[Installation](#installation) • [Quick start](#quick-start) • [Authentication](#authentication) • [Resources](#resources) • [Pagination](#pagination) • [Errors](#errors)

## Features

- Typed fluent API generated from the RIXL OpenAPI spec
- Async-first — every call is awaitable
- Pre-mapped error responses for 400, 401, 403, 404, and 500
- Pluggable `RequestAdapter` and authentication providers
- Support for JSON, form, multipart, and plain-text payloads

## Requirements

- Python 3.10+
- A RIXL API key

## Installation

```bash
pip install rixl-python
```

`microsoft-kiota-bundle` is pulled in as a dependency and provides the HTTP transport, serializers, and `RequestAdapter` implementation.

## Quick start

```python
import asyncio

from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider, KeyLocation,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from rixl_client import RixlClient


async def main() -> None:
    auth = ApiKeyAuthenticationProvider(
        api_key="YOUR_RIXL_API_KEY",
        parameter_name="X-API-Key",
        key_location=KeyLocation.Header,
    )
    adapter = HttpxRequestAdapter(auth)
    client = RixlClient(adapter)

    image = await client.images.by_image_id("PS5IMKoFLm").get()
    print(image.id, image.width, image.height)


asyncio.run(main())
```
