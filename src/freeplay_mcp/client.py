"""Freeplay API client with authentication handling."""

import os
import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)


class FreeplayClient:
    """Async client for the Freeplay API."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        verify_ssl: bool | None = None,
    ):
        self.api_key = api_key or os.environ.get("FREEPLAY_API_KEY")
        if not self.api_key:
            raise ValueError(
                "FREEPLAY_API_KEY environment variable is required. "
                "Set it or pass api_key to the client."
            )

        self.base_url = (
            base_url
            or os.environ.get("FREEPLAY_BASE_URL", "https://app.freeplay.ai")
        ).rstrip("/")

        # SSL verification: explicit param > env var > default (True)
        if verify_ssl is not None:
            self.verify_ssl = verify_ssl
        else:
            env_val = os.environ.get("FREEPLAY_VERIFY_SSL", "").lower()
            self.verify_ssl = env_val not in ("false", "0", "no")

        self._client: httpx.AsyncClient | None = None

    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                timeout=30.0,
                verify=self.verify_ssl,
            )
        return self._client

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Make an authenticated request to the Freeplay API."""
        response = await self.client.request(method, path, **kwargs)
        response.raise_for_status()
        return response.json()

    async def list_projects(self) -> list[dict[str, Any]]:
        """List all projects accessible to the authenticated user."""
        data = await self._request("GET", "/api/v2/projects/all")
        return data.get("projects", data) if isinstance(data, dict) else data
