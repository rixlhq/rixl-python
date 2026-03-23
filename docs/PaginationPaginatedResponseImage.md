# PaginationPaginatedResponseImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Image]**](Image.md) | Data contains the slice of items for the current request. | [optional] 
**pagination** | [**PaginationPagination**](PaginationPagination.md) | Pagination data for the request. | [optional] 

## Example

```python
from rixl_api.models.pagination_paginated_response_image import PaginationPaginatedResponseImage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPaginatedResponseImage from a JSON string
pagination_paginated_response_image_instance = PaginationPaginatedResponseImage.from_json(json)
# print the JSON string representation of the object
print(PaginationPaginatedResponseImage.to_json())

# convert the object into a dict
pagination_paginated_response_image_dict = pagination_paginated_response_image_instance.to_dict()
# create an instance of PaginationPaginatedResponseImage from a dict
pagination_paginated_response_image_from_dict = PaginationPaginatedResponseImage.from_dict(pagination_paginated_response_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


