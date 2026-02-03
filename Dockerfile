# syntax=docker/dockerfile:1.7-labs
# Use the Chainguard Python image for building
# Note that in order to use this image locally, you'll need to set up a Chainguard pull token at https://console.chainguard.dev/org/freeplay.ai/settings/pull-tokens
# After you've set up a pull token, you'll need to use it to authenticate:
# docker login cgr.dev --username "your_pull_token_username" --password-stdin

FROM cgr.dev/freeplay.ai/python:latest-dev AS builder

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
COPY --chown=nonroot:nonroot src ./src
COPY --chown=nonroot:nonroot swagger ./swagger

# chown ensures the production container can read packages when running as nonroot (UID 65532)
RUN python -m uv sync --locked --no-group dev --no-editable && \
    rm -rf /home/nonroot/.cache/uv && \
    chown -R 65532:65532 /opt/pysetup/.venv


FROM cgr.dev/freeplay.ai/python:latest AS production

ENV PATH="/opt/pysetup/.venv/bin:$PATH"

COPY --from=builder --chown=65532:65532 /opt/pysetup /opt/pysetup

COPY --chown=nonroot:nonroot --parents \
    ./pyproject.toml \
    ./main.py \
    ./src ./swagger \
    /app/

WORKDIR /app

ENTRYPOINT ["/opt/pysetup/.venv/bin/python"]
CMD ["/app/main.py"]
