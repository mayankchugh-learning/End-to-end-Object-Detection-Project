import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')   

project_name = "signLanguage"

list_of_files = [

    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/data_loader.py",
    f"{project_name}/data/data_processor.py",
    f"{project_name}/data/data_splitter.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/traning_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/traning_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "Dockerfile",
    "README.md",
    "requirements.txt",
    "app.py",
    "setup.py"

]


for filepath in list_of_files:

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename}")

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass
            logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"File {filename} already exists")