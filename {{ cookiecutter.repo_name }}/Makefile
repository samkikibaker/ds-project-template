# Makefile for {{cookiecutter.project_name}}

.PHONY: install
install:
	git init
	pip install uv
	uv sync
	pre-commit install

{% if cookiecutter.azure_ml_project|lower in ['yes', 'y'] -%}

.PHONY: data-sync-raw
data-sync-raw:
	python -m {{cookiecutter.package_name}}.utils.azure_ml {{cookiecutter.package_name}}-raw $(version) data/01_raw/

.PHONY: aml-env-build
aml-env-build:
	docker build -f azureml/Dockerfile -t {{cookiecutter.repo_name}}_env .

.PHONY: aml-env-push
aml-env-push:
	docker tag {{cookiecutter.repo_name}}_env ${CONTAINER_REGISTRY}/{{cookiecutter.repo_name}}_env:1
	docker push ${CONTAINER_REGISTRY}/{{cookiecutter.repo_name}}_env:1

{% endif -%}
{% if cookiecutter.include_streamlit_app|lower in ['yes', 'y'] -%}

.PHONY: streamlit-build
streamlit-build:
	docker build -f app_streamlit/Dockerfile -t {{cookiecutter.repo_name}}_webapp .

.PHONY: streamlit-run
streamlit-run:
	docker run -p 8501:8501 {{cookiecutter.repo_name}}_webapp

{% endif -%}
{% if cookiecutter.include_fastapi_app|lower in ['yes', 'y'] -%}

.PHONY: fastapi-build
fastapi-build:
	docker build -f app_fastapi/Dockerfile -t {{cookiecutter.repo_name}}_api .

.PHONY: fastapi-run
fastapi-run:
	docker run -p 8000:8000 {{cookiecutter.repo_name}}_api

{% endif -%}

.PHONY: test
test: install
	coverage run -m pytest
	coverage report -m

.PHONY: test-html
test_html: test
	python -m http.server --directory htmlcov/

.PHONY: ruff-fix
ruff-fix:
	ruff check --fix

.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete