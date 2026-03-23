# Post


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**feed_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**plan_type** | [**GithubComQeeqezApiDbSqlcPlanType**](GithubComQeeqezApiDbSqlcPlanType.md) |  | [optional] 
**type** | [**PostType**](PostType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**video** | [**GithubComQeeqezApiInternalVideosVideoResponse**](GithubComQeeqezApiInternalVideosVideoResponse.md) |  | [optional] 

## Example

```python
from rixl_api.models.post import Post

# TODO update the JSON string below
json = "{}"
# create an instance of Post from a JSON string
post_instance = Post.from_json(json)
# print the JSON string representation of the object
print(Post.to_json())

# convert the object into a dict
post_dict = post_instance.to_dict()
# create an instance of Post from a dict
post_from_dict = Post.from_dict(post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


