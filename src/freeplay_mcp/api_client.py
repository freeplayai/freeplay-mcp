"""Shared API client setup and utilities for Freeplay MCP tools."""

import os
import sys
from importlib.metadata import version, PackageNotFoundError

# Add swagger client to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'swagger', 'python-api'))

# Get version from installed package metadata
try:
    MCP_VERSION = version("freeplay-mcp")
except PackageNotFoundError:
    MCP_VERSION = "version-not-found"

from swagger_client import Configuration, ApiClient
from swagger_client.api.configuration_api import ConfigurationApi
from swagger_client.api.search__analytics_api import SearchAnalyticsApi
from swagger_client.api.prompt_templates_api import PromptTemplatesApi

# Lazy-initialized API clients
_api_client: ApiClient | None = None
_config_api: ConfigurationApi | None = None
_search_api: SearchAnalyticsApi | None = None
_prompt_templates_api: PromptTemplatesApi | None = None


def get_api_client() -> ApiClient:
    """Get or create the Swagger API client."""
    global _api_client
    if _api_client is None:
        api_key = os.environ.get("FREEPLAY_API_KEY")
        if not api_key:
            raise ValueError("FREEPLAY_API_KEY environment variable is required.")

        base_url = os.environ.get("FREEPLAY_BASE_URL", "https://app.freeplay.ai").rstrip("/")
        verify_ssl_env = os.environ.get("FREEPLAY_VERIFY_SSL", "").lower()
        verify_ssl = verify_ssl_env not in ("false", "0", "no")

        config = Configuration()
        config.host = base_url
        config.verify_ssl = verify_ssl
        # Set up Bearer auth
        _api_client = ApiClient(config, header_name="Authorization", header_value=f"Bearer {api_key}")
        # Set custom user agent
        _api_client.user_agent = f"freeplay-mcp/{MCP_VERSION}"
    return _api_client


def get_config_api() -> ConfigurationApi:
    """Get or create the Configuration API."""
    global _config_api
    if _config_api is None:
        _config_api = ConfigurationApi(get_api_client())
    return _config_api


def get_search_api() -> SearchAnalyticsApi:
    """Get or create the Search Analytics API."""
    global _search_api
    if _search_api is None:
        _search_api = SearchAnalyticsApi(get_api_client())
    return _search_api


def get_prompt_templates_api() -> PromptTemplatesApi:
    """Get or create the Prompt Templates API."""
    global _prompt_templates_api
    if _prompt_templates_api is None:
        _prompt_templates_api = PromptTemplatesApi(get_api_client())
    return _prompt_templates_api


def build_filters(
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
) -> dict:
    """Build filter conditions for search endpoints."""
    filter_conditions = []

    if start_date is not None:
        start_value = start_date if " " in start_date else f"{start_date} 00:00:00"
        filter_conditions.append({"field": "start_time", "op": "gte", "value": start_value})
    if end_date is not None:
        end_value = end_date if " " in end_date else f"{end_date} 23:59:59"
        filter_conditions.append({"field": "start_time", "op": "lte", "value": end_value})

    equality_filters = [
        ("environment", environment),
        ("prompt_template", template_name),
        ("prompt_template_id", prompt_template_id),
        ("model", model),
        ("provider", provider),
        ("session_id", session_id),
        ("completion_id", completion_id),
        ("agent_name", agent_name),
        ("review_status", review_status),
    ]
    for field, value in equality_filters:
        if value is not None:
            filter_conditions.append({"field": field, "op": "eq", "value": value})

    if cost_min is not None:
        filter_conditions.append({"field": "cost", "op": "gte", "value": cost_min})
    if cost_max is not None:
        filter_conditions.append({"field": "cost", "op": "lte", "value": cost_max})
    if latency_min is not None:
        filter_conditions.append({"field": "latency", "op": "gte", "value": latency_min})
    if latency_max is not None:
        filter_conditions.append({"field": "latency", "op": "lte", "value": latency_max})

    if len(filter_conditions) == 0:
        return {}
    elif len(filter_conditions) == 1:
        return filter_conditions[0]
    else:
        return {"and": filter_conditions}
