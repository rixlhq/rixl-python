# PaginationPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of items to return in a single request. | [optional] 
**offset** | **int** | Starting point of the result set. | [optional] 
**total** | **int** | The total number of available items in the full list. | [optional] 

## Example

```python
from rixl_api.models.pagination_pagination import PaginationPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationPagination from a JSON string
pagination_pagination_instance = PaginationPagination.from_json(json)
# print the JSON string representation of the object
print(PaginationPagination.to_json())

# convert the object into a dict
pagination_pagination_dict = pagination_pagination_instance.to_dict()
# create an instance of PaginationPagination from a dict
pagination_pagination_from_dict = PaginationPagination.from_dict(pagination_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


