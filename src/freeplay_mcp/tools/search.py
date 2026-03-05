"""Unified search tool for sessions, traces, and completions."""

import asyncio
import json
from typing import Literal

from freeplay_mcp.vendor.swagger_client.models.search_request import (
    SearchRequest,  # type: ignore[import-untyped]
)

from ..api_client import get_search_api

ResultType = Literal["sessions", "traces", "completions"]

SEARCH_ENDPOINT = {
    "sessions": "post_search_sessions",
    "traces": "post_search_traces",
    "completions": "post_search_completions",
}


async def search(
    project_id: str,
    result_type: ResultType,
    filters: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> str:
    """Search observability data in a Freeplay project. This is a read-only operation.

    Returns sessions, traces, or completions matching the given filters.

    - **Sessions** are top-level containers that group related traces and completions,
      representing a complete user interaction, conversation, or agent run.
    - **Traces** group related completions and tool calls within a session, representing
      a functional unit of work such as a single agent run or workflow step.
    - **Completions** are individual LLM calls with their inputs, outputs, and metadata.

    ## Filter syntax

    The `filters` parameter accepts a JSON string. A single filter has the form:
        {"field": "<field>", "op": "<operator>", "value": <value>}

    ### Operators
        eq        Equals
        lt        Less than
        gt        Greater than
        lte       Less than or equal
        gte       Greater than or equal
        contains  Contains substring
        between   Within numeric range

    ### Available fields

    Numeric fields (support eq, lt, gt, lte, gte):
        cost                                  e.g. 0.003
        latency                               e.g. 8 (seconds)
        start_time                            e.g. "2024-06-01 00:00:00"

    Equality fields (support eq):
        environment                           e.g. "staging"
        prompt_template                       e.g. "my-prompt"
        prompt_template_id                    e.g. "uuid..."
        completion_id                         e.g. "uuid..."
        session_id                            e.g. "uuid..."
        model                                 e.g. "gpt-4o"
        provider                              e.g. "openai"
        review_status                         e.g. "review_complete"
        agent_name                            e.g. "support-agent"
        trace_agent_name                      e.g. "my-agent"
        api_key                               e.g. "production-key"
        assignee                              e.g. "user@example.com"
        insight_name                          e.g. "Response Quality Issues"

    Text search fields (support contains):
        completion_output                     e.g. "weather"

    Nested JSON fields (field.* syntax, support contains):
        completion_inputs.*                   e.g. field="completion_inputs.topic", value="weather"
        completion_feedback.*                 e.g. field="completion_feedback.rating", value="positive"
        session_custom_metadata.*             e.g. field="session_custom_metadata.user_type", value="premium"
        trace_custom_metadata.*               e.g. field="trace_custom_metadata.workflow", value="onboarding"
        trace_input.*                         e.g. field="trace_input.query", value="weather"
        trace_output.*                        e.g. field="trace_output.response", value="sunny"
        trace_feedback.*                      e.g. field="trace_feedback.rating", value="positive"

    Evaluation result fields (nested JSON, field.* syntax):
        completion_evaluation_results.*       supports eq. e.g. field="completion_evaluation_results.Response Quality", value="4"
        completion_client_evaluation_results.* supports eq. e.g. field="completion_client_evaluation_results.score", value="85"
        trace_evaluation_results.*            supports eq, gt, lt, gte, lte, contains. e.g. field="trace_evaluation_results.Quality Score", value=5
        trace_client_eval_results.*           supports eq, contains. e.g. field="trace_client_eval_results.confidence_score", value=0.95

    Evaluation notes fields:
        evaluation_notes.content              supports contains. e.g. "needs review"
        evaluation_notes.author               supports eq. e.g. "user@example.com"
        evaluation_notes.created_at           supports gt, lt, gte, lte. e.g. "2024-06-01 00:00:00"

    ### Compound filters

    Combine filters with "and", "or", "not" (nestable to any depth):
        {"and": [<filter>, <filter>, ...]}    All conditions must match
        {"or": [<filter>, <filter>, ...]}     At least one must match
        {"not": <filter>}                     Negates a condition

    Example - expensive GPT-4o or Claude completions outside production:
        {"and": [{"field": "cost", "op": "gte", "value": 0.001}, {"or": [{"field": "model", "op": "eq", "value": "gpt-4o"}, {"field": "model", "op": "eq", "value": "claude-3-opus"}]}, {"not": {"field": "environment", "op": "eq", "value": "prod"}}]}

    Args:
        project_id: The Freeplay project ID
        result_type: What to search for: "sessions", "traces", or "completions"
        filters: Optional JSON string with filter expression. Examples:
            Simple: '{"field": "environment", "op": "eq", "value": "production"}'
            Compound: '{"and": [{"field": "cost", "op": "gte", "value": 0.01}, {"field": "model", "op": "eq", "value": "gpt-4o"}]}'
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip for pagination (default: 0)
    """
    api = get_search_api()

    parsed_filters: dict = {}
    if filters:
        parsed_filters = json.loads(filters)

    page_size = limit
    page = (offset // limit) + 1 if limit > 0 else 1
    body = SearchRequest(filters=parsed_filters)

    endpoint_method = getattr(api, SEARCH_ENDPOINT[result_type])
    result = await asyncio.to_thread(
        endpoint_method, project_id, body=body, page=page, page_size=page_size
    )

    return json.dumps(
        {
            "result_type": result_type,
            "count": len(result.data),
            "has_next": result.pagination.has_next,
            "data": result.data,
        },
        indent=2,
        default=str,
    )
