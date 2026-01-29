"""Completion search tools."""

import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.models.search_request import SearchRequest

from ..api_client import get_search_api, build_filters

logger = logging.getLogger(__name__)


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
        filters = build_filters(
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
