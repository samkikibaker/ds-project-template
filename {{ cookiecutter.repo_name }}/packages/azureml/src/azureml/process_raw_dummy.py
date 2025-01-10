import os
import argparse
from {{ cookiecutter.package_name }}.utils.util import yaml2dict

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, required=True)
parser.add_argument("--output_path", type=str, required=True)
args = parser.parse_args()

# Input and output paths
input_path = args.input_path
output_path = args.output_path

if os.getenv("ENV", "development") == "production":
    params = yaml2dict("/app/conf/parameters.yaml")
else:
    params = yaml2dict("conf/parameters.yaml")

# Do something with the input data
