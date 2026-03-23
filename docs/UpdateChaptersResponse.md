# UpdateChaptersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chapters** | [**List[Chapter]**](Chapter.md) |  | [optional] 
**video_id** | **str** |  | [optional] 

## Example

```python
from rixl_api.models.update_chapters_response import UpdateChaptersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChaptersResponse from a JSON string
update_chapters_response_instance = UpdateChaptersResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateChaptersResponse.to_json())

# convert the object into a dict
update_chapters_response_dict = update_chapters_response_instance.to_dict()
# create an instance of UpdateChaptersResponse from a dict
update_chapters_response_from_dict = UpdateChaptersResponse.from_dict(update_chapters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


