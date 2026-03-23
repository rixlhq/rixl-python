# GithubComQeeqezApiInternalVideosVideoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitrate** | **int** |  | [optional] 
**chapters** | [**List[Chapter]**](Chapter.md) |  | [optional] 
**codec** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**file** | [**File**](File.md) |  | [optional] 
**framerate** | **str** |  | [optional] 
**hdr** | **bool** |  | [optional] 
**height** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**plan_type** | [**GithubComQeeqezApiDbSqlcPlanType**](GithubComQeeqezApiDbSqlcPlanType.md) |  | [optional] 
**poster** | [**Image**](Image.md) |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from rixl_api.models.github_com_qeeqez_api_internal_videos_video_response import GithubComQeeqezApiInternalVideosVideoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComQeeqezApiInternalVideosVideoResponse from a JSON string
github_com_qeeqez_api_internal_videos_video_response_instance = GithubComQeeqezApiInternalVideosVideoResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComQeeqezApiInternalVideosVideoResponse.to_json())

# convert the object into a dict
github_com_qeeqez_api_internal_videos_video_response_dict = github_com_qeeqez_api_internal_videos_video_response_instance.to_dict()
# create an instance of GithubComQeeqezApiInternalVideosVideoResponse from a dict
github_com_qeeqez_api_internal_videos_video_response_from_dict = GithubComQeeqezApiInternalVideosVideoResponse.from_dict(github_com_qeeqez_api_internal_videos_video_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


