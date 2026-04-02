# Import para visualizar as pastas
import os
import sys

import matplotlib.pyplot as plt
import seaborn as sns

# Adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from pathlib import Path

# Caminho onde serão salvo os resultados rsults/eda
results_path = Path("../results/eda")
results_path.mkdir(exist_ok=True)

# Gerando mapa de calor (apenas colunas numéricas)
def geraMapaCalor(dataframe, i = None):
    plt.figure(figsize=(18,15))
    sns.heatmap(dataframe.corr(numeric_only=True), cmap=('Blues'), annot=True)
    plt.title('Correlação entre os atributos', size=20)
    plt.xticks(rotation=45)

    # Se i = 1, salvará o mapa de calor na pasta result/eda/mapa_calor.png
    # Senão apenas mostrará na saída o gráfico
    if i == 1:
        file_name = results_path / 'mapa_calor.png'
        plt.savefig(file_name)
        plt.close()
        print(f'Imagem salva em {file_name}')

    elif i == None:
        plt.show()