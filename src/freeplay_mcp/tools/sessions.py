"""Session search tools."""

import asyncio
import logging

from freeplay_mcp.vendor.swagger_client.models.search_request import (
    SearchRequest,  # type: ignore[import-untyped]
)

from ..api_client import build_filters, get_search_api
from ..response import ListItem, ListResponse

logger = logging.getLogger(__name__)


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
    filters: str | None = None,
) -> str:
    """Search sessions in a Freeplay project. This is a read-only operation.

    Sessions are top-level containers for logging events that group related traces and completions
    together, representing a complete user interaction, conversation, or agent run.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
        start_date: Filter sessions after this ISO date (e.g., "2024-01-01")
        end_date: Filter sessions before this ISO date
        environment: Filter by environment (e.g., "prod", "dev", "local")
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
        filters: JSON string with additional filter conditions, AND'd with any named params above.

            Format: {"field": "<name>", "op": "<operator>", "value": <value>}
            Compound: {"and": [...]}, {"or": [...]}, {"not": {...}}
            Operators: eq, gt, gte, lt, lte, contains, between
            For between: value is [lower, upper] (e.g. [0.01, 0.05])

            Note on evaluation result fields: Use "contains" (not "eq") for
            non-numeric evaluation values (e.g. boolean or text client evals).
            The "eq" operator only matches numeric scores.

            Available fields:
            - completion_output (contains on LLM response text)
            - completion_inputs.<var> (contains on prompt input variables)
            - completion_evaluation_results.<criteria> (numeric auto-eval scores; use eq/gt/lt)
            - completion_client_evaluation_results.<name> (client eval results; use contains for text/boolean values, eq for numeric)
            - trace_evaluation_results.<criteria> (numeric trace auto-eval scores; use eq/gt/lt)
            - trace_client_eval_results.<name> (trace client eval results; use contains for text/boolean values, eq for numeric)
            - completion_feedback.<key>, trace_feedback.<key>
            - session_custom_metadata.<key>, trace_custom_metadata.<key>
            - trace_input.<key>, trace_output.<key>
            - api_key, assignee, prompt_version, trace_agent_name, trace_id
            - evaluation_notes.author, evaluation_notes.content, evaluation_notes.created_at
            - insight_name, insight_id

            Examples:
            '{"field": "completion_client_evaluation_results.Parseable", "op": "contains", "value": "no"}'
            '{"field": "completion_evaluation_results.Accuracy", "op": "gte", "value": 0.8}'
            '{"field": "completion_output", "op": "contains", "value": "error"}'
            '{"or": [{"field": "model", "op": "eq", "value": "gpt-4"}, {"field": "model", "op": "eq", "value": "claude-3"}]}'
    """
    api = get_search_api()
    filter_query = build_filters(
        start_date=start_date,
        end_date=end_date,
        environment=environment,
        template_name=template_name,
        prompt_template_id=prompt_template_id,
        model=model,
        provider=provider,
        session_id=session_id,
        agent_name=agent_name,
        review_status=review_status,
        cost_min=cost_min,
        cost_max=cost_max,
        latency_min=latency_min,
        latency_max=latency_max,
        extra_filters=filters,
    )

    page_size = limit
    page = (offset // limit) + 1 if limit > 0 else 1
    body = SearchRequest(filters=filter_query)

    result = await asyncio.to_thread(
        api.post_search_sessions, project_id, body=body, page=page, page_size=page_size
    )

    sessions = result.data if hasattr(result, "data") else []
    pagination = result.pagination if hasattr(result, "pagination") else {}
    has_next = pagination.has_next if hasattr(pagination, "has_next") else False

    items = []
    for session in sessions:
        if isinstance(session, dict):
            sess_id = session.get("session_id", session.get("id", "unknown"))
            env = session.get("environment", "N/A")
            start_time = session.get("start_time", "unknown")
            metadata = session.get("custom_metadata", {}) or {}
        else:
            sess_id = getattr(session, "session_id", getattr(session, "id", "unknown"))
            env = getattr(session, "environment", "N/A")
            start_time = getattr(session, "start_time", "unknown")
            metadata = getattr(session, "custom_metadata", {}) or {}

        lines = [
            f"Environment: {env}",
            f"Time: {start_time}",
        ]
        if metadata and isinstance(metadata, dict):
            meta_str = ", ".join(f"{k}={v}" for k, v in list(metadata.items())[:3])
            if len(metadata) > 3:
                meta_str += ", ..."
            lines.append(f"Metadata: {meta_str}")

        items.append(ListItem(id=sess_id, title=f"ID: {sess_id}", lines=lines))

    return ListResponse(
        header=f"Found {len(items)} sessions",
        items=items,
        has_next=has_next,
    ).render()
