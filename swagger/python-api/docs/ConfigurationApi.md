# swagger_client.ConfigurationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_environment**](ConfigurationApi.md#delete_delete_environment) | **DELETE** /api/v2/environments/{environment_id} | Delete Environment
[**delete_delete_user**](ConfigurationApi.md#delete_delete_user) | **DELETE** /api/v2/users/{user_id} | Delete User
[**delete_remove_member**](ConfigurationApi.md#delete_remove_member) | **DELETE** /api/v2/projects/{project_id}/members/{user_id} | Remove Project Member
[**get_get_project**](ConfigurationApi.md#get_get_project) | **GET** /api/v2/projects/{project_id} | Get Project
[**get_get_projects**](ConfigurationApi.md#get_get_projects) | **GET** /api/v2/projects/all | List Projects
[**get_get_user**](ConfigurationApi.md#get_get_user) | **GET** /api/v2/users/{user_id} | Get User
[**get_list_environments**](ConfigurationApi.md#get_list_environments) | **GET** /api/v2/environments | List Environments
[**get_list_members**](ConfigurationApi.md#get_list_members) | **GET** /api/v2/projects/{project_id}/members | List Project Members
[**get_list_users**](ConfigurationApi.md#get_list_users) | **GET** /api/v2/users | List Users
[**patch_update_environment**](ConfigurationApi.md#patch_update_environment) | **PATCH** /api/v2/environments/{environment_id} | Update Environment
[**patch_update_member**](ConfigurationApi.md#patch_update_member) | **PATCH** /api/v2/projects/{project_id}/members/{user_id} | Update Project Member
[**patch_update_user**](ConfigurationApi.md#patch_update_user) | **PATCH** /api/v2/users/{user_id} | Update User
[**post_add_member**](ConfigurationApi.md#post_add_member) | **POST** /api/v2/projects/{project_id}/members | Add Project Member
[**post_create_environment**](ConfigurationApi.md#post_create_environment) | **POST** /api/v2/environments | Create Environment
[**post_create_project**](ConfigurationApi.md#post_create_project) | **POST** /api/v2/projects | Create Project
[**post_create_user**](ConfigurationApi.md#post_create_user) | **POST** /api/v2/users | Create User
[**put_update_project**](ConfigurationApi.md#put_update_project) | **PUT** /api/v2/projects/{project_id} | Update Project

# **delete_delete_environment**
> object delete_delete_environment(environment_id)

Delete Environment

 Remove an environment. Use when retiring deployment targets no longer in use.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
environment_id = NULL # object | 

try:
    # Delete Environment
    api_response = api_instance.delete_delete_environment(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_delete_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delete_user**
> object delete_delete_user(user_id)

Delete User

 Remove a user from your workspace. Requires account admin role. Use for offboarding or access revocation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
user_id = NULL # object | 

try:
    # Delete User
    api_response = api_instance.delete_delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remove_member**
> object delete_remove_member(project_id, user_id)

Remove Project Member

 Revoke a user's access to the project. Requires project admin role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
user_id = NULL # object | 

try:
    # Remove Project Member
    api_response = api_instance.delete_remove_member(project_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **user_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_project**
> ProjectDetail get_get_project(project_id)

Get Project

 Retrieve the current project's details. Use to check project settings like spend limits or data retention.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 

try:
    # Get Project
    api_response = api_instance.get_get_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_projects**
> Projects get_get_projects()

List Projects

 Retrieve all projects accessible to the current user. Use to discover available projects or build project selection UIs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # List Projects
    api_response = api_instance.get_get_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Projects**](Projects.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_user**
> UserResponse1 get_get_user(user_id)

Get User

 Retrieve a user's details by ID. Requires account admin role. Use to check user settings or role assignments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
user_id = NULL # object | 

try:
    # Get User
    api_response = api_instance.get_get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

[**UserResponse1**](UserResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_environments**
> EnvironmentsListResponse get_list_environments(page=page, page_size=page_size)

List Environments

 Retrieve all deployment environments in your workspace. Use to discover available environments for prompt deployment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Environments
    api_response = api_instance.get_list_environments(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_list_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**EnvironmentsListResponse**](EnvironmentsListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_members**
> MembersList get_list_members(project_id, page=page, page_size=page_size)

List Project Members

 Retrieve all users with access to the project and their roles. Use for access management or auditing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Project Members
    api_response = api_instance.get_list_members(project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**MembersList**](MembersList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_users**
> UsersListResponse get_list_users(include_deleted=include_deleted)

List Users

 Retrieve all users in your workspace. Requires account admin role. Use for user management or access auditing. Set include_deleted=true to include soft-deleted users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
include_deleted = null # object |  (optional) (default to null)

try:
    # List Users
    api_response = api_instance.get_list_users(include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | [**object**](.md)|  | [optional] [default to null]

### Return type

[**UsersListResponse**](UsersListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_environment**
> EnvironmentInfo1 patch_update_environment(environment_id, body=body)

Update Environment

 Rename an existing environment. Use when consolidating or reorganizing deployment targets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
environment_id = NULL # object | 
body = swagger_client.UpdateEnvironmentRequest() # UpdateEnvironmentRequest |  (optional)

try:
    # Update Environment
    api_response = api_instance.patch_update_environment(environment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->patch_update_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**object**](.md)|  | 
 **body** | [**UpdateEnvironmentRequest**](UpdateEnvironmentRequest.md)|  | [optional] 

### Return type

[**EnvironmentInfo1**](EnvironmentInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_member**
> object patch_update_member(project_id, user_id, body=body)

Update Project Member

 Change a user's role in the project. Requires project admin role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
user_id = NULL # object | 
body = swagger_client.UpdateMemberRequest() # UpdateMemberRequest |  (optional)

try:
    # Update Project Member
    api_response = api_instance.patch_update_member(project_id, user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->patch_update_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **user_id** | [**object**](.md)|  | 
 **body** | [**UpdateMemberRequest**](UpdateMemberRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_user**
> UserResponse1 patch_update_user(user_id, body=body)

Update User

 Modify a user's name, role, or profile settings. Requires account admin role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
user_id = NULL # object | 
body = swagger_client.UpdateUserRequest() # UpdateUserRequest |  (optional)

try:
    # Update User
    api_response = api_instance.patch_update_user(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->patch_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **body** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional] 

### Return type

[**UserResponse1**](UserResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_add_member**
> object post_add_member(project_id, body=body)

Add Project Member

 Grant a user access to the project with a specified role. Requires project admin role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.AddMemberRequest() # AddMemberRequest |  (optional)

try:
    # Add Project Member
    api_response = api_instance.post_add_member(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->post_add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**AddMemberRequest**](AddMemberRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_environment**
> EnvironmentInfo1 post_create_environment(body=body)

Create Environment

 Create a new deployment environment. Use to add environments beyond Freeplay defaults, like staging or feature branches.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateEnvironmentRequest() # CreateEnvironmentRequest |  (optional)

try:
    # Create Environment
    api_response = api_instance.post_create_environment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->post_create_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEnvironmentRequest**](CreateEnvironmentRequest.md)|  | [optional] 

### Return type

[**EnvironmentInfo1**](EnvironmentInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_project**
> ProjectDetail post_create_project(body=body)

Create Project

 Create a new project in your workspace. Use to organize prompts, datasets, and observability data by team or application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProjectRequest() # CreateProjectRequest |  (optional)

try:
    # Create Project
    api_response = api_instance.post_create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->post_create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | [optional] 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_user**
> UserResponse1 post_create_user(body=body)

Create User

 Create a new user in your workspace. Requires account admin role. Use for automated user provisioning or SCIM integrations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateUserRequest() # CreateUserRequest |  (optional)

try:
    # Create User
    api_response = api_instance.post_create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->post_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequest**](CreateUserRequest.md)|  | [optional] 

### Return type

[**UserResponse1**](UserResponse1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_project**
> ProjectDetail put_update_project(project_id, body=body)

Update Project

 Modify project settings like name, visibility, or resource limits. Requires project admin role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.UpdateProjectRequest() # UpdateProjectRequest |  (optional)

try:
    # Update Project
    api_response = api_instance.put_update_project(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | [optional] 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

