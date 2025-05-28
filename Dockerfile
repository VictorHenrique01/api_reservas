# Usa uma imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY . /app

# Instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta que o Flask irá rodar
EXPOSE 5001

# Comando para iniciar o app
CMD ["python", "main.py"]
