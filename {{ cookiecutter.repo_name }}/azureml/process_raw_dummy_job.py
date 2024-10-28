import os
from dotenv import load_dotenv
from azure.ai.ml import command
from azure.ai.ml.constants import AssetTypes, InputOutputModes
from azure.ai.ml import Input, Output

from {{ cookiecutter.package_name }}.utils.azure_ml import get_ml_client, get_datastore_path

load_dotenv(override=True)

ml_client = get_ml_client()
raw_data_version = os.getenv("RAW_DATA_VERSION")
input_asset = ""

env_name = ""
env_version = ""

input_path = f"azureml:{input_asset}:{raw_data_version}"

output_path = get_datastore_path(version=raw_data_version, directory="02_processed")

env_vars = {
    "ENV": "production",
    "SUBSCRIPTION_ID": os.getenv("SUBSCRIPTION_ID"),
    "RESOURCE_GROUP_NAME": os.getenv("RESOURCE_GROUP_NAME"),
    "WORKSPACE_NAME": os.getenv("WORKSPACE_NAME"),
    "RAW_DATA_VERSION": os.getenv("RAW_DATA_VERSION"),
}

# Define the command job
job = command(
    code="azureml/",
    command="python process_raw_dummy.py --input_path ${{ "{{" }}inputs.input_path{{ "}}" }} "
    "--output_path ${{ "{{" }}outputs.output_path{{ "}}" }}",
    inputs={
        "input_path": Input(
            type=AssetTypes.URI_FOLDER,
            path=input_path,
            mode=InputOutputModes.DOWNLOAD,
        ),
    },
    outputs={
        "output_path": Output(
            type=AssetTypes.URI_FOLDER,
            path=output_path,
            mode=InputOutputModes.UPLOAD,
        ),
    },
    environment=f"{env_name}@{env_version}",
    environment_variables=env_vars,
    compute=os.getenv("COMPUTE_RESOURCE"),
    display_name="dummy-processing",
    description="Dummy processing job.",
)

# Submit the job
ml_client.jobs.create_or_update(job)
