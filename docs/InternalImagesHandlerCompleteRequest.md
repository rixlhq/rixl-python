# InternalImagesHandlerCompleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_to_video** | **bool** |  | [optional] 
**image_id** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.internal_images_handler_complete_request import InternalImagesHandlerCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalImagesHandlerCompleteRequest from a JSON string
internal_images_handler_complete_request_instance = InternalImagesHandlerCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(InternalImagesHandlerCompleteRequest.to_json())

# convert the object into a dict
internal_images_handler_complete_request_dict = internal_images_handler_complete_request_instance.to_dict()
# create an instance of InternalImagesHandlerCompleteRequest from a dict
internal_images_handler_complete_request_from_dict = InternalImagesHandlerCompleteRequest.from_dict(internal_images_handler_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


