# https://www.kaggle.com/datasets/laotse/credit-risk-dataset
import kagglehub
import os
import pandas as pd
import shutil
from pathlib import Path

def load_raw_data(filename="credit_risk_dataset.csv", output="data/raw"):
    #base_dir = Path(__file__).resolve().parent.parent.parent
    current_file = Path(__file__).resolve()
    src_folder = current_file.parent
    base_dir = src_folder.parent

    # Custom path
    custom_path = os.path.join(base_dir, output)

    # Custom file
    file_path_destiny = os.path.join(custom_path, filename)

    # Avoid duplicate files
    if os.path.exists(file_path_destiny):
        print("Arquivo já existe, pulando donwload.")
        print(f"Arquivo salvo no projeto {base_dir} em: {custom_path}")

        # Create dataframe
        df = pd.read_csv(file_path_destiny)

        return df

    else:
        # Download latest version
        path = kagglehub.dataset_download("laotse/credit-risk-dataset")
        file_path_origin = os.path.join(path, filename)

        # If directory does't exist, create
        os.makedirs(custom_path, exist_ok=True)

        # Copy file
        shutil.copy(file_path_origin, file_path_destiny)

        print(f"Arquivo primeiramente salvo em: {file_path_origin}")
        print(f"Arquivo copiado e salvo no projeto {base_dir} em: {custom_path}")

        # Create dataframe
        df = pd.read_csv(file_path_destiny)

        return df

def load_custom_data(filename: str, output="data/processed"):
    # __file__ -> variável que contém o caminho do arquivo Python atual que está executado.
    # Path(__file__) -> transforma esse caminho em um objeto Path, que permite manipular diretórios facilmente.
    # .resolve() -> converte o caminho para caminho absoluto real, resolvendo links simbólicos.
    current_file = Path(__file__).resolve()
    # .parent -> retorna a pasta que contém o arquivo
    src_folder = current_file.parent
    # .parent -> retorna a pasta que contém o arquivo
    base_dir = src_folder.parent

    # Custom path
    custom_path = os.path.join(base_dir, output)

    # Custom file
    file_path_destiny = os.path.join(custom_path, filename)

    if os.path.exists(file_path_destiny):
        print(f"Arquivo existe, carregando Dataframe {file_path_destiny}")

        # Create dataframe
        df = pd.read_csv(file_path_destiny)

        return df

    else:
        print("Arquivo inexistente, favor gerar o arquivo antes de carregar.")