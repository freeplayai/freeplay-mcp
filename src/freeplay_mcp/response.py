"""Response types for MCP tools."""

import json
import os

from pydantic import BaseModel

OUTPUT_FORMAT = os.getenv("FREEPLAY_OUTPUT_FORMAT", "text")


class ToolResponse(BaseModel):
    def render(self) -> str:
        if OUTPUT_FORMAT == "json":
            return self.model_dump_json(indent=2)
        return self._render_text()

    def _render_text(self) -> str:
        raise NotImplementedError


class ListItem(BaseModel):
    id: str
    title: str
    lines: list[str] = []


class ListResponse(ToolResponse):
    header: str
    items: list[ListItem]
    has_next: bool = False

    def _render_text(self) -> str:
        if not self.items:
            return f"No {self.header.lower()} found."
        lines = [f"{self.header} (has_next: {self.has_next}):", ""]
        for item in self.items:
            lines.append(f"- {item.title} (ID: {item.id})")
            for line in item.lines:
                lines.append(f"  {line}")
            lines.append("")
        return "\n".join(lines)


class DetailResponse(ToolResponse):
    title: str
    sections: dict[str, str | dict | list]

    def _render_text(self) -> str:
        lines = [self.title, ""]
        for key, value in self.sections.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{key}:")
                lines.append(json.dumps(value, indent=2))
            else:
                lines.append(f"{key}: {value}")
        return "\n".join(lines)


class ActionResponse(ToolResponse):
    message: str
    details: dict[str, str]

    def _render_text(self) -> str:
        lines = [self.message, ""]
        for key, value in self.details.items():
            lines.append(f"{key}: {value}")
        return "\n".join(lines)


class ErrorResponse(ToolResponse):
    error: str

    def _render_text(self) -> str:
        return self.error
