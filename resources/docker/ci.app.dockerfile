FROM python:3.12-slim

WORKDIR /app

COPY uv.lock pyproject.toml ./

RUN pip install --no-cache-dir uv \
    && uv venv \
    && uv sync --group app --group local

ENTRYPOINT ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
