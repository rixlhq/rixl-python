# InternalImagesHandlerUploadInitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.internal_images_handler_upload_init_request import InternalImagesHandlerUploadInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalImagesHandlerUploadInitRequest from a JSON string
internal_images_handler_upload_init_request_instance = InternalImagesHandlerUploadInitRequest.from_json(json)
# print the JSON string representation of the object
print(InternalImagesHandlerUploadInitRequest.to_json())

# convert the object into a dict
internal_images_handler_upload_init_request_dict = internal_images_handler_upload_init_request_instance.to_dict()
# create an instance of InternalImagesHandlerUploadInitRequest from a dict
internal_images_handler_upload_init_request_from_dict = InternalImagesHandlerUploadInitRequest.from_dict(internal_images_handler_upload_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


