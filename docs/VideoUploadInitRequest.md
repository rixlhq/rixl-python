# VideoUploadInitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**image_format** | **str** |  | [optional] 
**video_quality** | [**GithubComQeeqezApiDbSqlcVideoQuality**](GithubComQeeqezApiDbSqlcVideoQuality.md) |  | [optional] 

## Example

```python
from rixl_api.models.video_upload_init_request import VideoUploadInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VideoUploadInitRequest from a JSON string
video_upload_init_request_instance = VideoUploadInitRequest.from_json(json)
# print the JSON string representation of the object
print(VideoUploadInitRequest.to_json())

# convert the object into a dict
video_upload_init_request_dict = video_upload_init_request_instance.to_dict()
# create an instance of VideoUploadInitRequest from a dict
video_upload_init_request_from_dict = VideoUploadInitRequest.from_dict(video_upload_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


