# InternalImagesHandlerInitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** |  | [optional] 
**presigned_url** | **str** |  | [optional] 
**upload_expires** | **int** |  | [optional] 

## Example

```python
from rixl_api.models.internal_images_handler_init_response import InternalImagesHandlerInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalImagesHandlerInitResponse from a JSON string
internal_images_handler_init_response_instance = InternalImagesHandlerInitResponse.from_json(json)
# print the JSON string representation of the object
print(InternalImagesHandlerInitResponse.to_json())

# convert the object into a dict
internal_images_handler_init_response_dict = internal_images_handler_init_response_instance.to_dict()
# create an instance of InternalImagesHandlerInitResponse from a dict
internal_images_handler_init_response_from_dict = InternalImagesHandlerInitResponse.from_dict(internal_images_handler_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


