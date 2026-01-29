# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_agent**](DefaultApi.md#delete_delete_agent) | **DELETE** /api/v2/projects/{project_id}/agents/{agent_id} | 
[**delete_delete_project**](DefaultApi.md#delete_delete_project) | **DELETE** /api/v2/projects/{project_id} | 
[**delete_delete_theme**](DefaultApi.md#delete_delete_theme) | **DELETE** /api/v2/projects/{project_id}/review-themes/{theme_id} | Delete Review Theme
[**get_get_agent**](DefaultApi.md#get_get_agent) | **GET** /api/v2/projects/{project_id}/agents/{agent_id} | 
[**get_get_agents**](DefaultApi.md#get_get_agents) | **GET** /api/v2/projects/{project_id}/agents | 
[**get_get_theme**](DefaultApi.md#get_get_theme) | **GET** /api/v2/projects/{project_id}/review-themes/{theme_id} | Get Review Theme
[**get_list_themes**](DefaultApi.md#get_list_themes) | **GET** /api/v2/projects/{project_id}/review-themes | List Review Themes
[**patch_update_agent**](DefaultApi.md#patch_update_agent) | **PATCH** /api/v2/projects/{project_id}/agents/{agent_id} | 
[**patch_update_evaluation_criteria**](DefaultApi.md#patch_update_evaluation_criteria) | **PATCH** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id} | 
[**post_create_agent**](DefaultApi.md#post_create_agent) | **POST** /api/v2/projects/{project_id}/agents | 
[**post_create_criteria_version**](DefaultApi.md#post_create_criteria_version) | **POST** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/versions | 
[**post_create_evaluation_criteria**](DefaultApi.md#post_create_evaluation_criteria) | **POST** /api/v2/projects/{project_id}/evaluation-criteria | 
[**post_generate_benchmark_insights**](DefaultApi.md#post_generate_benchmark_insights) | **POST** /api/v2/projects/{project_id}/experimental/test-insights/benchmark-generate | 
[**post_generate_comparison_insights**](DefaultApi.md#post_generate_comparison_insights) | **POST** /api/v2/projects/{project_id}/experimental/test-insights/generate | 
[**post_generate_insights**](DefaultApi.md#post_generate_insights) | **POST** /api/v2/projects/{project_id}/experimental/evaluation-insights/generate | 
[**post_metrics**](DefaultApi.md#post_metrics) | **POST** /api/v0/otel/v1/metrics | 
[**post_reactivate_user**](DefaultApi.md#post_reactivate_user) | **POST** /admin/api/accounts/{account_id}/users/{user_id}/reactivate | 
[**post_replicate_theme**](DefaultApi.md#post_replicate_theme) | **POST** /api/v2/projects/{project_id}/review-themes | Create Review Theme
[**post_traces**](DefaultApi.md#post_traces) | **POST** /api/v0/otel/v1/traces | 
[**put_update_theme**](DefaultApi.md#put_update_theme) | **PUT** /api/v2/projects/{project_id}/review-themes/{theme_id} | Update Review Theme

# **delete_delete_agent**
> object delete_delete_agent(project_id, agent_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
agent_id = NULL # object | 

try:
    api_response = api_instance.delete_delete_agent(project_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_delete_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **agent_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_project**
> object delete_delete_project(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 

try:
    api_response = api_instance.delete_delete_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_theme**
> object delete_delete_theme(project_id, theme_id)

Delete Review Theme

 Delete a review theme from the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
theme_id = NULL # object | 

try:
    # Delete Review Theme
    api_response = api_instance.delete_delete_theme(project_id, theme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_delete_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **theme_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_agent**
> AgentInfo1 get_get_agent(project_id, agent_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
agent_id = NULL # object | 

try:
    api_response = api_instance.get_get_agent(project_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_get_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **agent_id** | [**object**](.md)|  | 

### Return type

[**AgentInfo1**](AgentInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_agents**
> GetAgentsResponsePayload get_get_agents(project_id, page=page, page_size=page_size, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
name = NULL # object |  (optional)

try:
    api_response = api_instance.get_get_agents(project_id, page=page, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_get_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **name** | [**object**](.md)|  | [optional] 

### Return type

[**GetAgentsResponsePayload**](GetAgentsResponsePayload.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_theme**
> ReviewThemeReplicationInfo1 get_get_theme(project_id, theme_id)

Get Review Theme

 Retrieve details for a specific review theme by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
theme_id = NULL # object | 

try:
    # Get Review Theme
    api_response = api_instance.get_get_theme(project_id, theme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_get_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **theme_id** | [**object**](.md)|  | 

### Return type

[**ReviewThemeReplicationInfo1**](ReviewThemeReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_themes**
> ReviewThemeReplicationListResponse get_list_themes(project_id, page=page, page_size=page_size)

List Review Themes

 Retrieve a paginated list of review themes for the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Review Themes
    api_response = api_instance.get_list_themes(project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_list_themes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**ReviewThemeReplicationListResponse**](ReviewThemeReplicationListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_agent**
> AgentInfo1 patch_update_agent(project_id, agent_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
agent_id = NULL # object | 
body = swagger_client.UpdateAgentRequest() # UpdateAgentRequest |  (optional)

try:
    api_response = api_instance.patch_update_agent(project_id, agent_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_update_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **agent_id** | [**object**](.md)|  | 
 **body** | [**UpdateAgentRequest**](UpdateAgentRequest.md)|  | [optional] 

### Return type

[**AgentInfo1**](AgentInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_evaluation_criteria**
> object patch_update_evaluation_criteria(project_id, criteria_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
body = swagger_client.UpdateEvaluationCriteriaRequest() # UpdateEvaluationCriteriaRequest |  (optional)

try:
    api_response = api_instance.patch_update_evaluation_criteria(project_id, criteria_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_update_evaluation_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **body** | [**UpdateEvaluationCriteriaRequest**](UpdateEvaluationCriteriaRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_agent**
> AgentInfo1 post_create_agent(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreateAgentRequest() # CreateAgentRequest |  (optional)

try:
    api_response = api_instance.post_create_agent(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_create_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**CreateAgentRequest**](CreateAgentRequest.md)|  | [optional] 

### Return type

[**AgentInfo1**](AgentInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_criteria_version**
> EvaluationCriteriaVersionInfo1 post_create_criteria_version(project_id, criteria_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
body = swagger_client.CreateCriteriaVersionRequest() # CreateCriteriaVersionRequest |  (optional)

try:
    api_response = api_instance.post_create_criteria_version(project_id, criteria_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_create_criteria_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **body** | [**CreateCriteriaVersionRequest**](CreateCriteriaVersionRequest.md)|  | [optional] 

### Return type

[**EvaluationCriteriaVersionInfo1**](EvaluationCriteriaVersionInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_evaluation_criteria**
> CreateEvaluationCriteriaResponse post_create_evaluation_criteria(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreateEvaluationCriteriaRequest() # CreateEvaluationCriteriaRequest |  (optional)

try:
    api_response = api_instance.post_create_evaluation_criteria(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_create_evaluation_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**CreateEvaluationCriteriaRequest**](CreateEvaluationCriteriaRequest.md)|  | [optional] 

### Return type

[**CreateEvaluationCriteriaResponse**](CreateEvaluationCriteriaResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_benchmark_insights**
> GenerateBenchmarkInsightsResponse post_generate_benchmark_insights(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.GenerateBenchmarkInsightsRequest() # GenerateBenchmarkInsightsRequest |  (optional)

try:
    api_response = api_instance.post_generate_benchmark_insights(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_generate_benchmark_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**GenerateBenchmarkInsightsRequest**](GenerateBenchmarkInsightsRequest.md)|  | [optional] 

### Return type

[**GenerateBenchmarkInsightsResponse**](GenerateBenchmarkInsightsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_comparison_insights**
> GenerateComparisonInsightsResponse post_generate_comparison_insights(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.GenerateComparisonInsightsRequest() # GenerateComparisonInsightsRequest |  (optional)

try:
    api_response = api_instance.post_generate_comparison_insights(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_generate_comparison_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**GenerateComparisonInsightsRequest**](GenerateComparisonInsightsRequest.md)|  | [optional] 

### Return type

[**GenerateComparisonInsightsResponse**](GenerateComparisonInsightsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_insights**
> GenerateInsightsResponse post_generate_insights(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.GenerateInsightsRequest() # GenerateInsightsRequest |  (optional)

try:
    api_response = api_instance.post_generate_insights(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_generate_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**GenerateInsightsRequest**](GenerateInsightsRequest.md)|  | [optional] 

### Return type

[**GenerateInsightsResponse**](GenerateInsightsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_metrics**
> post_metrics()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    api_instance.post_metrics()
except ApiException as e:
    print("Exception when calling DefaultApi->post_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reactivate_user**
> object post_reactivate_user(account_id, user_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
account_id = NULL # object | 
user_id = NULL # object | 

try:
    api_response = api_instance.post_reactivate_user(account_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_reactivate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**object**](.md)|  | 
 **user_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_replicate_theme**
> ReviewThemeReplicationInfo1 post_replicate_theme(project_id, body=body)

Create Review Theme

 Create or upsert a review theme for the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.ReplicateReviewThemeRequest() # ReplicateReviewThemeRequest |  (optional)

try:
    # Create Review Theme
    api_response = api_instance.post_replicate_theme(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_replicate_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**ReplicateReviewThemeRequest**](ReplicateReviewThemeRequest.md)|  | [optional] 

### Return type

[**ReviewThemeReplicationInfo1**](ReviewThemeReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_traces**
> post_traces()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    api_instance.post_traces()
except ApiException as e:
    print("Exception when calling DefaultApi->post_traces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_theme**
> ReviewThemeReplicationInfo1 put_update_theme(project_id, theme_id, body=body)

Update Review Theme

 Update an existing review theme.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
theme_id = NULL # object | 
body = swagger_client.UpdateReviewThemeReplicationRequest() # UpdateReviewThemeReplicationRequest |  (optional)

try:
    # Update Review Theme
    api_response = api_instance.put_update_theme(project_id, theme_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_update_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **theme_id** | [**object**](.md)|  | 
 **body** | [**UpdateReviewThemeReplicationRequest**](UpdateReviewThemeReplicationRequest.md)|  | [optional] 

### Return type

[**ReviewThemeReplicationInfo1**](ReviewThemeReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

