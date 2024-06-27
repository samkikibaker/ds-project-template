# Hoare Lea Data Science Project Template
A standardised project structure for doing and sharing data science work that enforces best practices. This template includes useful boilerplate code for Hoare Lea projects including:
* Hoare Lea fonts, colors, logos and css styles added to streamlit apps by default
* Utility functions for generating plotly data visualisations in the Hoare Lea style
* Utility functions for connecting to company data sources (FUTURE)

The goal of this template is to maintain modularity and separation of concerns:
- **Shared Code**: All reusable code should reside in the `src` directory.
- **Apps, Pipelines, and Notebooks**: Use the shared code in apps, pipelines, and notebooks, ensuring that your project remains clean and maintainable.

## Usage
1. Install cookiecutter.
   ```bash
   pip install cookiecutter
   ```
2. Start a new project. You will be prompted to enter some configuration values.
   ```bash
   cookiecutter gh:HoareLea/ds-project-template
   ```

## Technologies
This project template comes with several tools designed to improve code quality and development efficiency. Some tools are included by default, while others are optional and can be chosen during the setup process.
- **[Jupyter](https://jupyter.org/)**: Jupyter Notebooks are a popular tool for data exploration and communication. They allow you to write and run code in an interactive environment, which is particularly useful for data analysis and visualization. Note that Jupyter is intended for exploration and not for production code.
- **[pytest](https://docs.pytest.org/en/)**: pytest is a testing framework for Python that makes it easy to write simple and scalable test cases. Using pytest helps ensure that your code is working correctly and can catch issues early in the development process.
- **[Docker](https://www.docker.com/)**: Docker is a platform that allows you to create, deploy, and run applications in containers. Containers are lightweight and portable, making it easy to share and run your project in any environment. Including Docker ensures that your project can be consistently run anywhere, from your local machine to a production server.
- **Makefile**: A Makefile is included to simplify running common commands. It helps you automate repetitive tasks, such as setting up your environment, running tests, or building your application. Using a Makefile can save time and reduce the potential for errors.

#### Pre-Commit Hooks
Pre-commit hooks are scripts that run automatically before you make a commit in your version control system (e.g., Git). They help ensure that your code meets certain standards before it is saved to the repository.
- **[Black](https://black.readthedocs.io/en/stable/)**: Black is an opinionated code formatter. It automatically formats your Python code to make it more readable and consistent. By using Black, you can avoid debates about coding style and focus on what the code actually does.
- **[Flake8](https://flake8.pycqa.org/en/latest/)**: Flake8 is a tool for checking the style and quality of Python code. It combines several tools to check for coding errors, enforce coding style, and maintain code quality. Using Flake8 helps catch common mistakes early in the development process.
- **[nbstripout](https://github.com/kynan/nbstripout)**: Nbstripout is a tool to strip output from Jupyter notebooks. This is useful for keeping your version control history clean by removing potentially large and unnecessary output data from the notebooks, making them easier to review and manage.

#### Optional Tools
During the setup process, you can choose to include the following optional tools. If selected, relevant boilerplate code and configuration will be added to your project.
- **[Streamlit](https://streamlit.io/)**: Streamlit is a framework for creating web applications from Python scripts. It is especially useful for creating interactive data applications and dashboards with minimal effort. Including Streamlit allows you to build and share interactive data apps quickly.
- **[FastAPI](https://fastapi.tiangolo.com/)**: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It is designed for creating RESTful APIs easily and efficiently. If you need to expose your models or data processing as APIs, FastAPI is a great choice.
- **[Prefect](https://www.prefect.io/)**: Prefect is a workflow management tool for building, scheduling, and monitoring data pipelines. It helps you automate and manage data workflows, ensuring that tasks run in the correct order and handle failures gracefully. Prefect is useful for managing complex data workflows and ensuring reliable data processing.
- **Cloud Storage Connections**: You can choose to create connections to one of the three main cloud providers (AWS, Azure, or GCP). If selected, helper functions will be created in the `utils` section of the local package. Just update the `.env` file with the relevant secrets to enable these connections.
- **Database Connections**: You can choose to connect to PostgreSQL or MySQL databases. If selected, helper functions will be created in the `utils` section of the local package. Update the `.env` file with the relevant database connection details to use these functions.

## Project Structure
The directory structure of your new project looks like this:
```
├── .env                   <- Local secrets and credentials that should not be stored in source control.
├── Makefile               <- Makefile with useful commands for project setup and running analysis.
├── README.md              <- The top-level README for developers using this project.
├── app                    <- App-specific code, requirements file and Dockerfile.
├── conf                   <- Configuration files that can be stored in source control.
├── data
│   ├── 01_raw             <- The original, immutable data dump.
│   ├── 02_intermediate    <- Intermediate data that has been transformed.
│   ├── 03_model_input     <- The final, canonical data sets for modeling.
│   └── 04_model_output    <- Outputs from models (e.g. predictions).
├── models                 <- Trained and serialized models or model summaries.
├── notebooks              <- Jupyter notebooks.
├── pipelines              <- Pipeline scripts for data processing and model training.
├── pyproject.toml         <- Project metadata and dependencies.
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── src                    <- Source code for use in this project.
│   └── package
│       ├── __init__.py    <- Make package a Python module.
│       ├── data           <- Scripts to download or generate data.
│       ├── features       <- Scripts to turn raw data into features for modeling.
│       ├── model          <- Scripts to train models and make predictions.
│       ├── utils          <- Utility functions.
│       └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
└── tests                  <- Tests for functions in src.
```
