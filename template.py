import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: [%(message)s]:')
project_name = "CNnClassifier"
base_directory = ""  # Replace with your desired directory path

list_of_files = [
    os.path.join(".github", "workflows", ".gitkeep"),
    os.path.join("src", project_name, "__init__.py"),
    os.path.join("src", project_name, "components", "__init__.py"),
    os.path.join("src", project_name, "utils", "__init__.py"),
    os.path.join("src", project_name, "config", "__init__.py"),
    os.path.join("src", project_name, "config", "configuration.py"),
    os.path.join("src", project_name, "pipeline", "__init__.py"),
    os.path.join("src", project_name, "entity", "__init__.py"),
    os.path.join("src", project_name, "constants", "__init__.py"),
    "config", "config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research", "trials.ipynb"
]

for filepath in list_of_files:
    filepath = os.path.join(base_directory, filepath)  # Build the full path
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        try:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
        except PermissionError as e:
            logging.error(f"Permission denied: {str(e)}")
    else:
        logging.info(f"{filename} already exists")
