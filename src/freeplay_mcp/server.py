"""Freeplay MCP Server - Workflow-oriented tools for the Freeplay API."""

import asyncio
import logging
import os
import sys

from mcp.server.fastmcp import FastMCP

# Add swagger client to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'swagger', 'python-api'))

from swagger_client import Configuration, ApiClient
from swagger_client.api.configuration_api import ConfigurationApi
from swagger_client.api.search__analytics_api import SearchAnalyticsApi
from swagger_client.models.search_request import SearchRequest

# Configure logging to stderr (stdout corrupts MCP JSON-RPC)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("freeplay")

# Lazy-initialized API clients
_api_client: ApiClient | None = None
_config_api: ConfigurationApi | None = None
_search_api: SearchAnalyticsApi | None = None


def get_api_client() -> ApiClient:
    """Get or create the Swagger API client."""
    global _api_client
    if _api_client is None:
        api_key = os.environ.get("FREEPLAY_API_KEY")
        if not api_key:
            raise ValueError("FREEPLAY_API_KEY environment variable is required.")

        base_url = os.environ.get("FREEPLAY_BASE_URL", "https://app.freeplay.ai").rstrip("/")
        verify_ssl_env = os.environ.get("FREEPLAY_VERIFY_SSL", "").lower()
        verify_ssl = verify_ssl_env not in ("false", "0", "no")

        config = Configuration()
        config.host = base_url
        config.verify_ssl = verify_ssl
        # Set up Bearer auth
        _api_client = ApiClient(config, header_name="Authorization", header_value=f"Bearer {api_key}")
    return _api_client


def get_config_api() -> ConfigurationApi:
    """Get or create the Configuration API."""
    global _config_api
    if _config_api is None:
        _config_api = ConfigurationApi(get_api_client())
    return _config_api


def get_search_api() -> SearchAnalyticsApi:
    """Get or create the Search Analytics API."""
    global _search_api
    if _search_api is None:
        _search_api = SearchAnalyticsApi(get_api_client())
    return _search_api


def _build_filters(
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    completion_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> dict:
    """Build filter conditions for search endpoints."""
    filter_conditions = []

    if start_date is not None:
        start_value = start_date if " " in start_date else f"{start_date} 00:00:00"
        filter_conditions.append({"field": "start_time", "op": "gte", "value": start_value})
    if end_date is not None:
        end_value = end_date if " " in end_date else f"{end_date} 23:59:59"
        filter_conditions.append({"field": "start_time", "op": "lte", "value": end_value})

    equality_filters = [
        ("environment", environment),
        ("prompt_template", template_name),
        ("prompt_template_id", prompt_template_id),
        ("model", model),
        ("provider", provider),
        ("session_id", session_id),
        ("completion_id", completion_id),
        ("agent_name", agent_name),
        ("review_status", review_status),
    ]
    for field, value in equality_filters:
        if value is not None:
            filter_conditions.append({"field": field, "op": "eq", "value": value})

    if cost_min is not None:
        filter_conditions.append({"field": "cost", "op": "gte", "value": cost_min})
    if cost_max is not None:
        filter_conditions.append({"field": "cost", "op": "lte", "value": cost_max})
    if latency_min is not None:
        filter_conditions.append({"field": "latency", "op": "gte", "value": latency_min})
    if latency_max is not None:
        filter_conditions.append({"field": "latency", "op": "lte", "value": latency_max})

    if len(filter_conditions) == 0:
        return {}
    elif len(filter_conditions) == 1:
        return filter_conditions[0]
    else:
        return {"and": filter_conditions}


@mcp.tool()
async def list_projects() -> str:
    """List all Freeplay projects accessible to the authenticated user.

    Returns a formatted list of projects with their IDs and names.
    Use a project ID from this list for other Freeplay operations.
    """
    try:
        api = get_config_api()
        result = await asyncio.to_thread(api.get_get_projects)

        projects = result.projects if hasattr(result, 'projects') else result
        if not projects:
            return "No projects found."

        lines = ["Available Freeplay Projects:", ""]
        for project in projects:
            project_id = project.id if hasattr(project, 'id') else project.get("id", "unknown")
            name = project.name if hasattr(project, 'name') else project.get("name", "Unnamed")
            description = project.description if hasattr(project, 'description') else project.get("description", "")

            line = f"- {name} (ID: {project_id})"
            if description:
                line += f"\n  {description}"
            lines.append(line)

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error listing projects")
        return f"Error listing projects: {e}"


@mcp.tool()
async def search_completions(
    project_id: str,
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    completion_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> str:
    """Search logged completions in a Freeplay project.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter completions after this ISO date (e.g., "2024-01-01")
        end_date: Filter completions before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
        prompt_template_id: Filter by prompt template ID
        model: Filter by model name (e.g., "gpt-4", "claude-3")
        provider: Filter by provider (e.g., "openai", "anthropic")
        session_id: Filter by session ID
        completion_id: Filter by specific completion ID
        agent_name: Filter by agent name
        review_status: Filter by review status
        cost_min: Filter by minimum cost
        cost_max: Filter by maximum cost
        latency_min: Filter by minimum latency (ms)
        latency_max: Filter by maximum latency (ms)
    """
    try:
        api = get_search_api()
        filters = _build_filters(
            start_date=start_date, end_date=end_date, environment=environment,
            template_name=template_name, prompt_template_id=prompt_template_id,
            model=model, provider=provider, session_id=session_id,
            completion_id=completion_id, agent_name=agent_name,
            review_status=review_status, cost_min=cost_min, cost_max=cost_max,
            latency_min=latency_min, latency_max=latency_max,
        )

        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1
        body = SearchRequest(filters=filters)

        result = await asyncio.to_thread(
            api.post_search_completions, project_id, body=body, page=page, page_size=page_size
        )

        completions = result.data if hasattr(result, 'data') else []
        pagination = result.pagination if hasattr(result, 'pagination') else {}
        has_next = pagination.has_next if hasattr(pagination, 'has_next') else False

        if not completions:
            return "No completions found matching the search criteria."

        lines = [f"Found {len(completions)} completions (has_next: {has_next}):", ""]

        for comp in completions:
            # Handle both dict and object access patterns (API returns dicts)
            if isinstance(comp, dict):
                comp_id = comp.get('completion_id', comp.get('id', 'unknown'))
                metadata = comp.get('completion_metadata', {}) or {}
                messages = comp.get('messages', [])
            else:
                comp_id = getattr(comp, 'completion_id', getattr(comp, 'id', 'unknown'))
                metadata = getattr(comp, 'completion_metadata', {}) or {}
                messages = getattr(comp, 'messages', [])

            if isinstance(metadata, dict):
                start_time = metadata.get('start_time', 'unknown')
                template_info = metadata.get('prompt_template')
                env = metadata.get('environment', 'N/A')
                model_name = metadata.get('model', 'N/A')
            else:
                start_time = getattr(metadata, 'start_time', 'unknown')
                template_info = getattr(metadata, 'prompt_template', None)
                env = getattr(metadata, 'environment', 'N/A')
                model_name = getattr(metadata, 'model', 'N/A')

            if isinstance(template_info, dict):
                template = template_info.get('name', 'N/A')
            elif template_info:
                template = getattr(template_info, 'name', 'N/A')
            else:
                template = 'N/A'

            lines.append(f"- ID: {comp_id}")
            lines.append(f"  Template: {template} | Env: {env} | Model: {model_name}")
            lines.append(f"  Time: {start_time}")

            if messages:
                last_msg = messages[-1] if messages else {}
                if isinstance(last_msg, dict):
                    content = str(last_msg.get('content', ''))[:100]
                    full_content = str(last_msg.get('content', ''))
                else:
                    content = str(getattr(last_msg, 'content', ''))[:100]
                    full_content = str(getattr(last_msg, 'content', ''))
                if len(full_content) > 100:
                    content += "..."
                lines.append(f"  Last message: {content}")

            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error searching completions")
        return f"Error searching completions: {e}"


@mcp.tool()
async def search_traces(
    project_id: str,
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> str:
    """Search traces in a Freeplay project.

    Traces represent structured execution flows/chains within a session,
    and can have parent-child relationships.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter traces after this ISO date (e.g., "2024-01-01")
        end_date: Filter traces before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
        prompt_template_id: Filter by prompt template ID
        model: Filter by model name (e.g., "gpt-4", "claude-3")
        provider: Filter by provider (e.g., "openai", "anthropic")
        session_id: Filter by session ID
        agent_name: Filter by agent name
        review_status: Filter by review status
        cost_min: Filter by minimum cost
        cost_max: Filter by maximum cost
        latency_min: Filter by minimum latency (ms)
        latency_max: Filter by maximum latency (ms)
    """
    try:
        api = get_search_api()
        filters = _build_filters(
            start_date=start_date, end_date=end_date, environment=environment,
            template_name=template_name, prompt_template_id=prompt_template_id,
            model=model, provider=provider, session_id=session_id,
            agent_name=agent_name, review_status=review_status,
            cost_min=cost_min, cost_max=cost_max,
            latency_min=latency_min, latency_max=latency_max,
        )

        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1
        body = SearchRequest(filters=filters)

        result = await asyncio.to_thread(
            api.post_search_traces, project_id, body=body, page=page, page_size=page_size
        )

        traces = result.data if hasattr(result, 'data') else []
        pagination = result.pagination if hasattr(result, 'pagination') else {}
        has_next = pagination.has_next if hasattr(pagination, 'has_next') else False

        if not traces:
            return "No traces found matching the search criteria."

        lines = [f"Found {len(traces)} traces (has_next: {has_next}):", ""]

        for trace in traces:
            # Handle both dict and object access patterns (API returns dicts)
            if isinstance(trace, dict):
                trace_id = trace.get('trace_id', trace.get('id', 'unknown'))
                name = trace.get('name', 'N/A')
                kind = trace.get('kind', 'N/A')
                agent = trace.get('agent_name', 'N/A')
                start_time = trace.get('start_time', 'unknown')
                end_time = trace.get('end_time', 'unknown')
                parent_id = trace.get('parent_id')
                trace_input = trace.get('input', '')
            else:
                trace_id = getattr(trace, 'trace_id', getattr(trace, 'id', 'unknown'))
                name = getattr(trace, 'name', 'N/A')
                kind = getattr(trace, 'kind', 'N/A')
                agent = getattr(trace, 'agent_name', 'N/A')
                start_time = getattr(trace, 'start_time', 'unknown')
                end_time = getattr(trace, 'end_time', 'unknown')
                parent_id = getattr(trace, 'parent_id', None)
                trace_input = getattr(trace, 'input', '')

            lines.append(f"- ID: {trace_id}")
            lines.append(f"  Name: {name} | Kind: {kind} | Agent: {agent}")
            lines.append(f"  Time: {start_time} -> {end_time}")
            if parent_id:
                lines.append(f"  Parent: {parent_id}")

            if trace_input:
                content = str(trace_input)[:100]
                if len(str(trace_input)) > 100:
                    content += "..."
                lines.append(f"  Input: {content}")

            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error searching traces")
        return f"Error searching traces: {e}"


@mcp.tool()
async def search_sessions(
    project_id: str,
    limit: int = 20,
    offset: int = 0,
    start_date: str | None = None,
    end_date: str | None = None,
    environment: str | None = None,
    template_name: str | None = None,
    prompt_template_id: str | None = None,
    model: str | None = None,
    provider: str | None = None,
    session_id: str | None = None,
    agent_name: str | None = None,
    review_status: str | None = None,
    cost_min: float | None = None,
    cost_max: float | None = None,
    latency_min: float | None = None,
    latency_max: float | None = None,
) -> str:
    """Search sessions in a Freeplay project.

    Sessions are top-level containers that group related traces and completions together.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter sessions after this ISO date (e.g., "2024-01-01")
        end_date: Filter sessions before this ISO date
        environment: Filter by environment (e.g., "production", "staging")
        template_name: Filter by prompt template name
        prompt_template_id: Filter by prompt template ID
        model: Filter by model name (e.g., "gpt-4", "claude-3")
        provider: Filter by provider (e.g., "openai", "anthropic")
        session_id: Filter by specific session ID
        agent_name: Filter by agent name
        review_status: Filter by review status
        cost_min: Filter by minimum cost
        cost_max: Filter by maximum cost
        latency_min: Filter by minimum latency (ms)
        latency_max: Filter by maximum latency (ms)
    """
    try:
        api = get_search_api()
        filters = _build_filters(
            start_date=start_date, end_date=end_date, environment=environment,
            template_name=template_name, prompt_template_id=prompt_template_id,
            model=model, provider=provider, session_id=session_id,
            agent_name=agent_name, review_status=review_status,
            cost_min=cost_min, cost_max=cost_max,
            latency_min=latency_min, latency_max=latency_max,
        )

        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1
        body = SearchRequest(filters=filters)

        result = await asyncio.to_thread(
            api.post_search_sessions, project_id, body=body, page=page, page_size=page_size
        )

        sessions = result.data if hasattr(result, 'data') else []
        pagination = result.pagination if hasattr(result, 'pagination') else {}
        has_next = pagination.has_next if hasattr(pagination, 'has_next') else False

        if not sessions:
            return "No sessions found matching the search criteria."

        lines = [f"Found {len(sessions)} sessions (has_next: {has_next}):", ""]

        for session in sessions:
            # Handle both dict and object access patterns (API returns dicts)
            if isinstance(session, dict):
                sess_id = session.get('session_id', session.get('id', 'unknown'))
                env = session.get('environment', 'N/A')
                start_time = session.get('start_time', 'unknown')
                metadata = session.get('custom_metadata', {}) or {}
            else:
                sess_id = getattr(session, 'session_id', getattr(session, 'id', 'unknown'))
                env = getattr(session, 'environment', 'N/A')
                start_time = getattr(session, 'start_time', 'unknown')
                metadata = getattr(session, 'custom_metadata', {}) or {}

            lines.append(f"- ID: {sess_id}")
            lines.append(f"  Environment: {env}")
            lines.append(f"  Time: {start_time}")
            if metadata:
                if isinstance(metadata, dict):
                    meta_str = ", ".join(f"{k}={v}" for k, v in list(metadata.items())[:3])
                    if len(metadata) > 3:
                        meta_str += ", ..."
                    lines.append(f"  Metadata: {meta_str}")

            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error searching sessions")
        return f"Error searching sessions: {e}"


def main() -> None:
    """Run the Freeplay MCP server."""
    logger.info("Starting Freeplay MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
