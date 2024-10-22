import os
import shutil

include_streamlit_app = "{{cookiecutter.include_streamlit_app}}"
include_fastapi_app = "{{cookiecutter.include_fastapi_app}}"
azure_ml_project = "{{cookiecutter.azure_ml_project}}"

proj_path = os.getcwd()
utils_dir = os.path.join(proj_path, "src", "{{cookiecutter.package_name}}", "utils")

# Remove unnecessary app templates
if include_streamlit_app.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(proj_path, 'app_streamlit'))
    shutil.rmtree(os.path.join(proj_path, 'assets'))
    shutil.rmtree(os.path.join(proj_path, '.streamlit'))

if include_fastapi_app.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(proj_path, 'app_fastapi'))

if azure_ml_project.lower() not in ['yes', 'y']:
    shutil.rmtree(os.path.join(proj_path, 'azureml'))
    shutil.rmtree(os.path.join(proj_path, 'data', '01_raw'))
    shutil.rmtree(os.path.join(proj_path, 'data', '02_intermediate'))
    shutil.rmtree(os.path.join(proj_path, 'data', '03_model_input'))
    shutil.rmtree(os.path.join(proj_path, 'data', '04_model_output'))

# Remove unnecessary utility functions
if "{{cookiecutter.database_type}}" == 'none':
    os.remove(os.path.join(utils_dir, "db.py"))
