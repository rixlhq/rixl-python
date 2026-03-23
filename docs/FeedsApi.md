# rixl_api.FeedsApi

All URIs are relative to *https://api.rixl.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feeds_feed_id**](FeedsApi.md#get_feeds_feed_id) | **GET** /feeds/{feedId} | List posts in a feed
[**get_feeds_feed_id_creators_creator_id**](FeedsApi.md#get_feeds_feed_id_creators_creator_id) | **GET** /feeds/{feedId}/creators/{creatorId} | List posts by creator
[**get_feeds_feed_id_post_id**](FeedsApi.md#get_feeds_feed_id_post_id) | **GET** /feeds/{feedId}/{postId} | Get a post


# **get_feeds_feed_id**
> PaginationPaginatedResponsePost get_feeds_feed_id(feed_id, limit=limit, offset=offset)

List posts in a feed

Retrieve posts in a feed, with pagination.

### Example


```python
import rixl_api
from rixl_api.models.pagination_paginated_response_post import PaginationPaginatedResponsePost
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
    api_instance = rixl_api.FeedsApi(api_client)
    feed_id = 'feed_id_example' # str | Feed ID
    limit = 25 # int | Maximum number of items to return in a single request. <br> **Default:** `25` (optional) (default to 25)
    offset = 0 # int | Starting point of the result set. <br>To get page 2 with a limit of 25, set `offset` to `25`. <br> **Default:** `0` (optional) (default to 0)

    try:
        # List posts in a feed
        api_response = api_instance.get_feeds_feed_id(feed_id, limit=limit, offset=offset)
        print("The response of FeedsApi->get_feeds_feed_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedsApi->get_feeds_feed_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Feed ID | 
 **limit** | **int**| Maximum number of items to return in a single request. &lt;br&gt; **Default:** &#x60;25&#x60; | [optional] [default to 25]
 **offset** | **int**| Starting point of the result set. &lt;br&gt;To get page 2 with a limit of 25, set &#x60;offset&#x60; to &#x60;25&#x60;. &lt;br&gt; **Default:** &#x60;0&#x60; | [optional] [default to 0]

### Return type

[**PaginationPaginatedResponsePost**](PaginationPaginatedResponsePost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid feed ID or query parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feeds_feed_id_creators_creator_id**
> PaginationPaginatedResponsePost get_feeds_feed_id_creators_creator_id(feed_id, creator_id, limit=limit, offset=offset)

List posts by creator

Retrieve posts in a feed by a specific creator, with pagination.

### Example


```python
import rixl_api
from rixl_api.models.pagination_paginated_response_post import PaginationPaginatedResponsePost
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
    api_instance = rixl_api.FeedsApi(api_client)
    feed_id = 'feed_id_example' # str | Feed ID
    creator_id = 'creator_id_example' # str | Creator ID
    limit = 25 # int | Maximum number of items to return in a single request. <br> **Default:** `25` (optional) (default to 25)
    offset = 0 # int | Starting point of the result set. <br>To get page 2 with a limit of 25, set `offset` to `25`. <br> **Default:** `0` (optional) (default to 0)

    try:
        # List posts by creator
        api_response = api_instance.get_feeds_feed_id_creators_creator_id(feed_id, creator_id, limit=limit, offset=offset)
        print("The response of FeedsApi->get_feeds_feed_id_creators_creator_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedsApi->get_feeds_feed_id_creators_creator_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Feed ID | 
 **creator_id** | **str**| Creator ID | 
 **limit** | **int**| Maximum number of items to return in a single request. &lt;br&gt; **Default:** &#x60;25&#x60; | [optional] [default to 25]
 **offset** | **int**| Starting point of the result set. &lt;br&gt;To get page 2 with a limit of 25, set &#x60;offset&#x60; to &#x60;25&#x60;. &lt;br&gt; **Default:** &#x60;0&#x60; | [optional] [default to 0]

### Return type

[**PaginationPaginatedResponsePost**](PaginationPaginatedResponsePost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid feed ID, creator ID, or query parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feeds_feed_id_post_id**
> Post get_feeds_feed_id_post_id(feed_id, post_id)

Get a post

Retrieve a post from feed by its ID

### Example


```python
import rixl_api
from rixl_api.models.post import Post
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
    api_instance = rixl_api.FeedsApi(api_client)
    feed_id = 'feed_id_example' # str | Feed ID
    post_id = 'post_id_example' # str | Post ID

    try:
        # Get a post
        api_response = api_instance.get_feeds_feed_id_post_id(feed_id, post_id)
        print("The response of FeedsApi->get_feeds_feed_id_post_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedsApi->get_feeds_feed_id_post_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Feed ID | 
 **post_id** | **str**| Post ID | 

### Return type

[**Post**](Post.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

