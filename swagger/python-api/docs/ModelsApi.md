# swagger_client.ModelsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_model**](ModelsApi.md#delete_delete_model) | **DELETE** /api/v2/models/{model_id} | Delete Model
[**get_get_model**](ModelsApi.md#get_get_model) | **GET** /api/v2/models/{model_id} | Get Model
[**get_list_models**](ModelsApi.md#get_list_models) | **GET** /api/v2/models | List Models
[**post_replicate_model**](ModelsApi.md#post_replicate_model) | **POST** /api/v2/models | Create Model
[**put_update_model**](ModelsApi.md#put_update_model) | **PUT** /api/v2/models/{model_id} | Update Model

# **delete_delete_model**
> object delete_delete_model(model_id)

Delete Model

 Delete a custom model configuration from the account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = NULL # object | 

try:
    # Delete Model
    api_response = api_instance.delete_delete_model(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->delete_delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_model**
> ModelReplicationInfo1 get_get_model(model_id)

Get Model

 Retrieve details for a specific custom model by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = NULL # object | 

try:
    # Get Model
    api_response = api_instance.get_get_model(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | [**object**](.md)|  | 

### Return type

[**ModelReplicationInfo1**](ModelReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_models**
> ModelListResponse get_list_models(page=page, page_size=page_size)

List Models

 Retrieve a paginated list of custom models configured for the account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Models
    api_response = api_instance.get_list_models(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_list_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**ModelListResponse**](ModelListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_replicate_model**
> ModelReplicationInfo1 post_replicate_model(body=body)

Create Model

 Create or upsert a custom model configuration for the account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReplicateModelRequest() # ReplicateModelRequest |  (optional)

try:
    # Create Model
    api_response = api_instance.post_replicate_model(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->post_replicate_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicateModelRequest**](ReplicateModelRequest.md)|  | [optional] 

### Return type

[**ModelReplicationInfo1**](ModelReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_model**
> ModelReplicationInfo1 put_update_model(model_id, body=body)

Update Model

 Update an existing custom model configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = NULL # object | 
body = swagger_client.UpdateModelRequest() # UpdateModelRequest |  (optional)

try:
    # Update Model
    api_response = api_instance.put_update_model(model_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->put_update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | [**object**](.md)|  | 
 **body** | [**UpdateModelRequest**](UpdateModelRequest.md)|  | [optional] 

### Return type

[**ModelReplicationInfo1**](ModelReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

