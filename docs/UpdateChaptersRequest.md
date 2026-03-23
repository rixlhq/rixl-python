# UpdateChaptersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chapters** | [**List[GithubComQeeqezApiInternalVideosTypesChapterInput]**](GithubComQeeqezApiInternalVideosTypesChapterInput.md) |  | [optional] 

## Example

```python
from rixl_api.models.update_chapters_request import UpdateChaptersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChaptersRequest from a JSON string
update_chapters_request_instance = UpdateChaptersRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateChaptersRequest.to_json())

# convert the object into a dict
update_chapters_request_dict = update_chapters_request_instance.to_dict()
# create an instance of UpdateChaptersRequest from a dict
update_chapters_request_from_dict = UpdateChaptersRequest.from_dict(update_chapters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


