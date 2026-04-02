# Salvando o novo dataframe em data/processed
# Import para visualizar as pastas
from pathlib import Path

def save_new_df(file_name: str, new_dataframe):
    new_path_data = Path("../data/processed")
    new_path_data.mkdir(exist_ok=True)
    file_name = file_name
    file_path = new_path_data / file_name

    new_dataframe.to_csv(file_path, index=False)

    retorno = (f'Novo dataframe {file_name} salvo em {file_path}')

    return retorno