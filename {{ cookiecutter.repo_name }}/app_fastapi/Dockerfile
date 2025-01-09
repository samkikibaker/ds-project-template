FROM python:3.9-slim

# Install the uv package
RUN pip install uv

# Set the working directory in the container
WORKDIR /app

# Copy relevant files to the container
COPY src src
COPY app_fastapi/pyproject.toml pyproject.toml
COPY app_fastapi/main.py main.py

# Install dependencies from the pyproject.toml file
RUN uv sync

# Expose the port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
