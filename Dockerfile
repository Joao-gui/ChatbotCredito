# Imagem base
FROM python:3.11-slim

# Diretório dentro do container
WORKDIR /app

# Copiar dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar projeto
COPY . .

# Porta padrão
EXPOSE 8000

# 🚀 COMANDO PARA RODAR A API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]