from dotenv import load_dotenv

from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

from {{ cookiecutter.package_name }}.utils.util import yaml2dict
from {{ cookiecutter.package_name }}.utils.azure_ml import get_ml_client, get_datastore_path

load_dotenv(override=True)
azureml_config = yaml2dict("azureml/azureml_config.yaml")

ml_client = get_ml_client()

for data_asset in azureml_config["data_assets"]:
    for version in data_asset["versions"]:
        azure_path = get_datastore_path(
            version=str(version["version"]), directory=version["path"]
        )

        my_data = Data(
            path=azure_path,
            type=AssetTypes.URI_FOLDER,
            description=version["description"],
            name=data_asset["name"],
            version=str(version["version"]),
        )

        ml_client.data.create_or_update(my_data)
