FROM python:3.9-slim-buster

# Install the uv package
RUN pip install uv

# Set the working directory in the container
WORKDIR /app

# Copy required files to the container
COPY .streamlit .streamlit
COPY src src
COPY assets assets
COPY app_streamlit/pyproject.toml pyproject.toml
COPY app_streamlit/app.py app.py
COPY app_streamlit/style.css style.css

# Install the required packages and create venv
RUN uv sync

# Expose the port
EXPOSE 8501

# Place executable in the env
ENV PATH="/app/.venv/bin:$PATH"

# Run the streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
