# SubtitleDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.subtitle_delete import SubtitleDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleDelete from a JSON string
subtitle_delete_instance = SubtitleDelete.from_json(json)
# print the JSON string representation of the object
print(SubtitleDelete.to_json())

# convert the object into a dict
subtitle_delete_dict = subtitle_delete_instance.to_dict()
# create an instance of SubtitleDelete from a dict
subtitle_delete_from_dict = SubtitleDelete.from_dict(subtitle_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


