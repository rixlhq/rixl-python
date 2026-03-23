# rixl_api.VideosApi

All URIs are relative to *https://api.rixl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_videos_video_id_audio_tracks**](VideosApi.md#delete_videos_video_id_audio_tracks) | **DELETE** /videos/{videoId}/audio-tracks | Delete all audio tracks
[**delete_videos_video_id_audio_tracks_lang_code**](VideosApi.md#delete_videos_video_id_audio_tracks_lang_code) | **DELETE** /videos/{videoId}/audio-tracks/{lang_code} | Delete audio track by language
[**delete_videos_video_id_audio_tracks_track_id**](VideosApi.md#delete_videos_video_id_audio_tracks_track_id) | **DELETE** /videos/{videoId}/audio-tracks/{trackId} | Delete audio track
[**delete_videos_video_id_chapters**](VideosApi.md#delete_videos_video_id_chapters) | **DELETE** /videos/{videoId}/chapters | Delete video chapters
[**delete_videos_video_id_delete**](VideosApi.md#delete_videos_video_id_delete) | **DELETE** /videos/{videoId}/delete | Delete video
[**delete_videos_video_id_subtitles**](VideosApi.md#delete_videos_video_id_subtitles) | **DELETE** /videos/{videoId}/subtitles | Delete all subtitles
[**delete_videos_video_id_subtitles_lang_code**](VideosApi.md#delete_videos_video_id_subtitles_lang_code) | **DELETE** /videos/{videoId}/subtitles/{lang_code} | Delete subtitle by language
[**delete_videos_video_id_subtitles_subtitle_id**](VideosApi.md#delete_videos_video_id_subtitles_subtitle_id) | **DELETE** /videos/{videoId}/subtitles/{subtitleId} | Delete subtitle
[**get_videos**](VideosApi.md#get_videos) | **GET** /videos | List videos for a project
[**get_videos_languages**](VideosApi.md#get_videos_languages) | **GET** /videos/languages | List available subtitle languages
[**get_videos_video_id**](VideosApi.md#get_videos_video_id) | **GET** /videos/{videoId} | Get a video
[**post_videos_upload_complete**](VideosApi.md#post_videos_upload_complete) | **POST** /videos/upload/complete | Upload: Mark as complete
[**post_videos_upload_init**](VideosApi.md#post_videos_upload_init) | **POST** /videos/upload/init | Upload: Init
[**post_videos_video_id_audio_tracks**](VideosApi.md#post_videos_video_id_audio_tracks) | **POST** /videos/{videoId}/audio-tracks | Bulk upsert video audio tracks
[**post_videos_video_id_subtitles**](VideosApi.md#post_videos_video_id_subtitles) | **POST** /videos/{videoId}/subtitles | Bulk upsert video subtitles
[**put_videos_video_id_audio_tracks_lang_code**](VideosApi.md#put_videos_video_id_audio_tracks_lang_code) | **PUT** /videos/{videoId}/audio-tracks/{lang_code} | Upsert video audio track
[**put_videos_video_id_chapters**](VideosApi.md#put_videos_video_id_chapters) | **PUT** /videos/{videoId}/chapters | Update video chapters
[**put_videos_video_id_subtitles_lang_code**](VideosApi.md#put_videos_video_id_subtitles_lang_code) | **PUT** /videos/{videoId}/subtitles/{lang_code} | Upsert video subtitle
[**put_videos_video_id_thumbnail**](VideosApi.md#put_videos_video_id_thumbnail) | **PUT** /videos/{videoId}/thumbnail | Update video thumbnail


# **delete_videos_video_id_audio_tracks**
> AudioTrackDelete delete_videos_video_id_audio_tracks(video_id)

Delete all audio tracks

Remove all additional audio tracks from a video using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.audio_track_delete import AudioTrackDelete
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID

    try:
        # Delete all audio tracks
        api_response = api_instance.delete_videos_video_id_audio_tracks(video_id)
        print("The response of VideosApi->delete_videos_video_id_audio_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_audio_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 

### Return type

[**AudioTrackDelete**](AudioTrackDelete.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_audio_tracks_lang_code**
> AudioTrackDelete delete_videos_video_id_audio_tracks_lang_code(video_id, lang_code)

Delete audio track by language

Remove an audio track for a specific language using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.audio_track_delete import AudioTrackDelete
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    lang_code = 'lang_code_example' # str | Language Code (BCP 47)

    try:
        # Delete audio track by language
        api_response = api_instance.delete_videos_video_id_audio_tracks_lang_code(video_id, lang_code)
        print("The response of VideosApi->delete_videos_video_id_audio_tracks_lang_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_audio_tracks_lang_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **lang_code** | **str**| Language Code (BCP 47) | 

### Return type

[**AudioTrackDelete**](AudioTrackDelete.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_audio_tracks_track_id**
> AudioTrackDelete delete_videos_video_id_audio_tracks_track_id(video_id, track_id)

Delete audio track

Remove an additional audio track from a video using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.audio_track_delete import AudioTrackDelete
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    track_id = 'track_id_example' # str | Audio Track ID

    try:
        # Delete audio track
        api_response = api_instance.delete_videos_video_id_audio_tracks_track_id(video_id, track_id)
        print("The response of VideosApi->delete_videos_video_id_audio_tracks_track_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_audio_tracks_track_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **track_id** | **str**| Audio Track ID | 

### Return type

[**AudioTrackDelete**](AudioTrackDelete.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_chapters**
> UpdateChaptersResponse delete_videos_video_id_chapters(video_id)

Delete video chapters

Remove all chapters from a video using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.update_chapters_response import UpdateChaptersResponse
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID

    try:
        # Delete video chapters
        api_response = api_instance.delete_videos_video_id_chapters(video_id)
        print("The response of VideosApi->delete_videos_video_id_chapters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_chapters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 

### Return type

[**UpdateChaptersResponse**](UpdateChaptersResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**403** | Access denied |  -  |
**404** | Video not found |  -  |
**500** | Failed to delete chapters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_delete**
> delete_videos_video_id_delete(video_id)

Delete video

Delete a video by its ID within a project

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID

    try:
        # Delete video
        api_instance.delete_videos_video_id_delete(video_id)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Video deleted successfully |  -  |
**400** | Invalid project ID or video ID |  -  |
**401** | Unauthorized |  -  |
**403** | Access denied |  -  |
**404** | Video not found |  -  |
**500** | Failed to delete video |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_subtitles**
> SubtitleDelete delete_videos_video_id_subtitles(video_id)

Delete all subtitles

Remove all subtitles from a video using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.subtitle_delete import SubtitleDelete
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID

    try:
        # Delete all subtitles
        api_response = api_instance.delete_videos_video_id_subtitles(video_id)
        print("The response of VideosApi->delete_videos_video_id_subtitles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_subtitles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 

### Return type

[**SubtitleDelete**](SubtitleDelete.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_subtitles_lang_code**
> SubtitleDelete delete_videos_video_id_subtitles_lang_code(video_id, lang_code)

Delete subtitle by language

Remove a subtitle for a specific language using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.subtitle_delete import SubtitleDelete
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    lang_code = 'lang_code_example' # str | Language Code (BCP 47)

    try:
        # Delete subtitle by language
        api_response = api_instance.delete_videos_video_id_subtitles_lang_code(video_id, lang_code)
        print("The response of VideosApi->delete_videos_video_id_subtitles_lang_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_subtitles_lang_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **lang_code** | **str**| Language Code (BCP 47) | 

### Return type

[**SubtitleDelete**](SubtitleDelete.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_videos_video_id_subtitles_subtitle_id**
> SubtitleDelete delete_videos_video_id_subtitles_subtitle_id(video_id, subtitle_id)

Delete subtitle

Remove a subtitle from a video using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.subtitle_delete import SubtitleDelete
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    subtitle_id = 'subtitle_id_example' # str | Subtitle ID

    try:
        # Delete subtitle
        api_response = api_instance.delete_videos_video_id_subtitles_subtitle_id(video_id, subtitle_id)
        print("The response of VideosApi->delete_videos_video_id_subtitles_subtitle_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->delete_videos_video_id_subtitles_subtitle_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **subtitle_id** | **str**| Subtitle ID | 

### Return type

[**SubtitleDelete**](SubtitleDelete.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos**
> PaginationPaginatedResponseVideo get_videos(limit=limit, offset=offset, sort=sort, order=order)

List videos for a project

Retrieve all videos for a specific project, with pagination and sorting.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.pagination_paginated_response_video import PaginationPaginatedResponseVideo
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    limit = 25 # int | Maximum number of items to return in a single request. <br> **Default:** `25` (optional) (default to 25)
    offset = 0 # int | Starting point of the result set. <br>To get page 2 with a limit of 25, set `offset` to `25`. <br> **Default:** `0` (optional) (default to 0)
    sort = 'sort_example' # str | Field to sort by (created_at, name, size, updated_at, duration) (optional)
    order = 'order_example' # str | Sort order (asc, desc) (optional)

    try:
        # List videos for a project
        api_response = api_instance.get_videos(limit=limit, offset=offset, sort=sort, order=order)
        print("The response of VideosApi->get_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items to return in a single request. &lt;br&gt; **Default:** &#x60;25&#x60; | [optional] [default to 25]
 **offset** | **int**| Starting point of the result set. &lt;br&gt;To get page 2 with a limit of 25, set &#x60;offset&#x60; to &#x60;25&#x60;. &lt;br&gt; **Default:** &#x60;0&#x60; | [optional] [default to 0]
 **sort** | **str**| Field to sort by (created_at, name, size, updated_at, duration) | [optional] 
 **order** | **str**| Sort order (asc, desc) | [optional] 

### Return type

[**PaginationPaginatedResponseVideo**](PaginationPaginatedResponseVideo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid query parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_languages**
> List[InternalVideosHandlerSubtitlesLanguageResponse] get_videos_languages()

List available subtitle languages

Get list of supported languages for subtitles

### Example


```python
import rixl_api
from rixl_api.models.internal_videos_handler_subtitles_language_response import InternalVideosHandlerSubtitlesLanguageResponse
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)


# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)

    try:
        # List available subtitle languages
        api_response = api_instance.get_videos_languages()
        print("The response of VideosApi->get_videos_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_videos_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[InternalVideosHandlerSubtitlesLanguageResponse]**](InternalVideosHandlerSubtitlesLanguageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_video_id**
> Video get_videos_video_id(video_id)

Get a video

Retrieve a video by its ID for a specific project.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.video import Video
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID

    try:
        # Get a video
        api_response = api_instance.get_videos_video_id(video_id)
        print("The response of VideosApi->get_videos_video_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_videos_video_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 

### Return type

[**Video**](Video.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid video ID |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Video not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_upload_complete**
> Video post_videos_upload_complete(request)

Upload: Mark as complete

Mark a video upload as complete after successful upload to storage using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.github_com_qeeqez_api_internal_videos_handler_upload_complete_request import GithubComQeeqezApiInternalVideosHandlerUploadCompleteRequest
from rixl_api.models.video import Video
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    request = rixl_api.GithubComQeeqezApiInternalVideosHandlerUploadCompleteRequest() # GithubComQeeqezApiInternalVideosHandlerUploadCompleteRequest | Video upload completion request

    try:
        # Upload: Mark as complete
        api_response = api_instance.post_videos_upload_complete(request)
        print("The response of VideosApi->post_videos_upload_complete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->post_videos_upload_complete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GithubComQeeqezApiInternalVideosHandlerUploadCompleteRequest**](GithubComQeeqezApiInternalVideosHandlerUploadCompleteRequest.md)| Video upload completion request | 

### Return type

[**Video**](Video.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**403** | Access denied |  -  |
**404** | File not found |  -  |
**500** | Failed to complete upload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_upload_init**
> GithubComQeeqezApiInternalVideosHandlerUploadInitResponse post_videos_upload_init(request)

Upload: Init

Initialize a video upload and get presigned URLs for video and poster using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.github_com_qeeqez_api_internal_videos_handler_upload_init_response import GithubComQeeqezApiInternalVideosHandlerUploadInitResponse
from rixl_api.models.video_upload_init_request import VideoUploadInitRequest
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    request = rixl_api.VideoUploadInitRequest() # VideoUploadInitRequest | Video upload initialization request

    try:
        # Upload: Init
        api_response = api_instance.post_videos_upload_init(request)
        print("The response of VideosApi->post_videos_upload_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->post_videos_upload_init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**VideoUploadInitRequest**](VideoUploadInitRequest.md)| Video upload initialization request | 

### Return type

[**GithubComQeeqezApiInternalVideosHandlerUploadInitResponse**](GithubComQeeqezApiInternalVideosHandlerUploadInitResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**403** | Access denied |  -  |
**500** | Failed to initialize upload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_video_id_audio_tracks**
> List[AudioTrack] post_videos_video_id_audio_tracks(video_id, files, language_codes, labels)

Bulk upsert video audio tracks

Replace all audio tracks with the provided ones using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.audio_track import AudioTrack
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    files = None # List[bytearray] | Audio files (.mp3, .opus, .flac, .wav, .ac3, .m4a, .aac)
    language_codes = 'language_codes_example' # str | Comma-separated language codes
    labels = 'labels_example' # str | Comma-separated labels

    try:
        # Bulk upsert video audio tracks
        api_response = api_instance.post_videos_video_id_audio_tracks(video_id, files, language_codes, labels)
        print("The response of VideosApi->post_videos_video_id_audio_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->post_videos_video_id_audio_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **files** | **List[bytearray]**| Audio files (.mp3, .opus, .flac, .wav, .ac3, .m4a, .aac) | 
 **language_codes** | **str**| Comma-separated language codes | 
 **labels** | **str**| Comma-separated labels | 

### Return type

[**List[AudioTrack]**](AudioTrack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_videos_video_id_subtitles**
> List[Subtitle] post_videos_video_id_subtitles(video_id, files, language_codes, labels)

Bulk upsert video subtitles

Replace all subtitles with the provided ones using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.subtitle import Subtitle
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    files = None # List[bytearray] | Subtitle files (.srt or .vtt)
    language_codes = 'language_codes_example' # str | Comma-separated language codes
    labels = 'labels_example' # str | Comma-separated labels

    try:
        # Bulk upsert video subtitles
        api_response = api_instance.post_videos_video_id_subtitles(video_id, files, language_codes, labels)
        print("The response of VideosApi->post_videos_video_id_subtitles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->post_videos_video_id_subtitles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **files** | **List[bytearray]**| Subtitle files (.srt or .vtt) | 
 **language_codes** | **str**| Comma-separated language codes | 
 **labels** | **str**| Comma-separated labels | 

### Return type

[**List[Subtitle]**](Subtitle.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_videos_video_id_audio_tracks_lang_code**
> AudioTrack put_videos_video_id_audio_tracks_lang_code(video_id, lang_code, file, label=label)

Upsert video audio track

Add or replace an audio track for a specific language using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.audio_track import AudioTrack
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    lang_code = 'lang_code_example' # str | Language Code (BCP 47)
    file = None # bytearray | Audio file (.mp3, .opus, .flac, .wav, .ac3, .m4a, .aac)
    label = 'label_example' # str | Label (e.g. English) (optional)

    try:
        # Upsert video audio track
        api_response = api_instance.put_videos_video_id_audio_tracks_lang_code(video_id, lang_code, file, label=label)
        print("The response of VideosApi->put_videos_video_id_audio_tracks_lang_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->put_videos_video_id_audio_tracks_lang_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **lang_code** | **str**| Language Code (BCP 47) | 
 **file** | **bytearray**| Audio file (.mp3, .opus, .flac, .wav, .ac3, .m4a, .aac) | 
 **label** | **str**| Label (e.g. English) | [optional] 

### Return type

[**AudioTrack**](AudioTrack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_videos_video_id_chapters**
> UpdateChaptersResponse put_videos_video_id_chapters(video_id, request)

Update video chapters

Replace all chapters for a video (atomic PUT operation) using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.update_chapters_request import UpdateChaptersRequest
from rixl_api.models.update_chapters_response import UpdateChaptersResponse
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    request = rixl_api.UpdateChaptersRequest() # UpdateChaptersRequest | Chapters array

    try:
        # Update video chapters
        api_response = api_instance.put_videos_video_id_chapters(video_id, request)
        print("The response of VideosApi->put_videos_video_id_chapters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->put_videos_video_id_chapters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **request** | [**UpdateChaptersRequest**](UpdateChaptersRequest.md)| Chapters array | 

### Return type

[**UpdateChaptersResponse**](UpdateChaptersResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body or video duration not available |  -  |
**401** | Unauthorized - Invalid API key |  -  |
**403** | Access denied |  -  |
**404** | Video not found |  -  |
**500** | Failed to update chapters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_videos_video_id_subtitles_lang_code**
> Subtitle put_videos_video_id_subtitles_lang_code(video_id, lang_code, file, label=label)

Upsert video subtitle

Add or replace a subtitle for a specific language using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.subtitle import Subtitle
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    lang_code = 'lang_code_example' # str | Language Code (BCP 47)
    file = None # bytearray | Subtitle file (.srt or .vtt)
    label = 'label_example' # str | Label (e.g. English) (optional)

    try:
        # Upsert video subtitle
        api_response = api_instance.put_videos_video_id_subtitles_lang_code(video_id, lang_code, file, label=label)
        print("The response of VideosApi->put_videos_video_id_subtitles_lang_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->put_videos_video_id_subtitles_lang_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **lang_code** | **str**| Language Code (BCP 47) | 
 **file** | **bytearray**| Subtitle file (.srt or .vtt) | 
 **label** | **str**| Label (e.g. English) | [optional] 

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_videos_video_id_thumbnail**
> Video put_videos_video_id_thumbnail(video_id, thumbnail)

Update video thumbnail

Update the thumbnail image for an existing video

### Example


```python
import rixl_api
from rixl_api.models.video import Video
from rixl_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rixl.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rixl_api.Configuration(
    host = "https://api.rixl.com"
)


# Enter a context with an instance of the API client
with rixl_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rixl_api.VideosApi(api_client)
    video_id = 'video_id_example' # str | Video ID
    thumbnail = None # bytearray | Thumbnail image file (max 5MB, image/*)

    try:
        # Update video thumbnail
        api_response = api_instance.put_videos_video_id_thumbnail(video_id, thumbnail)
        print("The response of VideosApi->put_videos_video_id_thumbnail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->put_videos_video_id_thumbnail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Video ID | 
 **thumbnail** | **bytearray**| Thumbnail image file (max 5MB, image/*) | 

### Return type

[**Video**](Video.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video with updated thumbnail |  -  |
**400** | Invalid file or request |  -  |
**401** | Unauthorized |  -  |
**403** | Access denied |  -  |
**404** | Video not found |  -  |
**500** | Upload or update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

