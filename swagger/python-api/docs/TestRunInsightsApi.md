# swagger_client.TestRunInsightsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_test_run_insights**](TestRunInsightsApi.md#get_get_test_run_insights) | **GET** /api/v2/projects/{project_id}/experimental/test-run-insights/{test_run_id} | Get Test Run Insights

# **get_get_test_run_insights**
> GetTestRunInsightsResponse get_get_test_run_insights(project_id, test_run_id)

Get Test Run Insights

 Retrieve all insights associated with a specific test run.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TestRunInsightsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
test_run_id = NULL # object | 

try:
    # Get Test Run Insights
    api_response = api_instance.get_get_test_run_insights(project_id, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunInsightsApi->get_get_test_run_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **test_run_id** | [**object**](.md)|  | 

### Return type

[**GetTestRunInsightsResponse**](GetTestRunInsightsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

