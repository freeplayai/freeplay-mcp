"""Shared API client setup and utilities for Freeplay MCP tools."""

import os
from importlib.metadata import PackageNotFoundError, version

from .secrets import SecretString

# Get version from installed package metadata
try:
    _mcp_version = version("freeplay-mcp")
except PackageNotFoundError:
    _mcp_version = "version-not-found"
MCP_VERSION = _mcp_version

from freeplay_mcp.vendor.swagger_client import (  # type: ignore[import-untyped]
    ApiClient,
    Configuration,
)
from freeplay_mcp.vendor.swagger_client.api.configuration_api import (
    ConfigurationApi,  # type: ignore[import-untyped]
)
from freeplay_mcp.vendor.swagger_client.api.prompt_templates_api import (
    PromptTemplatesApi,  # type: ignore[import-untyped]
)
from freeplay_mcp.vendor.swagger_client.api.search__analytics_api import (
    SearchAnalyticsApi,  # type: ignore[import-untyped]
)

# Lazy-initialized API clients
_api_client: ApiClient | None = None
_config_api: ConfigurationApi | None = None
_search_api: SearchAnalyticsApi | None = None
_prompt_templates_api: PromptTemplatesApi | None = None


def get_api_client() -> ApiClient:
    """Get or create the Swagger API client."""
    global _api_client
    if _api_client is None:
        api_key = SecretString(os.environ.get("FREEPLAY_API_KEY"))
        if not api_key:
            raise ValueError("FREEPLAY_API_KEY environment variable is required.")

        base_url = os.environ.get(
            "FREEPLAY_BASE_URL", "https://app.freeplay.ai"
        ).rstrip("/")
        verify_ssl_env = os.environ.get("FREEPLAY_VERIFY_SSL", "").lower()
        verify_ssl = verify_ssl_env not in ("false", "0", "no")

        config = Configuration()
        config.host = base_url
        config.verify_ssl = verify_ssl
        # Set up Bearer auth - use .get() to access the actual key value
        _api_client = ApiClient(
            config, header_name="Authorization", header_value=f"Bearer {api_key.get()}"
        )
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
