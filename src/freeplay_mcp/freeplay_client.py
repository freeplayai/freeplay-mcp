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

    def _build_filters(
        self,
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
    ) -> dict[str, Any]:
        """Build filter conditions for search endpoints."""
        filter_conditions: list[dict[str, Any]] = []

        # Date/time filters
        if start_date is not None:
            start_value = start_date if " " in start_date else f"{start_date} 00:00:00"
            filter_conditions.append({
                "field": "start_time",
                "op": "gte",
                "value": start_value,
            })
        if end_date is not None:
            end_value = end_date if " " in end_date else f"{end_date} 23:59:59"
            filter_conditions.append({
                "field": "start_time",
                "op": "lte",
                "value": end_value,
            })

        # Equality filters
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
                filter_conditions.append({
                    "field": field,
                    "op": "eq",
                    "value": value,
                })

        # Range filters (cost)
        if cost_min is not None:
            filter_conditions.append({
                "field": "cost",
                "op": "gte",
                "value": cost_min,
            })
        if cost_max is not None:
            filter_conditions.append({
                "field": "cost",
                "op": "lte",
                "value": cost_max,
            })

        # Range filters (latency)
        if latency_min is not None:
            filter_conditions.append({
                "field": "latency",
                "op": "gte",
                "value": latency_min,
            })
        if latency_max is not None:
            filter_conditions.append({
                "field": "latency",
                "op": "lte",
                "value": latency_max,
            })

        # Construct the filters object
        if len(filter_conditions) == 0:
            return {}
        elif len(filter_conditions) == 1:
            return filter_conditions[0]
        else:
            return {"and": filter_conditions}

    async def search_completions(
        self,
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
    ) -> dict[str, Any]:
        """Search completions in a project."""
        filters = self._build_filters(
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
            prompt_template_id=prompt_template_id,
            model=model,
            provider=provider,
            session_id=session_id,
            completion_id=completion_id,
            agent_name=agent_name,
            review_status=review_status,
            cost_min=cost_min,
            cost_max=cost_max,
            latency_min=latency_min,
            latency_max=latency_max,
        )

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

    async def search_traces(
        self,
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
        agent_name: str | None = None,
        review_status: str | None = None,
        cost_min: float | None = None,
        cost_max: float | None = None,
        latency_min: float | None = None,
        latency_max: float | None = None,
    ) -> dict[str, Any]:
        """Search traces in a project."""
        filters = self._build_filters(
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
            prompt_template_id=prompt_template_id,
            model=model,
            provider=provider,
            session_id=session_id,
            agent_name=agent_name,
            review_status=review_status,
            cost_min=cost_min,
            cost_max=cost_max,
            latency_min=latency_min,
            latency_max=latency_max,
        )

        body: dict[str, Any] = {"filters": filters}

        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1

        return await self._request(
            "POST",
            f"/api/v2/projects/{project_id}/search/traces",
            json=body,
            params={"page": page, "page_size": page_size},
        )

    async def search_sessions(
        self,
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
        agent_name: str | None = None,
        review_status: str | None = None,
        cost_min: float | None = None,
        cost_max: float | None = None,
        latency_min: float | None = None,
        latency_max: float | None = None,
    ) -> dict[str, Any]:
        """Search sessions in a project."""
        filters = self._build_filters(
            start_date=start_date,
            end_date=end_date,
            environment=environment,
            template_name=template_name,
            prompt_template_id=prompt_template_id,
            model=model,
            provider=provider,
            session_id=session_id,
            agent_name=agent_name,
            review_status=review_status,
            cost_min=cost_min,
            cost_max=cost_max,
            latency_min=latency_min,
            latency_max=latency_max,
        )

        body: dict[str, Any] = {"filters": filters}

        page_size = limit
        page = (offset // limit) + 1 if limit > 0 else 1

        return await self._request(
            "POST",
            f"/api/v2/projects/{project_id}/search/sessions",
            json=body,
            params={"page": page, "page_size": page_size},
        )
