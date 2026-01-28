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

    async def search_completions(
        self,
        project_id: str,
        query: str | None = None,
        limit: int = 20,
        offset: int = 0,
        start_date: str | None = None,
        end_date: str | None = None,
        environment: str | None = None,
        template_name: str | None = None,
    ) -> dict[str, Any]:
        """Search completions in a project."""
        # Build filters based on provided criteria
        filter_conditions: list[dict[str, Any]] = []

        if start_date is not None:
            filter_conditions.append({
                "field": "completion_metadata.start_time",
                "op": "gte",
                "value": start_date,
            })
        if end_date is not None:
            filter_conditions.append({
                "field": "completion_metadata.start_time",
                "op": "lte",
                "value": end_date,
            })
        if environment is not None:
            filter_conditions.append({
                "field": "completion_metadata.environment",
                "op": "eq",
                "value": environment,
            })
        if template_name is not None:
            filter_conditions.append({
                "field": "completion_metadata.prompt_template.name",
                "op": "eq",
                "value": template_name,
            })

        # Construct the filters object
        if len(filter_conditions) == 0:
            filters: dict[str, Any] = {}
        elif len(filter_conditions) == 1:
            filters = filter_conditions[0]
        else:
            filters = {"and": filter_conditions}

        body: dict[str, Any] = {"filters": filters}

        # Convert limit/offset to page/page_size
        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1

        return await self._request(
            "POST",
            f"/api/v2/projects/{project_id}/search/completions",
            json=body,
            params={"page": page, "page_size": page_size},
        )
