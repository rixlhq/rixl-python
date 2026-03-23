# Subtitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**video_id** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.subtitle import Subtitle

# TODO update the JSON string below
json = "{}"
# create an instance of Subtitle from a JSON string
subtitle_instance = Subtitle.from_json(json)
# print the JSON string representation of the object
print(Subtitle.to_json())

# convert the object into a dict
subtitle_dict = subtitle_instance.to_dict()
# create an instance of Subtitle from a dict
subtitle_from_dict = Subtitle.from_dict(subtitle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


