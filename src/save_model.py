# Import para visualizar as pastas
import os
import sys
from pathlib import Path

# Adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

import joblib

def save_model(file_name: str, grid_search, path='models'):

    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent

    model_dir = project_root / path
    model_dir.mkdir(parents=True, exist_ok=True)

    file_path = model_dir / file_name

    joblib.dump(grid_search.best_estimator_, file_path)

    print(f"Modelo salvo em: {file_path}")