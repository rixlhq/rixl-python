# GithubComQeeqezApiInternalVideosHandlerUploadInitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poster_id** | **str** |  | [optional] 
**poster_presigned_url** | **str** |  | [optional] 
**upload_expires** | **int** |  | [optional] 
**video_id** | **str** |  | [optional] 
**video_presigned_url** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.github_com_qeeqez_api_internal_videos_handler_upload_init_response import GithubComQeeqezApiInternalVideosHandlerUploadInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComQeeqezApiInternalVideosHandlerUploadInitResponse from a JSON string
github_com_qeeqez_api_internal_videos_handler_upload_init_response_instance = GithubComQeeqezApiInternalVideosHandlerUploadInitResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComQeeqezApiInternalVideosHandlerUploadInitResponse.to_json())

# convert the object into a dict
github_com_qeeqez_api_internal_videos_handler_upload_init_response_dict = github_com_qeeqez_api_internal_videos_handler_upload_init_response_instance.to_dict()
# create an instance of GithubComQeeqezApiInternalVideosHandlerUploadInitResponse from a dict
github_com_qeeqez_api_internal_videos_handler_upload_init_response_from_dict = GithubComQeeqezApiInternalVideosHandlerUploadInitResponse.from_dict(github_com_qeeqez_api_internal_videos_handler_upload_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


