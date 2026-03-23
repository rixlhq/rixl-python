# PaginationPaginatedResponsePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Post]**](Post.md) | Data contains the slice of items for the current request. | [optional] 
**pagination** | [**PaginationPagination**](PaginationPagination.md) | Pagination data for the request. | [optional] 

## Example

```python
from rixl_api.models.pagination_paginated_response_post import PaginationPaginatedResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPaginatedResponsePost from a JSON string
pagination_paginated_response_post_instance = PaginationPaginatedResponsePost.from_json(json)
# print the JSON string representation of the object
print(PaginationPaginatedResponsePost.to_json())

# convert the object into a dict
pagination_paginated_response_post_dict = pagination_paginated_response_post_instance.to_dict()
# create an instance of PaginationPaginatedResponsePost from a dict
pagination_paginated_response_post_from_dict = PaginationPaginatedResponsePost.from_dict(pagination_paginated_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


