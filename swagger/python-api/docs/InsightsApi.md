# swagger_client.InsightsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_insights**](InsightsApi.md#get_get_insights) | **GET** /api/v2/projects/{project_id}/insights | Get Insights

# **get_get_insights**
> GetInsightsResponsePayload get_get_insights(project_id, page=page, page_size=page_size, prompt_template_id=prompt_template_id, agent_id=agent_id)

Get Insights

 Retrieve a paginated list of insights for a project. Use to discover insights or filter by prompt template or agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InsightsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
prompt_template_id = null # object |  (optional) (default to null)
agent_id = null # object |  (optional) (default to null)

try:
    # Get Insights
    api_response = api_instance.get_get_insights(project_id, page=page, page_size=page_size, prompt_template_id=prompt_template_id, agent_id=agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightsApi->get_get_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **prompt_template_id** | [**object**](.md)|  | [optional] [default to null]
 **agent_id** | [**object**](.md)|  | [optional] [default to null]

### Return type

[**GetInsightsResponsePayload**](GetInsightsResponsePayload.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

