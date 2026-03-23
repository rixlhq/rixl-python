# GithubComQeeqezApiInternalErrorsErrorResponse

Standard error response returned by the API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | HTTP status code | [optional] 
**details** | **str** | Optional details about the error | [optional] 
**error** | **str** | Error message describing what went wrong | [optional] 

## Example

```python
from rixl_api.models.github_com_qeeqez_api_internal_errors_error_response import GithubComQeeqezApiInternalErrorsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComQeeqezApiInternalErrorsErrorResponse from a JSON string
github_com_qeeqez_api_internal_errors_error_response_instance = GithubComQeeqezApiInternalErrorsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComQeeqezApiInternalErrorsErrorResponse.to_json())

# convert the object into a dict
github_com_qeeqez_api_internal_errors_error_response_dict = github_com_qeeqez_api_internal_errors_error_response_instance.to_dict()
# create an instance of GithubComQeeqezApiInternalErrorsErrorResponse from a dict
github_com_qeeqez_api_internal_errors_error_response_from_dict = GithubComQeeqezApiInternalErrorsErrorResponse.from_dict(github_com_qeeqez_api_internal_errors_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


