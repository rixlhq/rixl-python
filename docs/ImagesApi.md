# rixl_api.ImagesApi

All URIs are relative to *https://api.rixl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_images_image_id**](ImagesApi.md#delete_images_image_id) | **DELETE** /images/{imageId} | Delete image
[**get_images**](ImagesApi.md#get_images) | **GET** /images | List images for a project
[**get_images_image_id**](ImagesApi.md#get_images_image_id) | **GET** /images/{imageId} | Get image
[**post_images_upload_complete**](ImagesApi.md#post_images_upload_complete) | **POST** /images/upload/complete | Upload: Mark as complete
[**post_images_upload_init**](ImagesApi.md#post_images_upload_init) | **POST** /images/upload/init | Upload: Init


# **delete_images_image_id**
> delete_images_image_id(image_id)

Delete image

delete an image by marking it as deleted

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
    api_instance = rixl_api.ImagesApi(api_client)
    image_id = 'image_id_example' # str | Image ID

    try:
        # Delete image
        api_instance.delete_images_image_id(image_id)
    except Exception as e:
        print("Exception when calling ImagesApi->delete_images_image_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID | 

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
**204** | Image deleted successfully |  -  |
**400** | Invalid project ID or image ID |  -  |
**401** | Unauthorized |  -  |
**403** | Access denied |  -  |
**404** | Image not found |  -  |
**500** | Failed to delete image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> PaginationPaginatedResponseImage get_images(limit=limit, offset=offset, sort=sort, order=order)

List images for a project

Retrieve all images for a specific project, with pagination and sorting.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.pagination_paginated_response_image import PaginationPaginatedResponseImage
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
    api_instance = rixl_api.ImagesApi(api_client)
    limit = 25 # int | Maximum number of items to return in a single request. <br> **Default:** `25` (optional) (default to 25)
    offset = 0 # int | Starting point of the result set. <br>To get page 2 with a limit of 25, set `offset` to `25`. <br> **Default:** `0` (optional) (default to 0)
    sort = 'sort_example' # str | Field to sort by (created_at, name, size, updated_at) (optional)
    order = 'order_example' # str | Sort order (asc, desc) (optional)

    try:
        # List images for a project
        api_response = api_instance.get_images(limit=limit, offset=offset, sort=sort, order=order)
        print("The response of ImagesApi->get_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items to return in a single request. &lt;br&gt; **Default:** &#x60;25&#x60; | [optional] [default to 25]
 **offset** | **int**| Starting point of the result set. &lt;br&gt;To get page 2 with a limit of 25, set &#x60;offset&#x60; to &#x60;25&#x60;. &lt;br&gt; **Default:** &#x60;0&#x60; | [optional] [default to 0]
 **sort** | **str**| Field to sort by (created_at, name, size, updated_at) | [optional] 
 **order** | **str**| Sort order (asc, desc) | [optional] 

### Return type

[**PaginationPaginatedResponseImage**](PaginationPaginatedResponseImage.md)

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

# **get_images_image_id**
> Image get_images_image_id(image_id)

Get image

Retrieve an image by its ID for a specific project.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.image import Image
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
    api_instance = rixl_api.ImagesApi(api_client)
    image_id = 'image_id_example' # str | Image ID

    try:
        # Get image
        api_response = api_instance.get_images_image_id(image_id)
        print("The response of ImagesApi->get_images_image_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_images_image_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID | 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid image ID |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Image not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_images_upload_complete**
> Image post_images_upload_complete(request)

Upload: Mark as complete

Complete the upload process and create the image record using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.image import Image
from rixl_api.models.internal_images_handler_complete_request import InternalImagesHandlerCompleteRequest
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
    api_instance = rixl_api.ImagesApi(api_client)
    request = rixl_api.InternalImagesHandlerCompleteRequest() # InternalImagesHandlerCompleteRequest | Upload completion request

    try:
        # Upload: Mark as complete
        api_response = api_instance.post_images_upload_complete(request)
        print("The response of ImagesApi->post_images_upload_complete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->post_images_upload_complete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalImagesHandlerCompleteRequest**](InternalImagesHandlerCompleteRequest.md)| Upload completion request | 

### Return type

[**Image**](Image.md)

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
**500** | Failed to complete upload or create image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_images_upload_init**
> InternalImagesHandlerInitResponse post_images_upload_init(request)

Upload: Init

Initialize a presigned URL upload for an image file using API key authentication

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import rixl_api
from rixl_api.models.internal_images_handler_init_response import InternalImagesHandlerInitResponse
from rixl_api.models.internal_images_handler_upload_init_request import InternalImagesHandlerUploadInitRequest
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
    api_instance = rixl_api.ImagesApi(api_client)
    request = rixl_api.InternalImagesHandlerUploadInitRequest() # InternalImagesHandlerUploadInitRequest | Upload initialization request

    try:
        # Upload: Init
        api_response = api_instance.post_images_upload_init(request)
        print("The response of ImagesApi->post_images_upload_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->post_images_upload_init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InternalImagesHandlerUploadInitRequest**](InternalImagesHandlerUploadInitRequest.md)| Upload initialization request | 

### Return type

[**InternalImagesHandlerInitResponse**](InternalImagesHandlerInitResponse.md)

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

