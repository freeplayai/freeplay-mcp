.PHONY: type-check
type-check:
	uv run basedpyright src/

.PHONY: lint
lint:
	uv run ruff format src/ && uv run ruff check --fix src/

# ONLY use this in CI. Locally, make it always do the fix.
.PHONY: lint-check
lint-check:
	uv run ruff format --check src/ && uv run ruff check src/

.PHONY: check
check: type-check lint-check

.PHONY: build
build:
	rm -rf dist/*
	uv build
