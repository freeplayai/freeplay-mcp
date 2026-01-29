"""Trace search tools."""

import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.models.search_request import SearchRequest

from ..api_client import get_search_api, build_filters
from ..response import ListItem, ListResponse

logger = logging.getLogger(__name__)


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
    api = get_search_api()
    filters = build_filters(
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

    items = []
    for trace in traces:
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

        lines = [
            f"Name: {name} | Kind: {kind} | Agent: {agent}",
            f"Time: {start_time} -> {end_time}",
        ]
        if parent_id:
            lines.append(f"Parent: {parent_id}")

        if trace_input:
            content = str(trace_input)[:100]
            if len(str(trace_input)) > 100:
                content += "..."
            lines.append(f"Input: {content}")

        items.append(ListItem(id=trace_id, title=f"ID: {trace_id}", lines=lines))

    return ListResponse(
        header=f"Found {len(items)} traces",
        items=items,
        has_next=has_next,
    ).render()
