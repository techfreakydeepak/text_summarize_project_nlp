import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "Dockerfile",
    "app.py",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "README.md",
    "setup.py",
    "main.py",
    "reasearch/trails.ipynb",
]

for filepath in list_of_files:
    dirpath = os.path.dirname(filepath)
    
    # Only create directories if dirpath is not empty
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
