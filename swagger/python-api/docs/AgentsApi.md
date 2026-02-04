# swagger_client.AgentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_agent**](AgentsApi.md#delete_delete_agent) | **DELETE** /api/v2/projects/{project_id}/agents/{agent_id} | Delete Agent
[**get_get_agent**](AgentsApi.md#get_get_agent) | **GET** /api/v2/projects/{project_id}/agents/{agent_id} | Get Agent
[**get_get_agents**](AgentsApi.md#get_get_agents) | **GET** /api/v2/projects/{project_id}/agents | List Agents
[**patch_update_agent**](AgentsApi.md#patch_update_agent) | **PATCH** /api/v2/projects/{project_id}/agents/{agent_id} | Update Agent
[**post_create_agent**](AgentsApi.md#post_create_agent) | **POST** /api/v2/projects/{project_id}/agents | Create Agent

# **delete_delete_agent**
> object delete_delete_agent(project_id, agent_id)

Delete Agent

 Delete an agent from your project. This operation cannot be undone.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
agent_id = NULL # object | 

try:
    # Delete Agent
    api_response = api_instance.delete_delete_agent(project_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->delete_delete_agent: %s\n" % e)
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

# **get_get_agent**
> AgentInfo1 get_get_agent(project_id, agent_id)

Get Agent

 Retrieve details for a specific agent by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
agent_id = NULL # object | 

try:
    # Get Agent
    api_response = api_instance.get_get_agent(project_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->get_get_agent: %s\n" % e)
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

List Agents

 Retrieve a paginated list of agents for your project. Optionally filter by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)
name = NULL # object |  (optional)

try:
    # List Agents
    api_response = api_instance.get_get_agents(project_id, page=page, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->get_get_agents: %s\n" % e)
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

# **patch_update_agent**
> AgentInfo1 patch_update_agent(project_id, agent_id, body=body)

Update Agent

 Update the name of an existing agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
agent_id = NULL # object | 
body = swagger_client.UpdateAgentRequest() # UpdateAgentRequest |  (optional)

try:
    # Update Agent
    api_response = api_instance.patch_update_agent(project_id, agent_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->patch_update_agent: %s\n" % e)
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

# **post_create_agent**
> AgentInfo1 post_create_agent(project_id, body=body)

Create Agent

 Create a new agent in your project. Agents are used to organize and group related sessions and traces.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AgentsApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.CreateAgentRequest() # CreateAgentRequest |  (optional)

try:
    # Create Agent
    api_response = api_instance.post_create_agent(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->post_create_agent: %s\n" % e)
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

