# swagger_client.AgentDatasetsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bulk_delete_agent_dataset_test_cases**](AgentDatasetsApi.md#delete_bulk_delete_agent_dataset_test_cases) | **DELETE** /api/v2/projects/{project_id}/agent-datasets/{dataset_id}/test-cases/bulk | Bulk Delete Agent Test Cases
[**delete_delete_agent_dataset**](AgentDatasetsApi.md#delete_delete_agent_dataset) | **DELETE** /api/v2/projects/{project_id}/agent-datasets/{dataset_id} | Delete Agent Dataset
[**delete_delete_agent_dataset_test_case**](AgentDatasetsApi.md#delete_delete_agent_dataset_test_case) | **DELETE** /api/v2/projects/{project_id}/agent-datasets/{dataset_id}/test-cases/{test_case_id} | Delete Agent Test Case
[**get_get_agent_dataset**](AgentDatasetsApi.md#get_get_agent_dataset) | **GET** /api/v2/projects/{project_id}/agent-datasets/{dataset_id} | Get Agent Dataset
[**get_get_agent_dataset_test_case**](AgentDatasetsApi.md#get_get_agent_dataset_test_case) | **GET** /api/v2/projects/{project_id}/agent-datasets/{dataset_id}/test-cases/{test_case_id} | Get Agent Test Case
[**get_get_agent_dataset_test_cases**](AgentDatasetsApi.md#get_get_agent_dataset_test_cases) | **GET** /api/v2/projects/{project_id}/agent-datasets/{dataset_id}/test-cases | List Agent Test Cases
[**get_get_agent_datasets**](AgentDatasetsApi.md#get_get_agent_datasets) | **GET** /api/v2/projects/{project_id}/agent-datasets | List Agent Datasets
[**patch_update_agent_dataset**](AgentDatasetsApi.md#patch_update_agent_dataset) | **PATCH** /api/v2/projects/{project_id}/agent-datasets/{dataset_id} | Update Agent Dataset
[**patch_update_agent_dataset_test_case**](AgentDatasetsApi.md#patch_update_agent_dataset_test_case) | **PATCH** /api/v2/projects/{project_id}/agent-datasets/{dataset_id}/test-cases/{test_case_id} | Update Agent Test Case
[**post_bulk_create_agent_dataset_test_cases**](AgentDatasetsApi.md#post_bulk_create_agent_dataset_test_cases) | **POST** /api/v2/projects/{project_id}/agent-datasets/{dataset_id}/test-cases/bulk | Bulk Create Agent Test Cases
[**post_create_agent_dataset**](AgentDatasetsApi.md#post_create_agent_dataset) | **POST** /api/v2/projects/{project_id}/agent-datasets | Create Agent-Level Dataset

# **delete_bulk_delete_agent_dataset_test_cases**
> object delete_bulk_delete_agent_dataset_test_cases(project_id, dataset_id, body=body)

Bulk Delete Agent Test Cases

 Remove multiple agent test cases in a single request. Use for batch cleanup operations.  Maximum 100 test cases per request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.BulkDeleteAgentTestCasesRequest() # BulkDeleteAgentTestCasesRequest |  (optional)

try:
    # Bulk Delete Agent Test Cases
    api_response = api_instance.delete_bulk_delete_agent_dataset_test_cases(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->delete_bulk_delete_agent_dataset_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**BulkDeleteAgentTestCasesRequest**](BulkDeleteAgentTestCasesRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_agent_dataset**
> object delete_delete_agent_dataset(project_id, dataset_id)

Delete Agent Dataset

 Archive an agent dataset and its test cases. Use when retiring datasets no longer needed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 

try:
    # Delete Agent Dataset
    api_response = api_instance.delete_delete_agent_dataset(project_id, dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->delete_delete_agent_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_agent_dataset_test_case**
> object delete_delete_agent_dataset_test_case(project_id, dataset_id, test_case_id)

Delete Agent Test Case

 Remove a test case from an agent dataset. Use to clean up invalid or outdated test cases.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
test_case_id = NULL # object | 

try:
    # Delete Agent Test Case
    api_response = api_instance.delete_delete_agent_dataset_test_case(project_id, dataset_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->delete_delete_agent_dataset_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **test_case_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_agent_dataset**
> AgentDatasetResponse1 get_get_agent_dataset(project_id, dataset_id)

Get Agent Dataset

 Retrieve an agent dataset's metadata by ID. Use to check dataset configuration or compatible agents.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 

try:
    # Get Agent Dataset
    api_response = api_instance.get_get_agent_dataset(project_id, dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->get_get_agent_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 

### Return type

[**AgentDatasetResponse1**](AgentDatasetResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_agent_dataset_test_case**
> AgentTestCaseResponse1 get_get_agent_dataset_test_case(project_id, dataset_id, test_case_id)

Get Agent Test Case

 Retrieve a specific agent test case by ID. Use to inspect test case details or debug test run results.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
test_case_id = NULL # object | 

try:
    # Get Agent Test Case
    api_response = api_instance.get_get_agent_dataset_test_case(project_id, dataset_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->get_get_agent_dataset_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **test_case_id** | [**object**](.md)|  | 

### Return type

[**AgentTestCaseResponse1**](AgentTestCaseResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_agent_dataset_test_cases**
> AgentTestCasesListResponse get_get_agent_dataset_test_cases(project_id, dataset_id, page=page, page_size=page_size)

List Agent Test Cases

 Retrieve all test cases (row-level values) in an agent dataset. Use to review dataset contents or export for analysis.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Agent Test Cases
    api_response = api_instance.get_get_agent_dataset_test_cases(project_id, dataset_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->get_get_agent_dataset_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**AgentTestCasesListResponse**](AgentTestCasesListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_agent_datasets**
> AgentDatasetsListResponse get_get_agent_datasets(project_id, page=page, page_size=page_size, id=id, name=name)

List Agent Datasets

 Retrieve all agent-level datasets in a project. Use to discover available datasets for agent test runs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
id = NULL # object |  (optional)
name = NULL # object |  (optional)

try:
    # List Agent Datasets
    api_response = api_instance.get_get_agent_datasets(project_id, page=page, page_size=page_size, id=id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->get_get_agent_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **id** | [**object**](.md)|  | [optional] 
 **name** | [**object**](.md)|  | [optional] 

### Return type

[**AgentDatasetsListResponse**](AgentDatasetsListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_agent_dataset**
> AgentDatasetResponse1 patch_update_agent_dataset(project_id, dataset_id, body=body)

Update Agent Dataset

 Modify an agent dataset's name, description, or compatible agents. Use to evolve datasets as agent requirements change.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.UpdateAgentDatasetRequest() # UpdateAgentDatasetRequest |  (optional)

try:
    # Update Agent Dataset
    api_response = api_instance.patch_update_agent_dataset(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->patch_update_agent_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**UpdateAgentDatasetRequest**](UpdateAgentDatasetRequest.md)|  | [optional] 

### Return type

[**AgentDatasetResponse1**](AgentDatasetResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_agent_dataset_test_case**
> AgentTestCaseResponse1 patch_update_agent_dataset_test_case(project_id, dataset_id, test_case_id, body=body)

Update Agent Test Case

 Modify an existing agent test case's inputs, outputs, or metadata. Use to correct errors or update expected outputs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
test_case_id = NULL # object | 
body = swagger_client.AgentTestCase1() # AgentTestCase1 |  (optional)

try:
    # Update Agent Test Case
    api_response = api_instance.patch_update_agent_dataset_test_case(project_id, dataset_id, test_case_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->patch_update_agent_dataset_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **test_case_id** | [**object**](.md)|  | 
 **body** | [**AgentTestCase1**](AgentTestCase1.md)|  | [optional] 

### Return type

[**AgentTestCaseResponse1**](AgentTestCaseResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bulk_create_agent_dataset_test_cases**
> BulkCreateAgentTestCasesResponse post_bulk_create_agent_dataset_test_cases(project_id, dataset_id, body=body)

Bulk Create Agent Test Cases

 Add multiple test cases to an agent dataset in a single request. Use for batch imports from production traces.  Maximum 100 test cases per request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.BulkCreateAgentTestCasesRequest() # BulkCreateAgentTestCasesRequest |  (optional)

try:
    # Bulk Create Agent Test Cases
    api_response = api_instance.post_bulk_create_agent_dataset_test_cases(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->post_bulk_create_agent_dataset_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**BulkCreateAgentTestCasesRequest**](BulkCreateAgentTestCasesRequest.md)|  | [optional] 

### Return type

[**BulkCreateAgentTestCasesResponse**](BulkCreateAgentTestCasesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_agent_dataset**
> AgentDatasetResponse1 post_create_agent_dataset(project_id, body=body)

Create Agent-Level Dataset

 Create a new dataset for agent-level testing. Use to organize test cases for evaluating full agent workflows.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreateAgentDatasetRequest() # CreateAgentDatasetRequest |  (optional)

try:
    # Create Agent-Level Dataset
    api_response = api_instance.post_create_agent_dataset(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentDatasetsApi->post_create_agent_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**CreateAgentDatasetRequest**](CreateAgentDatasetRequest.md)|  | [optional] 

### Return type

[**AgentDatasetResponse1**](AgentDatasetResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

