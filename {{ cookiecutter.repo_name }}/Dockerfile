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
RUN uv build --all-packages

# Create a venv and install dependencies
RUN uv sync

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"
    
# ---------------------
# FastAPI Final
# ---------------------
FROM base as fastapi
CMD ["uvicorn", "app_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
        
# ---------------------
# Streamlit Final
# ---------------------
FROM base as streamlit
CMD ["streamlit", "run", "app_streamlit/app.py", "--server.port=8501"]
    