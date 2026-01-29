"""Session search tools."""

import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.models.search_request import SearchRequest

from ..api_client import get_search_api, build_filters

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
