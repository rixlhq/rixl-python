# AudioTrackDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.audio_track_delete import AudioTrackDelete

# TODO update the JSON string below
json = "{}"
# create an instance of AudioTrackDelete from a JSON string
audio_track_delete_instance = AudioTrackDelete.from_json(json)
# print the JSON string representation of the object
print(AudioTrackDelete.to_json())

# convert the object into a dict
audio_track_delete_dict = audio_track_delete_instance.to_dict()
# create an instance of AudioTrackDelete from a dict
audio_track_delete_from_dict = AudioTrackDelete.from_dict(audio_track_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


