# swagger_client.PromptDatasetsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bulk_delete_prompt_dataset_test_cases**](PromptDatasetsApi.md#delete_bulk_delete_prompt_dataset_test_cases) | **DELETE** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id}/test-cases/bulk | Bulk Delete Prompt Test Cases
[**delete_delete_prompt_dataset**](PromptDatasetsApi.md#delete_delete_prompt_dataset) | **DELETE** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id} | Delete Prompt Dataset
[**delete_delete_prompt_dataset_test_case**](PromptDatasetsApi.md#delete_delete_prompt_dataset_test_case) | **DELETE** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id}/test-cases/{test_case_id} | Delete Prompt Test Case
[**get_get_by_id**](PromptDatasetsApi.md#get_get_by_id) | **GET** /api/v2/projects/{project_id}/datasets/id/{dataset_id} | Get Prompt Dataset
[**get_get_by_name**](PromptDatasetsApi.md#get_get_by_name) | **GET** /api/v2/projects/{project_id}/datasets/name/{dataset_name} | Get Prompt Dataset by Name
[**get_get_prompt_dataset**](PromptDatasetsApi.md#get_get_prompt_dataset) | **GET** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id} | Get Prompt Dataset
[**get_get_prompt_dataset_test_case**](PromptDatasetsApi.md#get_get_prompt_dataset_test_case) | **GET** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id}/test-cases/{test_case_id} | Get Prompt Test Case
[**get_get_prompt_dataset_test_cases**](PromptDatasetsApi.md#get_get_prompt_dataset_test_cases) | **GET** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id}/test-cases | List Prompt Test Cases
[**get_get_prompt_datasets**](PromptDatasetsApi.md#get_get_prompt_datasets) | **GET** /api/v2/projects/{project_id}/prompt-datasets | List Prompt Datasets
[**get_get_test_cases_by_id**](PromptDatasetsApi.md#get_get_test_cases_by_id) | **GET** /api/v2/projects/{project_id}/datasets/id/{dataset_id}/test-cases | List Prompt Test Cases
[**get_get_test_cases_by_name**](PromptDatasetsApi.md#get_get_test_cases_by_name) | **GET** /api/v2/projects/{project_id}/datasets/name/{dataset_name}/test-cases | List Prompt Test Cases by Dataset Name
[**patch_update_prompt_dataset**](PromptDatasetsApi.md#patch_update_prompt_dataset) | **PATCH** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id} | Update Prompt Dataset
[**patch_update_prompt_dataset_test_case**](PromptDatasetsApi.md#patch_update_prompt_dataset_test_case) | **PATCH** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id}/test-cases/{test_case_id} | Update Prompt Test Case
[**post_bulk_create_prompt_dataset_test_cases**](PromptDatasetsApi.md#post_bulk_create_prompt_dataset_test_cases) | **POST** /api/v2/projects/{project_id}/prompt-datasets/{dataset_id}/test-cases/bulk | Bulk Create Prompt Test Cases
[**post_create_prompt_dataset**](PromptDatasetsApi.md#post_create_prompt_dataset) | **POST** /api/v2/projects/{project_id}/prompt-datasets | Create Prompt-Level Dataset
[**post_upload_test_cases**](PromptDatasetsApi.md#post_upload_test_cases) | **POST** /api/v2/projects/{project_id}/datasets/id/{dataset_id}/test-cases | Upload Prompt Test Cases

# **delete_bulk_delete_prompt_dataset_test_cases**
> object delete_bulk_delete_prompt_dataset_test_cases(project_id, dataset_id, body=body)

Bulk Delete Prompt Test Cases

 Remove multiple test cases in a single request. Use for batch cleanup operations.  Maximum 100 test cases per request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.BulkDeletePromptTestCasesRequest() # BulkDeletePromptTestCasesRequest |  (optional)

try:
    # Bulk Delete Prompt Test Cases
    api_response = api_instance.delete_bulk_delete_prompt_dataset_test_cases(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->delete_bulk_delete_prompt_dataset_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**BulkDeletePromptTestCasesRequest**](BulkDeletePromptTestCasesRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_prompt_dataset**
> object delete_delete_prompt_dataset(project_id, dataset_id)

Delete Prompt Dataset

 Archive a prompt dataset and its test cases. Use when retiring datasets no longer needed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 

try:
    # Delete Prompt Dataset
    api_response = api_instance.delete_delete_prompt_dataset(project_id, dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->delete_delete_prompt_dataset: %s\n" % e)
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

# **delete_delete_prompt_dataset_test_case**
> object delete_delete_prompt_dataset_test_case(project_id, dataset_id, test_case_id)

Delete Prompt Test Case

 Remove a test case from a dataset. Use to clean up invalid or outdated test cases.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
test_case_id = NULL # object | 

try:
    # Delete Prompt Test Case
    api_response = api_instance.delete_delete_prompt_dataset_test_case(project_id, dataset_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->delete_delete_prompt_dataset_test_case: %s\n" % e)
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

# **get_get_by_id**
> TestListInfo get_get_by_id(project_id, dataset_id)

Get Prompt Dataset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 

try:
    # Get Prompt Dataset
    api_response = api_instance.get_get_by_id(project_id, dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 

### Return type

[**TestListInfo**](TestListInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_by_name**
> TestListInfo get_get_by_name(project_id, dataset_name)

Get Prompt Dataset by Name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_name = NULL # object | 

try:
    # Get Prompt Dataset by Name
    api_response = api_instance.get_get_by_name(project_id, dataset_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_name** | [**object**](.md)|  | 

### Return type

[**TestListInfo**](TestListInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_prompt_dataset**
> PromptDatasetResponse1 get_get_prompt_dataset(project_id, dataset_id)

Get Prompt Dataset

 Retrieve a prompt dataset's metadata by ID. Use to check dataset configuration or input schema.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 

try:
    # Get Prompt Dataset
    api_response = api_instance.get_get_prompt_dataset(project_id, dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_prompt_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 

### Return type

[**PromptDatasetResponse1**](PromptDatasetResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_prompt_dataset_test_case**
> PromptTestCaseResponse1 get_get_prompt_dataset_test_case(project_id, dataset_id, test_case_id)

Get Prompt Test Case

 Retrieve a specific test case (dataset row) by ID. Use to inspect test case details or debug test run results.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
test_case_id = NULL # object | 

try:
    # Get Prompt Test Case
    api_response = api_instance.get_get_prompt_dataset_test_case(project_id, dataset_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_prompt_dataset_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **test_case_id** | [**object**](.md)|  | 

### Return type

[**PromptTestCaseResponse1**](PromptTestCaseResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_prompt_dataset_test_cases**
> PromptTestCasesListResponse get_get_prompt_dataset_test_cases(project_id, dataset_id, page=page, page_size=page_size)

List Prompt Test Cases

 Retrieve all row-level test cases in a prompt dataset. Use to review dataset contents or export for analysis.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Prompt Test Cases
    api_response = api_instance.get_get_prompt_dataset_test_cases(project_id, dataset_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_prompt_dataset_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**PromptTestCasesListResponse**](PromptTestCasesListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_prompt_datasets**
> PromptDatasetsListResponse get_get_prompt_datasets(project_id, page=page, page_size=page_size, id=id, name=name)

List Prompt Datasets

 Retrieve all prompt-level datasets in a project. Use to discover available datasets for test runs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
id = NULL # object |  (optional)
name = NULL # object |  (optional)

try:
    # List Prompt Datasets
    api_response = api_instance.get_get_prompt_datasets(project_id, page=page, page_size=page_size, id=id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_prompt_datasets: %s\n" % e)
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

[**PromptDatasetsListResponse**](PromptDatasetsListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_test_cases_by_id**
> object get_get_test_cases_by_id(project_id, dataset_id, page=page, page_size=page_size)

List Prompt Test Cases

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
page = null # object |  (optional) (default to null)
page_size = null # object |  (optional) (default to null)

try:
    # List Prompt Test Cases
    api_response = api_instance.get_get_test_cases_by_id(project_id, dataset_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_test_cases_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to null]
 **page_size** | [**object**](.md)|  | [optional] [default to null]

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_test_cases_by_name**
> object get_get_test_cases_by_name(project_id, dataset_name, page=page, page_size=page_size)

List Prompt Test Cases by Dataset Name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_name = NULL # object | 
page = NULL # object |  (optional)
page_size = NULL # object |  (optional)

try:
    # List Prompt Test Cases by Dataset Name
    api_response = api_instance.get_get_test_cases_by_name(project_id, dataset_name, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->get_get_test_cases_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_name** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] 
 **page_size** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_prompt_dataset**
> PromptDatasetResponse1 patch_update_prompt_dataset(project_id, dataset_id, body=body)

Update Prompt Dataset

 Modify a prompt dataset's name, description, or input schema. Use to evolve datasets as prompt requirements change.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.UpdatePromptDatasetRequest() # UpdatePromptDatasetRequest |  (optional)

try:
    # Update Prompt Dataset
    api_response = api_instance.patch_update_prompt_dataset(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->patch_update_prompt_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**UpdatePromptDatasetRequest**](UpdatePromptDatasetRequest.md)|  | [optional] 

### Return type

[**PromptDatasetResponse1**](PromptDatasetResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_prompt_dataset_test_case**
> PromptTestCaseResponse1 patch_update_prompt_dataset_test_case(project_id, dataset_id, test_case_id, body=body)

Update Prompt Test Case

 Modify an existing test case's inputs, output, or metadata. Use to change ground truth output values or correct errors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
test_case_id = NULL # object | 
body = swagger_client.UpdatePromptTestCaseRequest() # UpdatePromptTestCaseRequest |  (optional)

try:
    # Update Prompt Test Case
    api_response = api_instance.patch_update_prompt_dataset_test_case(project_id, dataset_id, test_case_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->patch_update_prompt_dataset_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **test_case_id** | [**object**](.md)|  | 
 **body** | [**UpdatePromptTestCaseRequest**](UpdatePromptTestCaseRequest.md)|  | [optional] 

### Return type

[**PromptTestCaseResponse1**](PromptTestCaseResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bulk_create_prompt_dataset_test_cases**
> CreatePromptTestCasesResponse post_bulk_create_prompt_dataset_test_cases(project_id, dataset_id, body=body)

Bulk Create Prompt Test Cases

 Add multiple test cases to a dataset in a single request. Use for batch imports, e.g. from CSV or production logs.  Maximum 100 test cases per request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.CreatePromptTestCasesRequest() # CreatePromptTestCasesRequest |  (optional)

try:
    # Bulk Create Prompt Test Cases
    api_response = api_instance.post_bulk_create_prompt_dataset_test_cases(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->post_bulk_create_prompt_dataset_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**CreatePromptTestCasesRequest**](CreatePromptTestCasesRequest.md)|  | [optional] 

### Return type

[**CreatePromptTestCasesResponse**](CreatePromptTestCasesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_prompt_dataset**
> PromptDatasetResponse1 post_create_prompt_dataset(project_id, body=body)

Create Prompt-Level Dataset

 Create a new dataset for prompt-level testing. Use to organize test cases for evaluating individual prompts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreatePromptDatasetRequest() # CreatePromptDatasetRequest |  (optional)

try:
    # Create Prompt-Level Dataset
    api_response = api_instance.post_create_prompt_dataset(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->post_create_prompt_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**CreatePromptDatasetRequest**](CreatePromptDatasetRequest.md)|  | [optional] 

### Return type

[**PromptDatasetResponse1**](PromptDatasetResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_upload_test_cases**
> SimpleResponseWithMessage post_upload_test_cases(project_id, dataset_id, body=body)

Upload Prompt Test Cases

 Add test cases to a dataset using the legacy upload format. Use for bulk imports with input/output pairs.  Maximum 100 examples per request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptDatasetsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
dataset_id = NULL # object | 
body = swagger_client.TestCasesUploadRequest() # TestCasesUploadRequest |  (optional)

try:
    # Upload Prompt Test Cases
    api_response = api_instance.post_upload_test_cases(project_id, dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptDatasetsApi->post_upload_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **dataset_id** | [**object**](.md)|  | 
 **body** | [**TestCasesUploadRequest**](TestCasesUploadRequest.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

