import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s:")

project_name = "PostHoc-XAI"

list_of_files = [
    f"project_root/notebooks/01_data_preprocessing.ipynb",
    f"project_root/notebooks/02_framework_design.ipynb",
    f"project_root/notebooks/03_xai_techniques_implementation.ipynb",
    f"project_root/notebooks/04_strategic_bias_mitigation.ipynb",
    f"project_root/notebooks/05_quantitative_evaluation.ipynb",
    f"project_root/notebooks/06_cross_domain_generalization.ipynb",
    f"project_root/notebooks/07_practical_deployment_recommendations.ipynb",
    f"project_root/notebooks/08_ethical_ai_practices.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
