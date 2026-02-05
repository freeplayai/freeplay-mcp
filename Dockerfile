# syntax=docker/dockerfile:1.7-labs

FROM python:3.12-slim AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

RUN pip install uv

WORKDIR $PYSETUP_PATH

COPY pyproject.toml uv.lock README.md ./
COPY src ./src
COPY swagger ./swagger

RUN python -m uv sync --locked --no-group dev --no-editable && \
    rm -rf /root/.cache/uv


FROM python:3.12-slim AS production

RUN groupadd --gid 65532 nonroot && \
    useradd --uid 65532 --gid 65532 --no-create-home nonroot

ENV PATH="/opt/pysetup/.venv/bin:$PATH"

COPY --from=builder --chown=65532:65532 /opt/pysetup /opt/pysetup

COPY --chown=65532:65532 --parents \
    ./pyproject.toml \
    ./main.py \
    ./src ./swagger \
    /app/

WORKDIR /app

USER nonroot

ENTRYPOINT ["/opt/pysetup/.venv/bin/python"]
CMD ["/app/main.py"]
