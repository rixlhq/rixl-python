# AudioTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**video_id** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.audio_track import AudioTrack

# TODO update the JSON string below
json = "{}"
# create an instance of AudioTrack from a JSON string
audio_track_instance = AudioTrack.from_json(json)
# print the JSON string representation of the object
print(AudioTrack.to_json())

# convert the object into a dict
audio_track_dict = audio_track_instance.to_dict()
# create an instance of AudioTrack from a dict
audio_track_from_dict = AudioTrack.from_dict(audio_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


