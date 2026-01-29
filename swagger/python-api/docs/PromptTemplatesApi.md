# swagger_client.PromptTemplatesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_prompt_template**](PromptTemplatesApi.md#delete_delete_prompt_template) | **DELETE** /api/v2/projects/{project_id}/prompt-templates/id/{template_id} | Delete prompt template
[**delete_delete_template_version**](PromptTemplatesApi.md#delete_delete_template_version) | **DELETE** /api/v2/projects/{project_id}/prompt-templates/id/{template_id}/versions/{version_id} | Delete prompt template version
[**get_get_all_by_environment**](PromptTemplatesApi.md#get_get_all_by_environment) | **GET** /api/v2/projects/{project_id}/prompt-templates/all/{environment} | Get all prompt templates by environment
[**get_get_by_name_and_environment**](PromptTemplatesApi.md#get_get_by_name_and_environment) | **GET** /api/v2/projects/{project_id}/prompt-templates/name/{name} | Get prompt template by name and environment
[**get_get_by_template_version_id**](PromptTemplatesApi.md#get_get_by_template_version_id) | **GET** /api/v2/projects/{project_id}/prompt-templates/id/{template_id}/versions/{version_id} | Get prompt template version by ID
[**get_get_prompt_template**](PromptTemplatesApi.md#get_get_prompt_template) | **GET** /api/v2/projects/{project_id}/prompt-templates/id/{template_id} | Get prompt template
[**get_list_prompt_template_versions**](PromptTemplatesApi.md#get_list_prompt_template_versions) | **GET** /api/v2/projects/{project_id}/prompt-templates/id/{template_id}/versions | List prompt template versions
[**get_list_prompt_templates**](PromptTemplatesApi.md#get_list_prompt_templates) | **GET** /api/v2/projects/{project_id}/prompt-templates | List prompt templates
[**patch_update_prompt_template**](PromptTemplatesApi.md#patch_update_prompt_template) | **PATCH** /api/v2/projects/{project_id}/prompt-templates/id/{template_id} | Update prompt template
[**post_create_prompt_template**](PromptTemplatesApi.md#post_create_prompt_template) | **POST** /api/v2/projects/{project_id}/prompt-templates | Create prompt template
[**post_create_template_version_by_id**](PromptTemplatesApi.md#post_create_template_version_by_id) | **POST** /api/v2/projects/{project_id}/prompt-templates/id/{template_id}/versions | Create prompt template version by ID
[**post_create_template_version_by_name**](PromptTemplatesApi.md#post_create_template_version_by_name) | **POST** /api/v2/projects/{project_id}/prompt-templates/name/{template_name}/versions | Create prompt template version by name
[**post_get_bound_by_name_and_environment**](PromptTemplatesApi.md#post_get_bound_by_name_and_environment) | **POST** /api/v2/projects/{project_id}/prompt-templates/name/{name} | Get bound prompt template by name and environment
[**post_get_bound_by_template_version_id**](PromptTemplatesApi.md#post_get_bound_by_template_version_id) | **POST** /api/v2/projects/{project_id}/prompt-templates/id/{template_id}/versions/{version_id} | Get bound prompt template version by ID
[**post_update_template_version_environments**](PromptTemplatesApi.md#post_update_template_version_environments) | **POST** /api/v2/projects/{project_id}/prompt-templates/id/{template_id}/versions/{version_id}/environments | Update environment for prompt template version

# **delete_delete_prompt_template**
> object delete_delete_prompt_template(project_id, template_id)

Delete prompt template

 Archive a prompt template and all its versions. Use when retiring templates that are no longer needed. This is a soft delete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 

try:
    # Delete prompt template
    api_response = api_instance.delete_delete_prompt_template(project_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->delete_delete_prompt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_template_version**
> object delete_delete_template_version(project_id, template_id, version_id)

Delete prompt template version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
version_id = NULL # object | 

try:
    # Delete prompt template version
    api_response = api_instance.delete_delete_template_version(project_id, template_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->delete_delete_template_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_all_by_environment**
> PromptTemplatesByEnvironmentResponse get_get_all_by_environment(project_id, environment)

Get all prompt templates by environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
environment = NULL # object | 

try:
    # Get all prompt templates by environment
    api_response = api_instance.get_get_all_by_environment(project_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->get_get_all_by_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **environment** | [**object**](.md)|  | 

### Return type

[**PromptTemplatesByEnvironmentResponse**](PromptTemplatesByEnvironmentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_by_name_and_environment**
> PlainPromptTemplate1 get_get_by_name_and_environment(project_id, name, environment=environment, format=format, flavor_name=flavor_name)

Get prompt template by name and environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
name = NULL # object | 
environment = NULL # object |  (optional)
format = NULL # object |  (optional)
flavor_name = NULL # object |  (optional)

try:
    # Get prompt template by name and environment
    api_response = api_instance.get_get_by_name_and_environment(project_id, name, environment=environment, format=format, flavor_name=flavor_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->get_get_by_name_and_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **name** | [**object**](.md)|  | 
 **environment** | [**object**](.md)|  | [optional] 
 **format** | [**object**](.md)|  | [optional] 
 **flavor_name** | [**object**](.md)|  | [optional] 

### Return type

[**PlainPromptTemplate1**](PlainPromptTemplate1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_by_template_version_id**
> PlainPromptTemplate1 get_get_by_template_version_id(project_id, template_id, version_id)

Get prompt template version by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
version_id = NULL # object | 

try:
    # Get prompt template version by ID
    api_response = api_instance.get_get_by_template_version_id(project_id, template_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->get_get_by_template_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 

### Return type

[**PlainPromptTemplate1**](PlainPromptTemplate1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_prompt_template**
> PromptTemplateInfo1 get_get_prompt_template(project_id, template_id)

Get prompt template

 Retrieve a prompt template's metadata by ID. Use to check if a template exists or get its latest version ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 

try:
    # Get prompt template
    api_response = api_instance.get_get_prompt_template(project_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->get_get_prompt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 

### Return type

[**PromptTemplateInfo1**](PromptTemplateInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_prompt_template_versions**
> PromptTemplateVersionListResponse get_list_prompt_template_versions(project_id, template_id, page=page, page_size=page_size, from_version=from_version)

List prompt template versions

 Retrieve all versions of a prompt template. Use to view version history or compare changes over time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
from_version = null # object |  (optional) (default to null)

try:
    # List prompt template versions
    api_response = api_instance.get_list_prompt_template_versions(project_id, template_id, page=page, page_size=page_size, from_version=from_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->get_list_prompt_template_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]
 **from_version** | [**object**](.md)|  | [optional] [default to null]

### Return type

[**PromptTemplateVersionListResponse**](PromptTemplateVersionListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_prompt_templates**
> PromptTemplateListResponse get_list_prompt_templates(project_id, page=page, page_size=page_size)

List prompt templates

 Retrieve all prompt templates in a project. Use to discover available templates or build template management UIs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List prompt templates
    api_response = api_instance.get_list_prompt_templates(project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->get_list_prompt_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**PromptTemplateListResponse**](PromptTemplateListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_prompt_template**
> object patch_update_prompt_template(project_id, template_id, body=body)

Update prompt template

 Rename a prompt template. Use when refactoring template names across your codebase.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
body = swagger_client.UpdatePromptTemplateRequest() # UpdatePromptTemplateRequest |  (optional)

try:
    # Update prompt template
    api_response = api_instance.patch_update_prompt_template(project_id, template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->patch_update_prompt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **body** | [**UpdatePromptTemplateRequest**](UpdatePromptTemplateRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_prompt_template**
> CreatePromptTemplateResponse post_create_prompt_template(project_id, body=body)

Create prompt template

 Create a new prompt template without any versions. Use when you need to reserve a template name before adding versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreatePromptTemplateRequest() # CreatePromptTemplateRequest |  (optional)

try:
    # Create prompt template
    api_response = api_instance.post_create_prompt_template(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->post_create_prompt_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**CreatePromptTemplateRequest**](CreatePromptTemplateRequest.md)|  | [optional] 

### Return type

[**CreatePromptTemplateResponse**](CreatePromptTemplateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_template_version_by_id**
> PlainPromptTemplate1 post_create_template_version_by_id(project_id, template_id, body=body)

Create prompt template version by ID

 Create a new version of an existing prompt template. Freeplay assigns a random ID. Use when you have the template ID from a previous API call.  **Version Creation Semantics:**  A new version is created only if there is no existing version with identical: - Content (prompt messages) - Model - LLM parameters - Version name (if provided) - Version description - Tool schema - Output schema  If an identical version exists in any of the target environments, that version is reused and its environments are updated to match the requested environments. This ensures you never create duplicate versions with the same configuration.  **Environment Deployment:**  - When creating a new version, it will be deployed to the specified environments (or \"latest\" if none specified) - When reuploading an existing prompt template with a new environment, the environments on that prompt template version will be updated  These checks are performed so that you can safely upload prompt templates without worrying that you will be creating duplicate versions. This is especially useful in development workflows where your prompts are stored in code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
body = swagger_client.CreateTemplateVersionRequest() # CreateTemplateVersionRequest |  (optional)

try:
    # Create prompt template version by ID
    api_response = api_instance.post_create_template_version_by_id(project_id, template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->post_create_template_version_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **body** | [**CreateTemplateVersionRequest**](CreateTemplateVersionRequest.md)|  | [optional] 

### Return type

[**PlainPromptTemplate1**](PlainPromptTemplate1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_template_version_by_name**
> PlainPromptTemplate1 post_create_template_version_by_name(project_id, template_name, body=body, create_template_if_not_exists=create_template_if_not_exists)

Create prompt template version by name

 Create a new version of a prompt template, referenced by a string or name you define. [See SDK method.](https://docs.freeplay.ai/freeplay-sdk/prompts)  Set `create_template_if_not_exists=true` to auto-create the template if it doesn't exist.  **Version Creation Semantics:**  A new version is created only if there is no existing version with identical: - Content (prompt messages) - Model - LLM parameters - Version name (if provided) - Version description - Tool schema - Output schema  If an identical version exists in any of the target environments, that version is reused and its environments are updated to match the requested environments. This ensures you never create duplicate versions with the same configuration.  **Environment Deployment:**  - When creating a new version, it will be deployed to the specified environments (or \"latest\" if none specified) - When reuploading an existing prompt template with a new environment, the environments on that prompt template version will be updated  These checks are performed so that you can safely upload prompt templates without worrying that you will be creating duplicate versions. This is especially useful in development workflows where your prompts are stored in code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_name = NULL # object | 
body = swagger_client.CreateTemplateVersionRequest1() # CreateTemplateVersionRequest1 |  (optional)
create_template_if_not_exists = null # object |  (optional) (default to null)

try:
    # Create prompt template version by name
    api_response = api_instance.post_create_template_version_by_name(project_id, template_name, body=body, create_template_if_not_exists=create_template_if_not_exists)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->post_create_template_version_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_name** | [**object**](.md)|  | 
 **body** | [**CreateTemplateVersionRequest1**](CreateTemplateVersionRequest1.md)|  | [optional] 
 **create_template_if_not_exists** | [**object**](.md)|  | [optional] [default to null]

### Return type

[**PlainPromptTemplate1**](PlainPromptTemplate1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_bound_by_name_and_environment**
> PromptTemplateVersion post_get_bound_by_name_and_environment(project_id, name, body=body, environment=environment, format=format, flavor_name=flavor_name)

Get bound prompt template by name and environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
name = NULL # object | 
body = NULL # object |  (optional)
environment = NULL # object |  (optional)
format = NULL # object |  (optional)
flavor_name = NULL # object |  (optional)

try:
    # Get bound prompt template by name and environment
    api_response = api_instance.post_get_bound_by_name_and_environment(project_id, name, body=body, environment=environment, format=format, flavor_name=flavor_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->post_get_bound_by_name_and_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **name** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] 
 **format** | [**object**](.md)|  | [optional] 
 **flavor_name** | [**object**](.md)|  | [optional] 

### Return type

[**PromptTemplateVersion**](PromptTemplateVersion.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_bound_by_template_version_id**
> PromptTemplateVersion post_get_bound_by_template_version_id(project_id, template_id, version_id, body=body, environment=environment, format=format, flavor_name=flavor_name)

Get bound prompt template version by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
version_id = NULL # object | 
body = NULL # object |  (optional)
environment = NULL # object |  (optional)
format = null # object |  (optional) (default to null)
flavor_name = null # object |  (optional) (default to null)

try:
    # Get bound prompt template version by ID
    api_response = api_instance.post_get_bound_by_template_version_id(project_id, template_id, version_id, body=body, environment=environment, format=format, flavor_name=flavor_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->post_get_bound_by_template_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **environment** | [**object**](.md)|  | [optional] 
 **format** | [**object**](.md)|  | [optional] [default to null]
 **flavor_name** | [**object**](.md)|  | [optional] [default to null]

### Return type

[**PromptTemplateVersion**](PromptTemplateVersion.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_update_template_version_environments**
> object post_update_template_version_environments(project_id, template_id, version_id, body=body)

Update environment for prompt template version

 Deploy a prompt version to one or more environments. Use to promote versions through dev, staging, and production.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PromptTemplatesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
template_id = NULL # object | 
version_id = NULL # object | 
body = swagger_client.UpdateTemplateVersionEnvironmentsRequest() # UpdateTemplateVersionEnvironmentsRequest |  (optional)

try:
    # Update environment for prompt template version
    api_response = api_instance.post_update_template_version_environments(project_id, template_id, version_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromptTemplatesApi->post_update_template_version_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **template_id** | [**object**](.md)|  | 
 **version_id** | [**object**](.md)|  | 
 **body** | [**UpdateTemplateVersionEnvironmentsRequest**](UpdateTemplateVersionEnvironmentsRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

