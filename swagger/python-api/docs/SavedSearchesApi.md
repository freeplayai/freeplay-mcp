# swagger_client.SavedSearchesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_filter**](SavedSearchesApi.md#delete_delete_filter) | **DELETE** /api/v2/projects/{project_id}/session-filters/{filter_id} | Delete Saved Search
[**get_get_filter**](SavedSearchesApi.md#get_get_filter) | **GET** /api/v2/projects/{project_id}/session-filters/{filter_id} | Get Saved Search
[**get_list_filters**](SavedSearchesApi.md#get_list_filters) | **GET** /api/v2/projects/{project_id}/session-filters | List Saved Searches
[**post_replicate_filter**](SavedSearchesApi.md#post_replicate_filter) | **POST** /api/v2/projects/{project_id}/session-filters | Create Saved Search
[**put_update_filter**](SavedSearchesApi.md#put_update_filter) | **PUT** /api/v2/projects/{project_id}/session-filters/{filter_id} | Update Saved Search

# **delete_delete_filter**
> object delete_delete_filter(project_id, filter_id)

Delete Saved Search

 Delete a saved search from the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SavedSearchesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Delete Saved Search
    api_response = api_instance.delete_delete_filter(project_id, filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchesApi->delete_delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_filter**
> SessionFilterReplicationInfo1 get_get_filter(project_id, filter_id)

Get Saved Search

 Retrieve details for a specific saved search by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SavedSearchesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
filter_id = NULL # object | 

try:
    # Get Saved Search
    api_response = api_instance.get_get_filter(project_id, filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchesApi->get_get_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 

### Return type

[**SessionFilterReplicationInfo1**](SessionFilterReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_filters**
> SessionFilterReplicationListResponse get_list_filters(project_id, page=page, page_size=page_size)

List Saved Searches

 Retrieve a paginated list of saved searches for the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SavedSearchesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
page = 1 # object |  (optional) (default to 1)
page_size = 30 # object |  (optional) (default to 30)

try:
    # List Saved Searches
    api_response = api_instance.get_list_filters(project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchesApi->get_list_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **page_size** | [**object**](.md)|  | [optional] [default to 30]

### Return type

[**SessionFilterReplicationListResponse**](SessionFilterReplicationListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_replicate_filter**
> SessionFilterReplicationInfo1 post_replicate_filter(project_id, body=body)

Create Saved Search

 Create or upsert a saved search for the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SavedSearchesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
body = swagger_client.ReplicateSessionFilterRequest() # ReplicateSessionFilterRequest |  (optional)

try:
    # Create Saved Search
    api_response = api_instance.post_replicate_filter(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchesApi->post_replicate_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **body** | [**ReplicateSessionFilterRequest**](ReplicateSessionFilterRequest.md)|  | [optional] 

### Return type

[**SessionFilterReplicationInfo1**](SessionFilterReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_filter**
> SessionFilterReplicationInfo1 put_update_filter(project_id, filter_id, body=body)

Update Saved Search

 Update an existing saved search.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SavedSearchesApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
filter_id = NULL # object | 
body = swagger_client.UpdateSessionFilterReplicationRequest() # UpdateSessionFilterReplicationRequest |  (optional)

try:
    # Update Saved Search
    api_response = api_instance.put_update_filter(project_id, filter_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchesApi->put_update_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **filter_id** | [**object**](.md)|  | 
 **body** | [**UpdateSessionFilterReplicationRequest**](UpdateSessionFilterReplicationRequest.md)|  | [optional] 

### Return type

[**SessionFilterReplicationInfo1**](SessionFilterReplicationInfo1.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

