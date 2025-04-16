# ---------------------
# Base Stage
# ---------------------
FROM python:{{ cookiecutter.minimum_python_version }}-slim AS base

# The uv installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download the latest uv installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the uv installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Copy everything:
WORKDIR /app
COPY . .

# Create a venv and install dependencies
RUN uv sync

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

{% if cookiecutter.include_fastapi_app|lower in ['yes', 'y'] -%}
# ---------------------
# FastAPI Final
# ---------------------
# Create fast-api runtime
FROM base AS fastapi
CMD ["uvicorn", "app_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
{% endif -%}

{% if cookiecutter.include_streamlit_app|lower in ['yes', 'y'] -%}
# ---------------------
# Streamlit Final
# ---------------------
# Create streamlit runtime
FROM base AS streamlit
CMD ["streamlit", "run", "packages/app_streamlit/src/app_streamlit/app.py", "--server.port=8501"]
{% endif -%}

{% if cookiecutter.azure_ml_project|lower in ['yes', 'y'] -%}
# ---------------------
# AzureML Final
# ---------------------
# Create AzureML runtime
FROM base AS azureml
CMD ["bash"]
{% endif -%}
    