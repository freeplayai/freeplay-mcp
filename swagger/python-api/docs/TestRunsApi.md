# swagger_client.TestRunsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_test_run_results**](TestRunsApi.md#get_get_test_run_results) | **GET** /api/v2/projects/{project_id}/test-runs/id/{test_run_id} | Get Test Run Results
[**get_get_test_runs**](TestRunsApi.md#get_get_test_runs) | **GET** /api/v2/projects/{project_id}/test-runs | List Test Runs
[**post_create_with_test_cases**](TestRunsApi.md#post_create_with_test_cases) | **POST** /api/v2/projects/{project_id}/test-runs | Create Test Run

# **get_get_test_run_results**
> TestRunResponseInfo get_get_test_run_results(project_id, test_run_id)

Get Test Run Results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TestRunsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
test_run_id = NULL # object | 

try:
    # Get Test Run Results
    api_response = api_instance.get_get_test_run_results(project_id, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunsApi->get_get_test_run_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **test_run_id** | [**object**](.md)|  | 

### Return type

[**TestRunResponseInfo**](TestRunResponseInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_test_runs**
> TestRunListResponseInfo get_get_test_runs(project_id, page=page, page_size=page_size)

List Test Runs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TestRunsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 100 # object |  (optional) (default to 100)

try:
    # List Test Runs
    api_response = api_instance.get_get_test_runs(project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunsApi->get_get_test_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 100]

### Return type

[**TestRunListResponseInfo**](TestRunListResponseInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_with_test_cases**
> TestRunWithTestCasesInfo post_create_with_test_cases(project_id, body=body)

Create Test Run

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TestRunsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreateTestRunInfo() # CreateTestRunInfo |  (optional)

try:
    # Create Test Run
    api_response = api_instance.post_create_with_test_cases(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunsApi->post_create_with_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**CreateTestRunInfo**](CreateTestRunInfo.md)|  | [optional] 

### Return type

[**TestRunWithTestCasesInfo**](TestRunWithTestCasesInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

