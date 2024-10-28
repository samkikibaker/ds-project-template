FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update -y && apt-get install -y gcc
RUN pip install -U pip setuptools wheel

COPY src src
COPY pyproject.toml pyproject.toml
RUN pip install .

CMD ["bash"]