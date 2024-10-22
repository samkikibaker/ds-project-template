import os
import shutil
import argparse
import azure.ai.ml._artifacts._artifact_utilities as artifact_utils

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential


def get_ml_client() -> MLClient:
    ml_client = MLClient(
        credential=DefaultAzureCredential(),
        subscription_id=os.getenv("SUBSCRIPTION_ID"),
        resource_group_name=os.getenv("RESOURCE_GROUP_NAME"),
        workspace_name=os.getenv("WORKSPACE_NAME"),
    )

    return ml_client


def get_datastore_path(directory: str, version: str) -> str:
    if directory[-1] == "/":
        directory = directory[:-1]

    path = "azureml://"
    path += f"subscriptions/{os.getenv('SUBSCRIPTION_ID')}/"
    path += f"resourcegroups/{os.getenv('RESOURCE_GROUP_NAME')}/"
    path += f"workspaces/{os.getenv('WORKSPACE_NAME')}/"
    path += "datastores/workspaceblobstore/"
    path += f"paths/{os.getenv('PROJECT_NAME')}/"
    path += f"{directory}/{version}/"

    return path


def sync_data_local(asset: str, version: str, out_path: str) -> None:
    ml_client = get_ml_client()
    asset = ml_client.data.get(name=asset, version=version)

    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    os.makedirs(out_path)

    artifact_utils.download_artifact_from_aml_uri(
        uri=asset.path, destination=out_path, datastore_operation=ml_client.datastores
    )


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("asset", type=str, help="Name of the asset to sync.")
    parser.add_argument("version", type=str, help="Version of the asset to sync.")
    parser.add_argument("out_path", type=str, help="Output path for the synced data.")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    sync_data_local(asset=args.asset, version=args.version, out_path=args.out_path)
