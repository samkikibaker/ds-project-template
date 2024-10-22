import os
from dotenv import load_dotenv
from azure.ai.ml.entities import Environment

from {{ cookiecutter.package_name}}.utils.util import yaml2dict
from {{ cookiecutter.package_name }}.utils.azure_ml import get_ml_client

load_dotenv(override=True)
azureml_config = yaml2dict("azureml/azureml_config.yaml")

ml_client = get_ml_client()

for environment in azureml_config["environments"]:
    for version in environment["versions"]:
        image_name = f"{os.getenv('CONTAINER_REGISTRY')}/{version['image']}"

        my_env = Environment(
            name=environment["name"],
            description=version["description"],
            image=image_name,
            version=str(version["version"]),
        )

        ml_client.environments.create_or_update(my_env)
