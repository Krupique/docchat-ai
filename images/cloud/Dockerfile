# Use a base image com suporte a AWS Lambda
FROM public.ecr.aws/lambda/python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Instale o Poetry no sistema global
RUN pip install --no-cache-dir poetry

# Defina o diretório de trabalho
WORKDIR /var/task

# Copie os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./ 

# Instale as dependências (sem criar ambientes virtuais)
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copie o código da aplicação
COPY . .

# Defina o handler da aplicação (ajuste conforme necessário)
CMD ["src.main_lambda.lambda_handler"]
