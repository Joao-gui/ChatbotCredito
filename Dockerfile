# Imagem base
FROM python:3.14.3

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