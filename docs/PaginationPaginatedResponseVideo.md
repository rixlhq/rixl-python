# PaginationPaginatedResponseVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Video]**](Video.md) | Data contains the slice of items for the current request. | [optional] 
**pagination** | [**PaginationPagination**](PaginationPagination.md) | Pagination data for the request. | [optional] 

## Example

```python
from rixl_api.models.pagination_paginated_response_video import PaginationPaginatedResponseVideo

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPaginatedResponseVideo from a JSON string
pagination_paginated_response_video_instance = PaginationPaginatedResponseVideo.from_json(json)
# print the JSON string representation of the object
print(PaginationPaginatedResponseVideo.to_json())

# convert the object into a dict
pagination_paginated_response_video_dict = pagination_paginated_response_video_instance.to_dict()
# create an instance of PaginationPaginatedResponseVideo from a dict
pagination_paginated_response_video_from_dict = PaginationPaginatedResponseVideo.from_dict(pagination_paginated_response_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


