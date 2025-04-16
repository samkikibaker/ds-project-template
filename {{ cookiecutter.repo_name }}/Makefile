# Makefile for {{cookiecutter.project_name}}

SHELL := /bin/bash

.PHONY: install
setup:
	# Install uv globally
	curl -LsSf https://astral.sh/uv/install.sh | sh

	# Create a virtual environment
	uv venv

	# Install project dependencies
	uv pip install -e .

	# Install pre-commit hooks
	source .venv/bin/activate && pre-commit install

{% if cookiecutter.azure_ml_project|lower in ['yes', 'y'] -%}

.PHONY: data-sync-raw
data-sync-raw:
	python -m {{cookiecutter.package_name}}.utils.azure_ml {{cookiecutter.package_name}}-raw $(version) data/01_raw/

.PHONY: aml-env-build
aml-env-build:
	docker build \
	-f Dockerfile \
	--target azureml \
	-t {{cookiecutter.repo_name}}_env \
	.

.PHONY: aml-env-push
aml-env-push:
	docker tag {{cookiecutter.repo_name}}_env ${CONTAINER_REGISTRY}/{{cookiecutter.repo_name}}_env:1
	docker push ${CONTAINER_REGISTRY}/{{cookiecutter.repo_name}}_env:1

{% endif -%}
{% if cookiecutter.include_streamlit_app|lower in ['yes', 'y'] -%}

.PHONY: streamlit-build
streamlit-build:
	docker build \
		-f Dockerfile \
		--target streamlit \
		-t {{cookiecutter.repo_name}}_webapp \
		.

.PHONY: streamlit-run
streamlit-run:
	docker run -p 8501:8501 {{cookiecutter.repo_name}}_webapp

.PHONY: kill-streamlit
kill-streamlit:
	kill -9 $(lsof -t -i:8501)

{% endif -%}
{% if cookiecutter.include_fastapi_app|lower in ['yes', 'y'] -%}

.PHONY: fastapi-build
fastapi-build:
	docker build \
		-f Dockerfile \
		--target fastapi \
		-t {{cookiecutter.repo_name}}_api \
		.

.PHONY: fastapi-run
fastapi-run:
	docker run -p 8000:8000 {{cookiecutter.repo_name}}_api

.PHONY: kill-fastapi
kill-fastapi:
	kill -9 $(lsof -t -i:8000)

{% endif -%}


{% if cookiecutter.dev_dependencies|lower in ['yes', 'y'] -%}
.PHONY: test
test: install
	coverage run -m pytest
	coverage report -m

.PHONY: ruff
ruff:
	# Run ruff
	uv run ruff format
{% endif -%}