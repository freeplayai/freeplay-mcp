# swagger_client.EvaluationCriteriaApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_criteria_version**](EvaluationCriteriaApi.md#delete_delete_criteria_version) | **DELETE** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/versions/{version_id} | Delete Evaluation Criteria Version
[**delete_delete_evaluation_criteria**](EvaluationCriteriaApi.md#delete_delete_evaluation_criteria) | **DELETE** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id} | Delete Evaluation Criteria
[**get_get_criteria_version**](EvaluationCriteriaApi.md#get_get_criteria_version) | **GET** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/versions/{version_id} | Get Evaluation Criteria Version
[**get_get_evaluation_criteria**](EvaluationCriteriaApi.md#get_get_evaluation_criteria) | **GET** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id} | Get Evaluation Criteria
[**get_list_criteria_versions**](EvaluationCriteriaApi.md#get_list_criteria_versions) | **GET** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/versions | List Evaluation Criteria Versions
[**get_list_evaluation_criteria**](EvaluationCriteriaApi.md#get_list_evaluation_criteria) | **GET** /api/v2/projects/{project_id}/evaluation-criteria | List Evaluation Criteria
[**patch_disable_criteria**](EvaluationCriteriaApi.md#patch_disable_criteria) | **PATCH** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/disable | Disable Criteria
[**patch_enable_criteria**](EvaluationCriteriaApi.md#patch_enable_criteria) | **PATCH** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/enable | Enable Criteria
[**patch_reorder_criteria**](EvaluationCriteriaApi.md#patch_reorder_criteria) | **PATCH** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/reorder | Reorder Criteria
[**post_deploy_criteria_version**](EvaluationCriteriaApi.md#post_deploy_criteria_version) | **POST** /api/v2/projects/{project_id}/evaluation-criteria/id/{criteria_id}/versions/{version_id}/deploy | Deploy Evaluation Criteria Version

# **delete_delete_criteria_version**
> object delete_delete_criteria_version(project_id, criteria_id, version_id)

Delete Evaluation Criteria Version

 Permanently delete an evaluation criteria version. Use to clean up draft or unused versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
version_id = NULL # object | 

try:
    # Delete Evaluation Criteria Version
    api_response = api_instance.delete_delete_criteria_version(project_id, criteria_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->delete_delete_criteria_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_evaluation_criteria**
> object delete_delete_evaluation_criteria(project_id, criteria_id)

Delete Evaluation Criteria

 Permanently delete an evaluation criteria and all its versions. Use when retiring criteria no longer needed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 

try:
    # Delete Evaluation Criteria
    api_response = api_instance.delete_delete_evaluation_criteria(project_id, criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->delete_delete_evaluation_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_criteria_version**
> EvaluationCriteriaVersionInfo1 get_get_criteria_version(project_id, criteria_id, version_id)

Get Evaluation Criteria Version

 Retrieve a specific evaluation criteria version. Use to inspect version configuration or compare with other versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
version_id = NULL # object | 

try:
    # Get Evaluation Criteria Version
    api_response = api_instance.get_get_criteria_version(project_id, criteria_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->get_get_criteria_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 

### Return type

[**EvaluationCriteriaVersionInfo1**](EvaluationCriteriaVersionInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_evaluation_criteria**
> EvaluationCriteriaInfo1 get_get_evaluation_criteria(project_id, criteria_id)

Get Evaluation Criteria

 Retrieve an evaluation criteria's configuration by ID. Use to inspect criteria settings or get the latest version ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 

try:
    # Get Evaluation Criteria
    api_response = api_instance.get_get_evaluation_criteria(project_id, criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->get_get_evaluation_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 

### Return type

[**EvaluationCriteriaInfo1**](EvaluationCriteriaInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_criteria_versions**
> EvaluationCriteriaVersionListResponse get_list_criteria_versions(project_id, criteria_id, page=page, page_size=page_size)

List Evaluation Criteria Versions

 Retrieve all versions of an evaluation criteria. Use to view version history or compare changes over time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Evaluation Criteria Versions
    api_response = api_instance.get_list_criteria_versions(project_id, criteria_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->get_list_criteria_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**EvaluationCriteriaVersionListResponse**](EvaluationCriteriaVersionListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_evaluation_criteria**
> EvaluationCriteriaListResponse get_list_evaluation_criteria(project_id, page=page, page_size=page_size)

List Evaluation Criteria

 Retrieve all evaluation criteria in a project. Use to discover available criteria or build criteria management UIs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Evaluation Criteria
    api_response = api_instance.get_list_evaluation_criteria(project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->get_list_evaluation_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**EvaluationCriteriaListResponse**](EvaluationCriteriaListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_disable_criteria**
> object patch_disable_criteria(project_id, criteria_id)

Disable Criteria

 Deactivate an evaluation criteria without deleting it. Use to temporarily pause the use of a given criteria in evaluations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 

try:
    # Disable Criteria
    api_response = api_instance.patch_disable_criteria(project_id, criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->patch_disable_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_enable_criteria**
> object patch_enable_criteria(project_id, criteria_id)

Enable Criteria

 Activate an evaluation criteria for use in test runs and online evaluations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 

try:
    # Enable Criteria
    api_response = api_instance.patch_enable_criteria(project_id, criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->patch_enable_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_reorder_criteria**
> object patch_reorder_criteria(project_id, criteria_id, body=body)

Reorder Criteria

 Change the display order of evaluation criteria in the Freeplay UI. Use to organize criteria in a logical sequence for human review workflows.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
body = swagger_client.ReorderCriteriaRequest() # ReorderCriteriaRequest |  (optional)

try:
    # Reorder Criteria
    api_response = api_instance.patch_reorder_criteria(project_id, criteria_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->patch_reorder_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **body** | [**ReorderCriteriaRequest**](ReorderCriteriaRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_deploy_criteria_version**
> object post_deploy_criteria_version(project_id, criteria_id, version_id)

Deploy Evaluation Criteria Version

 Activate an evaluation criteria version for use in evaluations. Use to promote a tested version to production.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EvaluationCriteriaApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
criteria_id = NULL # object | 
version_id = NULL # object | 

try:
    # Deploy Evaluation Criteria Version
    api_response = api_instance.post_deploy_criteria_version(project_id, criteria_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationCriteriaApi->post_deploy_criteria_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **criteria_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

