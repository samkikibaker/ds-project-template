from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv(override=True)

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World", "Project": "{{cookiecutter.project_name}}"}
