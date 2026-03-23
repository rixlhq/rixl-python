# Chapter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_label** | **str** |  | [optional] 
**end_time_sec** | **float** |  | [optional] 
**start_time_sec** | **float** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.chapter import Chapter

# TODO update the JSON string below
json = "{}"
# create an instance of Chapter from a JSON string
chapter_instance = Chapter.from_json(json)
# print the JSON string representation of the object
print(Chapter.to_json())

# convert the object into a dict
chapter_dict = chapter_instance.to_dict()
# create an instance of Chapter from a dict
chapter_from_dict = Chapter.from_dict(chapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


