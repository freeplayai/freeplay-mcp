# swagger_client.SearchAnalyticsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_sessions_filtered**](SearchAnalyticsApi.md#get_get_sessions_filtered) | **GET** /api/v2/projects/{project_id}/sessions | List Sessions
[**post_get_all_completion_summaries**](SearchAnalyticsApi.md#post_get_all_completion_summaries) | **POST** /api/v2/projects/{project_id}/completions/statistics | Get All Completion Statistics
[**post_get_completion_summary**](SearchAnalyticsApi.md#post_get_completion_summary) | **POST** /api/v2/projects/{project_id}/completions/statistics/{prompt_template_id} | Get Completion Statistics
[**post_search_completions**](SearchAnalyticsApi.md#post_search_completions) | **POST** /api/v2/projects/{project_id}/search/completions | Search Completions
[**post_search_sessions**](SearchAnalyticsApi.md#post_search_sessions) | **POST** /api/v2/projects/{project_id}/search/sessions | Search Sessions
[**post_search_traces**](SearchAnalyticsApi.md#post_search_traces) | **POST** /api/v2/projects/{project_id}/search/traces | Search Traces

# **get_get_sessions_filtered**
> object get_get_sessions_filtered(project_id, page=page, page_size=page_size, to_date=to_date, from_date=from_date, test_list=test_list, test_run_id=test_run_id, prompt_name=prompt_name, review_queue_id=review_queue_id)

List Sessions

 Retrieve sessions with their completions, ordered by most recent first. Use to display conversation history or analyze LLM usage patterns. Traces are referenced by ID but not expanded.  Filter by custom metadata using query parameters prefixed with `custom_metadata.` (e.g., `custom_metadata.user_id=123`).  Prefer using the `/search/sessions` endpoint for more advanced filtering.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchAnalyticsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 10 # object |  (optional) (default to 10)
to_date = NULL # object |  (optional)
from_date = NULL # object |  (optional)
test_list = null # object |  (optional) (default to null)
test_run_id = null # object |  (optional) (default to null)
prompt_name = null # object |  (optional) (default to null)
review_queue_id = null # object |  (optional) (default to null)

try:
    # List Sessions
    api_response = api_instance.get_get_sessions_filtered(project_id, page=page, page_size=page_size, to_date=to_date, from_date=from_date, test_list=test_list, test_run_id=test_run_id, prompt_name=prompt_name, review_queue_id=review_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAnalyticsApi->get_get_sessions_filtered: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 10]
 **to_date** | [**object**](.md)|  | [optional] 
 **from_date** | [**object**](.md)|  | [optional] 
 **test_list** | [**object**](.md)|  | [optional] [default to null]
 **test_run_id** | [**object**](.md)|  | [optional] [default to null]
 **prompt_name** | [**object**](.md)|  | [optional] [default to null]
 **review_queue_id** | [**object**](.md)|  | [optional] [default to null]

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_all_completion_summaries**
> CompletionSummaryStatsInfo post_get_all_completion_summaries(project_id, body=body)

Get All Completion Statistics

 Retrieve aggregate evaluation statistics across all prompts for a date range. Use for dashboard metrics or trend analysis.  Maximum date range is 30 days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchAnalyticsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.GetCompletionSummaryInfo() # GetCompletionSummaryInfo |  (optional)

try:
    # Get All Completion Statistics
    api_response = api_instance.post_get_all_completion_summaries(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAnalyticsApi->post_get_all_completion_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**GetCompletionSummaryInfo**](GetCompletionSummaryInfo.md)|  | [optional] 

### Return type

[**CompletionSummaryStatsInfo**](CompletionSummaryStatsInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_completion_summary**
> CompletionSummaryStatsInfo post_get_completion_summary(project_id, prompt_template_id, body=body)

Get Completion Statistics

 Retrieve evaluation statistics for a specific prompt template. Use to track quality metrics for individual prompts.  Maximum date range is 30 days.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchAnalyticsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
prompt_template_id = NULL # object | 
body = swagger_client.GetCompletionSummaryInfo1() # GetCompletionSummaryInfo1 |  (optional)

try:
    # Get Completion Statistics
    api_response = api_instance.post_get_completion_summary(project_id, prompt_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAnalyticsApi->post_get_completion_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **prompt_template_id** | [**object**](.md)|  | 
 **body** | [**GetCompletionSummaryInfo1**](GetCompletionSummaryInfo1.md)|  | [optional] 

### Return type

[**CompletionSummaryStatsInfo**](CompletionSummaryStatsInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_completions**
> CompletionSearchResponse post_search_completions(project_id, body=body, page=page, page_size=page_size, include_children=include_children)

Search Completions

 Query LLM completions using advanced filters. Use to find specific prompts and responses, filter by evaluation results or metadata, prompt templates, latency, and more.  Supports pagination and optional inclusion of all child traces and completions within the session, using the `include_children` parameter.  For filter operators and examples, see: https://docs.freeplay.ai/openapi/search-api-operators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchAnalyticsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.SearchRequest() # SearchRequest |  (optional)
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
include_children = false # object |  (optional) (default to false)

try:
    # Search Completions
    api_response = api_instance.post_search_completions(project_id, body=body, page=page, page_size=page_size, include_children=include_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAnalyticsApi->post_search_completions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**SearchRequest**](SearchRequest.md)|  | [optional] 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **include_children** | [**object**](.md)|  | [optional] [default to false]

### Return type

[**CompletionSearchResponse**](CompletionSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_sessions**
> SessionSearchResponse post_search_sessions(project_id, body=body, page=page, page_size=page_size, include_children=include_children)

Search Sessions

 Query sessions using advanced filters. Use to find specific conversations or filter by metadata.  Supports pagination and optional inclusion of all traces and completions within the session, using the `include_children` parameter.  For filter operators and examples, see: https://docs.freeplay.ai/openapi/search-api-operators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchAnalyticsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.SearchRequest1() # SearchRequest1 |  (optional)
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
include_children = false # object |  (optional) (default to false)

try:
    # Search Sessions
    api_response = api_instance.post_search_sessions(project_id, body=body, page=page, page_size=page_size, include_children=include_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAnalyticsApi->post_search_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**SearchRequest1**](SearchRequest1.md)|  | [optional] 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **include_children** | [**object**](.md)|  | [optional] [default to false]

### Return type

[**SessionSearchResponse**](SessionSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_traces**
> TraceSearchResponse post_search_traces(project_id, body=body, page=page, page_size=page_size, include_children=include_children)

Search Traces

 Query traces using advanced filters. Use to find specific trace executions, filter by metadata, or analyze trace patterns.  Supports pagination and optional inclusion of all child traces and completions within the session, using the `include_children` parameter.  For filter operators and examples, see: https://docs.freeplay.ai/openapi/search-api-operators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchAnalyticsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.SearchRequest1() # SearchRequest1 |  (optional)
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
include_children = false # object |  (optional) (default to false)

try:
    # Search Traces
    api_response = api_instance.post_search_traces(project_id, body=body, page=page, page_size=page_size, include_children=include_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAnalyticsApi->post_search_traces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**SearchRequest1**](SearchRequest1.md)|  | [optional] 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **include_children** | [**object**](.md)|  | [optional] [default to false]

### Return type

[**TraceSearchResponse**](TraceSearchResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

