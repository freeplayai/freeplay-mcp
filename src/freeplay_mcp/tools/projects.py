"""Project management tools."""

import asyncio
import logging

from ..api_client import get_config_api
from ..response import ListItem, ListResponse

logger = logging.getLogger(__name__)


async def list_projects() -> str:
    """List all Freeplay projects accessible to the authenticated user.

    Returns a formatted list of projects with their IDs and names.
    Use a project ID from this list for other Freeplay operations.
    """
    api = get_config_api()
    result = await asyncio.to_thread(api.get_get_projects)

    projects = result.projects if hasattr(result, 'projects') else result
    items = []
    for project in projects or []:
        project_id = project.id if hasattr(project, 'id') else project.get("id", "unknown")
        name = project.name if hasattr(project, 'name') else project.get("name", "Unnamed")
        description = project.description if hasattr(project, 'description') else project.get("description", "")

        items.append(ListItem(
            id=project_id,
            title=name,
            lines=[description] if description else [],
        ))

    return ListResponse(header="Available Freeplay Projects", items=items).render()
