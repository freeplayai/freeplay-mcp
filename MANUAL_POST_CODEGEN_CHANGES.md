# Get Insights API - Implementation Summary

## Overview
Added Python API support for Freeplay's GET insights endpoint (`/api/v2/projects/{project_id}/insights`).

## Changes Made

### 1. Swagger Client - DefaultApi Class
**File**: `swagger/python-api/swagger_client/api/default_api.py`

Added two new methods following the existing pattern:
- `get_get_insights()` - Main method to call the insights endpoint
- `get_get_insights_with_http_info()` - Method with full HTTP info

**Parameters**:
- `project_id` (required): The project ID
- `page` (optional, default=1): Page number for pagination
- `page_size` (optional, default=30): Number of results per page
- `prompt_template_id` (optional): Filter by prompt template UUID
- `agent_id` (optional): Filter by agent UUID

**Returns**: Object with `data` (array of Insight objects) and `pagination` info

### 2. API Documentation
**File**: `swagger/python-api/docs/DefaultApi.md`

Added documentation for the new `get_get_insights` method including:
- Method signature
- Example usage
- Parameter descriptions
- Return type information
- Authorization requirements

### 3. MCP Tool - list_insights
**File**: `src/freeplay_mcp/tools/insights.py`

Created a new MCP tool that:
- Calls the `get_get_insights` API method
- Formats the response using `ListResponse` for consistent display
- Supports all query parameters (pagination, filtering)
- Displays key insight information:
  - ID and name
  - Description
  - Record count
  - Context source
  - Associated template/agent IDs

### 4. Tool Registration
**Files**: 
- `src/freeplay_mcp/tools/__init__.py` - Exported the new tool
- `src/freeplay_mcp/server.py` - Registered the tool with the MCP server

## Insight Response Structure

Based on the OpenAPI spec, each Insight contains:
- `id` (UUID): Unique identifier
- `name` (string): Insight name
- `description` (string): Detailed description
- `prompt_template_id` (UUID or null): Associated prompt template
- `agent_id` (UUID or null): Associated agent
- `record_count` (integer): Number of records
- `context_source` (string): Source of the insight
- `first_seen` (number): First occurrence timestamp
- `last_seen` (number): Last occurrence timestamp

## Usage Example

```python
from freeplay_mcp.tools import list_insights

# List all insights for a project
result = await list_insights(project_id="your-project-id")

# With pagination
result = await list_insights(
    project_id="your-project-id",
    page=2,
    page_size=50
)

# Filter by prompt template
result = await list_insights(
    project_id="your-project-id",
    prompt_template_id="template-uuid"
)

# Filter by agent
result = await list_insights(
    project_id="your-project-id",
    agent_id="agent-uuid"
)
```

## Testing

The implementation follows the same patterns as existing tools:
- Uses `asyncio.to_thread()` for async API calls
- Leverages `ListResponse` for formatted output
- Includes proper error handling via the swagger client
- Supports both text and JSON output formats

## References

- [Freeplay API Documentation](https://docs.freeplay.ai/api-reference/get-insights)
- OpenAPI Spec: `skills/freeplay-api/openapi.json` (line 10452)
