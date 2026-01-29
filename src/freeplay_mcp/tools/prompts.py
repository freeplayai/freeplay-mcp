"""Prompt template management tools."""

import asyncio
import json
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'swagger', 'python-api'))

from swagger_client.models.create_template_version_request1 import CreateTemplateVersionRequest1

from ..api_client import get_prompt_templates_api

logger = logging.getLogger(__name__)


async def list_prompt_templates(
    project_id: str,
    limit: int = 50,
    offset: int = 0,
) -> str:
    """List all prompt templates in a Freeplay project.

    Returns a list of prompt templates with their IDs, names, and latest version info.
    Use the template name or ID when creating new versions.

    Args:
        project_id: The Freeplay project ID (required)
        limit: Maximum number of results to return (default: 50)
        offset: Number of results to skip for pagination (default: 0)
    """
    try:
        api = get_prompt_templates_api()

        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1

        result = await asyncio.to_thread(
            api.get_list_prompt_templates, project_id, page=page, page_size=page_size
        )

        templates = result.data if hasattr(result, 'data') else []
        if not templates:
            return "No prompt templates found in this project."

        lines = [f"Found {len(templates)} prompt templates:", ""]

        for template in templates:
            if isinstance(template, dict):
                template_id = template.get('id', 'unknown')
                name = template.get('name', 'Unnamed')
                latest_version_id = template.get('latest_template_version_id', 'N/A')
            else:
                template_id = getattr(template, 'id', 'unknown')
                name = getattr(template, 'name', 'Unnamed')
                latest_version_id = getattr(template, 'latest_template_version_id', 'N/A')

            lines.append(f"- {name}")
            lines.append(f"  ID: {template_id}")
            lines.append(f"  Latest Version ID: {latest_version_id}")
            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error listing prompt templates")
        return f"Error listing prompt templates: {e}"


async def create_prompt_version_and_deploy(
    project_id: str,
    template_name: str,
    prompt_messages: str,
    model: str,
    provider: str,
    environments: str,
    version_name: str | None = None,
    version_description: str | None = None,
    llm_parameters: dict | None = None,
    tool_schema: list | None = None,
    output_schema: dict | None = None,
    create_if_not_exists: bool = True,
) -> str:
    """Create a new version of a prompt template and deploy it to specified environment(s).

    This tool creates a new version of a prompt template with the given content and
    automatically deploys it to the specified environment(s). If the template doesn't
    exist, it can optionally be created automatically.

    Note: If an identical version already exists, it will be reused and the environments
    will be updated rather than creating a duplicate.

    Args:
        project_id: The Freeplay project ID (required)
        template_name: Name of the prompt template (required)
        prompt_messages: JSON string of template messages array, e.g. '[{"role": "system", "content": "You are helpful."}]' (required)
        model: The model name, e.g. "gpt-4", "claude-3-opus" (required)
        provider: The provider name, e.g. "openai", "anthropic" (required)
        environments: Comma-separated list of environments to deploy to, e.g. "staging,production" (required)
        version_name: Optional name for this version
        version_description: Optional description for this version
        llm_parameters: Optional LLM parameters object, e.g. {"temperature": 0.7, "max_tokens": 1000}
        tool_schema: Optional tool definitions array for function calling
        output_schema: Optional output schema for structured outputs
        create_if_not_exists: If true, creates the template if it doesn't exist (default: true)
    """
    try:
        api = get_prompt_templates_api()

        # Parse the prompt messages JSON
        try:
            messages = json.loads(prompt_messages)
        except json.JSONDecodeError as e:
            return f"Error: Invalid JSON for prompt_messages: {e}"

        # Parse environments list
        env_list = [env.strip() for env in environments.split(",") if env.strip()]
        if not env_list:
            return "Error: At least one environment must be specified."

        # Create the request body
        body = CreateTemplateVersionRequest1(
            template_messages=messages,
            model=model,
            provider=provider,
            environments=env_list,
            version_name=version_name,
            version_description=version_description,
            llm_parameters=llm_parameters,
            tool_schema=tool_schema,
            output_schema=output_schema,
        )

        # Call the API with _preload_content=False to avoid model validation bugs
        response = await asyncio.to_thread(
            api.post_create_template_version_by_name,
            project_id,
            template_name,
            body=body,
            create_template_if_not_exists=create_if_not_exists,
            _preload_content=False,
        )
        result = json.loads(response.data.decode('utf-8'))

        version_id = result.get('prompt_template_version_id', result.get('id', 'unknown'))
        template_id = result.get('prompt_template_id', 'unknown')
        deployed_envs = result.get('environments', env_list)

        lines = [
            "Successfully created/updated prompt version:",
            "",
            f"Template Name: {template_name}",
            f"Template ID: {template_id}",
            f"Version ID: {version_id}",
            f"Model: {model}",
            f"Provider: {provider}",
            f"Deployed to: {', '.join(deployed_envs) if isinstance(deployed_envs, list) else deployed_envs}",
        ]

        if version_name:
            lines.append(f"Version Name: {version_name}")
        if version_description:
            lines.append(f"Description: {version_description}")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error creating prompt version")
        return f"Error creating prompt version: {e}"


async def get_prompt_version(
    project_id: str,
    template_id: str,
    version_id: str,
) -> str:
    """Get the full contents of a prompt template version.

    Returns the complete prompt configuration including messages, model, provider,
    and LLM parameters. Use this to inspect a version before making updates.

    Args:
        project_id: The Freeplay project ID
        template_id: The prompt template ID
        version_id: The version ID to retrieve
    """
    try:
        api = get_prompt_templates_api()

        # Use _preload_content=False to get raw response and avoid model validation bugs
        response = await asyncio.to_thread(
            api.get_get_by_template_version_id, project_id, template_id, version_id,
            _preload_content=False
        )
        data = json.loads(response.data.decode('utf-8'))

        metadata = data.get('metadata', {})
        messages = data.get('content', [])
        model = metadata.get('model', 'unknown')
        provider = metadata.get('provider', 'unknown')
        llm_params = metadata.get('params', {})
        tool_schema = data.get('tool_schema', [])
        version_name = data.get('version_name', '')
        version_desc = data.get('version_description', '')
        template_name = data.get('prompt_template_name', '')

        lines = [
            f"Prompt: {template_name}",
            f"Version: {version_name or version_id}",
            "",
            f"Model: {model}",
            f"Provider: {provider}",
        ]

        if version_desc:
            lines.append(f"Description: {version_desc}")

        if llm_params:
            lines.append("")
            lines.append("LLM Parameters:")
            lines.append(json.dumps(llm_params, indent=2))

        lines.append("")
        lines.append("Messages:")
        lines.append(json.dumps(messages, indent=2))

        if tool_schema:
            lines.append("")
            lines.append("Tools:")
            lines.append(json.dumps(tool_schema, indent=2))

        return "\n".join(lines)

    except Exception as e:
        logger.exception("Error getting prompt version")
        return f"Error getting prompt version: {e}"
