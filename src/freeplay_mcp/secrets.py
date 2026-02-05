"""Utilities for secure handling of API keys and secrets."""

import re


class SecretString:
    """A string wrapper that prevents accidental exposure in logs/prints.

    When printed or converted to string representation, shows "[REDACTED]"
    instead of the actual value. Use .get() to access the real value.

    Example:
        api_key = SecretString(os.environ.get("FREEPLAY_API_KEY"))
        print(api_key)  # Output: [REDACTED]
        headers = {"Authorization": f"Bearer {api_key.get()}"}  # Uses real value
    """

    def __init__(self, value: str | None):
        self._value = value

    def get(self) -> str | None:
        return self._value

    def __str__(self) -> str:
        return "[REDACTED]" if self._value else ""

    def __repr__(self) -> str:
        return "SecretString([REDACTED])" if self._value else "SecretString(None)"

    def __bool__(self) -> bool:
        return bool(self._value)


_SECRET_PATTERNS = [
    (re.compile(r'(Bearer\s+)[A-Za-z0-9_\-\.]+', re.IGNORECASE), r'\1[REDACTED]'),
    (re.compile(r'(Authorization["\']?\s*:\s*["\']?)[^"\'}\s]+', re.IGNORECASE), r'\1[REDACTED]'),
    (re.compile(r'(api[_-]?key["\']?\s*[:=]\s*["\']?)[A-Za-z0-9_\-\.]+', re.IGNORECASE), r'\1[REDACTED]'),
    (re.compile(r'(secret["\']?\s*[:=]\s*["\']?)[A-Za-z0-9_\-\.]+', re.IGNORECASE), r'\1[REDACTED]'),
    (re.compile(r'(token["\']?\s*[:=]\s*["\']?)[A-Za-z0-9_\-\.]+', re.IGNORECASE), r'\1[REDACTED]'),
    (re.compile(r'(FREEPLAY_API_KEY\s*=\s*)[^\s]+', re.IGNORECASE), r'\1[REDACTED]'),
]


def redact_secrets(text: str) -> str:
    """Remove potential secrets from text before logging."""
    result = text
    for pattern, replacement in _SECRET_PATTERNS:
        result = pattern.sub(replacement, result)
    return result
