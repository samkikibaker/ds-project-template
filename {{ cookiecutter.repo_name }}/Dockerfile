# ---------------------
# Base Stage
# ---------------------
FROM python:3.9-slim as base

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

# Build the entire workspace
RUN uv build {{cookiecutter.package_name}}

# Create a venv and install dependencies
RUN uv sync

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

{% if cookiecutter.include_fastapi_app.lower() in ['yes', 'y'] -%}
# ---------------------
# FastAPI Final
# ---------------------
    FROM base as fastapi
    RUN uv build app_fastapi
    CMD ["uvicorn", "app_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
{% endif -%}

{% if cookiecutter.include_streamlit_app.lower() in ['yes', 'y'] -%}
# ---------------------
# Streamlit Final
# ---------------------
    FROM base as streamlit
    RUN uv build app_streamlit
    CMD ["streamlit", "run", "packages/app_streamlit/src/app_streamlit/app.py", "--server.port=8501"]
{% endif -%}

{% if cookiecutter.azure_ml_project.lower() in ['yes', 'y'] -%}
# ---------------------
# AzureML Final
# ---------------------
    FROM base as azureml
    RUN uv build azureml
    CMD ["bash"]
{% endif -%}    
    