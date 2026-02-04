# swagger_client.PromptOptimizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_prompt_optimization_job**](PromptOptimizationApi.md#get_get_prompt_optimization_job) | **GET** /api/v2/projects/{project_id}/prompt-optimization-jobs/{job_id} | Get prompt optimization job status and details.
[**get_list_prompt_optimization_jobs**](PromptOptimizationApi.md#get_list_prompt_optimization_jobs) | **GET** /api/v2/projects/{project_id}/prompt-optimization-jobs | List prompt optimization jobs for the project.
[**post_cancel_prompt_optimization_job**](PromptOptimizationApi.md#post_cancel_prompt_optimization_job) | **POST** /api/v2/projects/{project_id}/prompt-optimization-jobs/{job_id}/cancel | Cancel a pending or in-progress prompt optimization job.
[**post_start_prompt_optimization_job**](PromptOptimizationApi.md#post_start_prompt_optimization_job) | **POST** /api/v2/projects/{project_id}/prompt-optimization-jobs | Start a new prompt optimization job.

# **get_get_prompt_optimization_job**
> PromptOptimizationJobStatusResponse get_get_prompt_optimization_job(project_id, job_id)

Get prompt optimization job status and details.

 Returns the current status of the prompt optimization job, including progress information for polling. When complete, includes the optimized_version_id and optionally test_run_id and comparison_id if run_test_after_optimization was True.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptOptimizationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
job_id = NULL # object | 

try:
    # Get prompt optimization job status and details.
    api_response = api_instance.get_get_prompt_optimization_job(project_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptOptimizationApi->get_get_prompt_optimization_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **job_id** | [**object**](.md)|  | 

### Return type

[**PromptOptimizationJobStatusResponse**](PromptOptimizationJobStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_prompt_optimization_jobs**
> PromptOptimizationJobListResponse get_list_prompt_optimization_jobs(project_id, page=page, page_size=page_size, status=status)

List prompt optimization jobs for the project.

 Returns a paginated list of prompt optimization jobs, sorted by creation date (newest first). Optionally filter by status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptOptimizationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
status = null # object |  (optional) (default to null)

try:
    # List prompt optimization jobs for the project.
    api_response = api_instance.get_list_prompt_optimization_jobs(project_id, page=page, page_size=page_size, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptOptimizationApi->get_list_prompt_optimization_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **status** | [**object**](.md)|  | [optional] [default to null]

### Return type

[**PromptOptimizationJobListResponse**](PromptOptimizationJobListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cancel_prompt_optimization_job**
> object post_cancel_prompt_optimization_job(project_id, job_id)

Cancel a pending or in-progress prompt optimization job.

 Only jobs that have not yet completed can be cancelled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptOptimizationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
job_id = NULL # object | 

try:
    # Cancel a pending or in-progress prompt optimization job.
    api_response = api_instance.post_cancel_prompt_optimization_job(project_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptOptimizationApi->post_cancel_prompt_optimization_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **job_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_start_prompt_optimization_job**
> PromptOptimizationJobCreatedResponse post_start_prompt_optimization_job(project_id, body=body)

Start a new prompt optimization job.

 Creates an asynchronous job that optimizes the specified prompt template version. The job will analyze examples from the dataset and generate an improved prompt.  When `run_test_after_optimization` is True (default), the job will also run baseline and optimized test runs and create a comparison.  Poll GET /prompt-optimization-jobs/{job_id} to check job status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptOptimizationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.StartPromptOptimizationJobRequest() # StartPromptOptimizationJobRequest |  (optional)

try:
    # Start a new prompt optimization job.
    api_response = api_instance.post_start_prompt_optimization_job(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptOptimizationApi->post_start_prompt_optimization_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**StartPromptOptimizationJobRequest**](StartPromptOptimizationJobRequest.md)|  | [optional] 

### Return type

[**PromptOptimizationJobCreatedResponse**](PromptOptimizationJobCreatedResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

