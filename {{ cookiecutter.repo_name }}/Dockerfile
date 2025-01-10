# ---------------------
# Base Stage
# ---------------------
FROM python:3.9-slim as base

# 1) Copy everything:
WORKDIR /app
COPY . .

# Install uv if needed
RUN pip install uv

# Build the entire workspace (installs everything into one environment)
RUN uv build --all-packages
    
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
    