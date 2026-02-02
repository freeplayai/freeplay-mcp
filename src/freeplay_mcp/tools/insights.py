"""Insights tools."""

import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.api.default_api import DefaultApi

from ..api_client import get_api_client
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
