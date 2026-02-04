# swagger_client.ObservabilityApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_delete_session**](ObservabilityApi.md#delete_delete_session) | **DELETE** /api/v2/projects/{project_id}/sessions/{session_id} | Delete Session
[**patch_update_session_metadata**](ObservabilityApi.md#patch_update_session_metadata) | **PATCH** /api/v2/projects/{project_id}/sessions/id/{session_id}/metadata | Update Session Metadata
[**patch_update_trace_by_id**](ObservabilityApi.md#patch_update_trace_by_id) | **PATCH** /api/v2/projects/{project_id}/sessions/{session_id}/traces/id/{trace_id} | Update Trace by ID
[**patch_update_trace_by_otel_span_id**](ObservabilityApi.md#patch_update_trace_by_otel_span_id) | **PATCH** /api/v2/projects/{project_id}/sessions/{session_id}/traces/otel-span-id/{otel_span_id_hex} | Update Trace by OTEL Span ID
[**patch_update_trace_metadata**](ObservabilityApi.md#patch_update_trace_metadata) | **PATCH** /api/v2/projects/{project_id}/sessions/{session_id}/traces/id/{trace_id}/metadata | Update Trace Metadata
[**post_create_completion_feedback**](ObservabilityApi.md#post_create_completion_feedback) | **POST** /api/v2/projects/{project_id}/completion-feedback/id/{completion_id} | Add Completion Feedback
[**post_record_completion**](ObservabilityApi.md#post_record_completion) | **POST** /api/v2/projects/{project_id}/sessions/{session_id}/completions | Record Completion
[**post_record_trace**](ObservabilityApi.md#post_record_trace) | **POST** /api/v2/projects/{project_id}/sessions/{session_id}/traces/id/{trace_id} | Record Trace
[**post_trace_feedback**](ObservabilityApi.md#post_trace_feedback) | **POST** /api/v2/projects/{project_id}/trace-feedback/id/{trace_id} | Add Trace Feedback
[**post_update**](ObservabilityApi.md#post_update) | **POST** /api/v2/projects/{project_id}/completions/{completion_id} | Update Completion

# **delete_delete_session**
> delete_delete_session(project_id, session_id)

Delete Session

 Permanently delete a session and all associated completions. Use when removing test data or honoring data deletion requests.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 

try:
    # Delete Session
    api_instance.delete_delete_session(project_id, session_id)
except ApiException as e:
    print("Exception when calling ObservabilityApi->delete_delete_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_session_metadata**
> SimpleResponseWithMessage patch_update_session_metadata(project_id, session_id, body=body)

Update Session Metadata

 Merge custom metadata into an existing session. Use to enrich sessions with post-hoc context like user ID or business metrics. [See SDK method.](https://docs.freeplay.ai/freeplay-sdk/sessions)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 
body = NULL # object |  (optional)

try:
    # Update Session Metadata
    api_response = api_instance.patch_update_session_metadata(project_id, session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->patch_update_session_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_trace_by_id**
> SimpleResponseWithMessage patch_update_trace_by_id(project_id, session_id, trace_id, body=body)

Update Trace by ID

 Update a trace's metadata and/or feedback by its trace ID. This endpoint is a superset of the older metadata and feedback update endpoints.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 
trace_id = NULL # object | 
body = swagger_client.TraceUpdateRequest() # TraceUpdateRequest |  (optional)

try:
    # Update Trace by ID
    api_response = api_instance.patch_update_trace_by_id(project_id, session_id, trace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->patch_update_trace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 
 **trace_id** | [**object**](.md)|  | 
 **body** | [**TraceUpdateRequest**](TraceUpdateRequest.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_trace_by_otel_span_id**
> SimpleResponseWithMessage patch_update_trace_by_otel_span_id(project_id, session_id, otel_span_id_hex, body=body)

Update Trace by OTEL Span ID

 Update a trace's metadata and/or feedback by its OpenTelemetry span ID (hex string).  Note: OTEL spans are mapped to Freeplay Traces, so we use the OTEL span ID to identify Traces.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 
otel_span_id_hex = NULL # object | 
body = swagger_client.TraceUpdateRequest1() # TraceUpdateRequest1 |  (optional)

try:
    # Update Trace by OTEL Span ID
    api_response = api_instance.patch_update_trace_by_otel_span_id(project_id, session_id, otel_span_id_hex, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->patch_update_trace_by_otel_span_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 
 **otel_span_id_hex** | [**object**](.md)|  | 
 **body** | [**TraceUpdateRequest1**](TraceUpdateRequest1.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_update_trace_metadata**
> SimpleResponseWithMessage patch_update_trace_metadata(project_id, session_id, trace_id, body=body)

Update Trace Metadata

 Merge custom metadata into an existing trace. Use to enrich traces with post-hoc context.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 
trace_id = NULL # object | 
body = NULL # object |  (optional)

try:
    # Update Trace Metadata
    api_response = api_instance.patch_update_trace_metadata(project_id, session_id, trace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->patch_update_trace_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 
 **trace_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_completion_feedback**
> SimpleResponseWithMessage post_create_completion_feedback(project_id, completion_id, body=body)

Add Completion Feedback

 Record end-user feedback on a completion. Use to capture thumbs up/down ratings or custom feedback attributes. [See SDK method.](https://docs.freeplay.ai/freeplay-sdk/customer-feedback)  The `freeplay_feedback` field must be \"positive\" or \"negative\". Additional custom fields are supported.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
completion_id = NULL # object | 
body = NULL # object |  (optional)

try:
    # Add Completion Feedback
    api_response = api_instance.post_create_completion_feedback(project_id, completion_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->post_create_completion_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **completion_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_record_completion**
> RecordCompletionInfo post_record_completion(project_id, session_id, body=body)

Record Completion

 Log an LLM completion with its prompt, response, and metadata. This is the primary endpoint for observability. [See SDK method.](https://docs.freeplay.ai/freeplay-sdk/recording-completions)  Sessions are created implicitly—just generate a session_id client-side (UUID v4). Optionally provide your own completion_id too to avoid waiting for Freeplay's response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 
body = swagger_client.RecordPayload() # RecordPayload |  (optional)

try:
    # Record Completion
    api_response = api_instance.post_record_completion(project_id, session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->post_record_completion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 
 **body** | [**RecordPayload**](RecordPayload.md)|  | [optional] 

### Return type

[**RecordCompletionInfo**](RecordCompletionInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_record_trace**
> object post_record_trace(project_id, session_id, trace_id, body=body)

Record Trace

 Create or update a trace within a session. Use to group related completions in agent workflows. [See SDK method.](https://docs.freeplay.ai/freeplay-sdk/traces)  Generate the trace_id client-side (UUID v4) to avoid round-trip latency.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
session_id = NULL # object | 
trace_id = NULL # object | 
body = swagger_client.TracePayload() # TracePayload |  (optional)

try:
    # Record Trace
    api_response = api_instance.post_record_trace(project_id, session_id, trace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->post_record_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 
 **trace_id** | [**object**](.md)|  | 
 **body** | [**TracePayload**](TracePayload.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_trace_feedback**
> SimpleResponseWithMessage post_trace_feedback(project_id, trace_id, body=body)

Add Trace Feedback

 Record end-user feedback on a trace. Use to capture feedback on conversation turns or agent workflow outcomes. [See SDK method.](https://docs.freeplay.ai/freeplay-sdk/customer-feedback)  The `freeplay_feedback` field must be \"positive\" or \"negative\". Additional custom fields are supported.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
trace_id = NULL # object | 
body = NULL # object |  (optional)

try:
    # Add Trace Feedback
    api_response = api_instance.post_trace_feedback(project_id, trace_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->post_trace_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **trace_id** | [**object**](.md)|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**SimpleResponseWithMessage**](SimpleResponseWithMessage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_update**
> RecordCompletionInfo post_update(project_id, completion_id, body=body)

Update Completion

 Append messages or evaluation results to an existing completion. Use for streaming responses or adding post-hoc evaluation metrics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObservabilityApi(swagger_client.ApiClient(configuration))
project_id = NULL # object | 
completion_id = NULL # object | 
body = swagger_client.RecordUpdatePayload() # RecordUpdatePayload |  (optional)

try:
    # Update Completion
    api_response = api_instance.post_update(project_id, completion_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObservabilityApi->post_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)|  | 
 **completion_id** | [**object**](.md)|  | 
 **body** | [**RecordUpdatePayload**](RecordUpdatePayload.md)|  | [optional] 

### Return type

[**RecordCompletionInfo**](RecordCompletionInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

