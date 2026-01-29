"""Project management tools."""

import asyncio
import logging

from ..api_client import get_config_api

logger = logging.getLogger(__name__)


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
