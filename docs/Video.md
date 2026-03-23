# Video


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
from rixl_api.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print(Video.to_json())

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_from_dict = Video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


