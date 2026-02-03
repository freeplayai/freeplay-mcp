"""Insights tools."""

import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.api.default_api import DefaultApi
from swagger_client.models.search_request import SearchRequest

from ..api_client import get_api_client, get_search_api
from ..response import ListItem, ListResponse

logger = logging.getLogger(__name__)


async def list_insights(
    project_id: str,
    page: int = 1,
    page_size: int = 30,
    prompt_template_id: str | None = None,
    agent_id: str | None = None,
) -> str:
    """List insights for a Freeplay project.

    Retrieve a paginated list of insights for a project. Insights are automatically
    generated observations and patterns from your logged data. Filter by prompt
    template or agent to see specific insights.

    Args:
        project_id: The Freeplay project ID (required)
        page: Page number for pagination (default: 1)
        page_size: Number of insights per page (default: 30)
        prompt_template_id: Filter insights by prompt template UUID (optional)
        agent_id: Filter insights by agent UUID (optional)
    """
    api = DefaultApi(get_api_client())
    
    kwargs = {
        'page': page,
        'page_size': page_size,
    }
    
    if prompt_template_id is not None:
        kwargs['prompt_template_id'] = prompt_template_id
    if agent_id is not None:
        kwargs['agent_id'] = agent_id
    
    result = await asyncio.to_thread(api.get_get_insights, project_id, **kwargs)
    
    data = result.get('data', [])
    pagination = result.get('pagination', {})
    
    items = []
    for insight in data:
        insight_id = insight.get('id', 'unknown')
        name = insight.get('name', 'Unnamed')
        description = insight.get('description', '')
        record_count = insight.get('record_count', 0)
        context_source = insight.get('context_source', '')
        
        lines = []
        if description:
            lines.append(description)
        lines.append(f"Records: {record_count}")
        lines.append(f"Source: {context_source}")
        
        template_id = insight.get('prompt_template_id')
        if template_id:
            lines.append(f"Template ID: {template_id}")
        
        agent_id_val = insight.get('agent_id')
        if agent_id_val:
            lines.append(f"Agent ID: {agent_id_val}")
        
        items.append(ListItem(
            id=insight_id,
            title=name,
            lines=lines,
        ))
    
    return ListResponse(
        header=f"Insights for Project {project_id}",
        items=items,
        has_next=pagination.get('has_next', False)
    ).render()


async def search_completions_by_insight(
    project_id: str,
    insight_name: str,
    page_size: int = 100,
) -> str:
    """Search for completions associated with a specific insight.

    Finds all completions that match the given insight name. Use this to
    understand what data is associated with an insight before creating
    datasets or running optimizations.

    Args:
        project_id: The Freeplay project ID
        insight_name: The exact name of the insight (from list_insights)
        page_size: Maximum number of completions to return (default: 100)
    """
    search_api = get_search_api()
    
    filters = {
        "field": "insight_name",
        "op": "eq",
        "value": insight_name,
    }
    
    search_body = SearchRequest(filters=filters)
    
    result = await asyncio.to_thread(
        search_api.post_search_completions,
        project_id,
        body=search_body,
        page=1,
        page_size=page_size,
    )
    
    completions = result.data if hasattr(result, 'data') else []
    
    items = []
    for comp in completions:
        if isinstance(comp, dict):
            comp_id = comp.get('completion_id', 'unknown')
            input_variables = comp.get('input_variables', {})
            metadata = comp.get('completion_metadata', {})
        else:
            comp_id = getattr(comp, 'completion_id', 'unknown')
            input_variables = getattr(comp, 'input_variables', {})
            metadata = getattr(comp, 'completion_metadata', {})
        
        # Show preview of inputs
        input_preview = str(input_variables)[:100]
        if len(str(input_variables)) > 100:
            input_preview += "..."
        
        model = metadata.get('model', 'N/A') if isinstance(metadata, dict) else 'N/A'
        
        items.append(ListItem(
            id=comp_id,
            title=f"Completion {comp_id[:8]}...",
            lines=[
                f"Model: {model}",
                f"Inputs: {input_preview}",
            ],
        ))
    
    return ListResponse(
        header=f"Found {len(items)} completions for insight '{insight_name}'",
        items=items,
    ).render()
