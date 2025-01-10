FROM python:3.9-slim-buster

# Install the uv package
RUN pip install uv

# Set the working directory in the container
WORKDIR /app

COPY src src
COPY azureml/pyproject.toml pyproject.toml

RUN uv sync

# Place executable in the env
ENV PATH="/app/.venv/bin:$PATH"

CMD ["bash"]