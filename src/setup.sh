#!/bin/sh

OS="$(uname)"
if [ "$OS" = "Linux" ]; then
  # Verificando se o pipenv esta instalado
  if ! command -v pipenv &> /dev/null
  then
    echo "pipenv não está instalado. instalando agora..."
    sudo pip install pipenv
  fi
elif [ "$OS" = "Darwin" ]; then
  # Verificando se o pipenv esta instalado
  if ! command -v pipenv &> /dev/null
  then
    echo "pipenv não está instalado. instalando agora..."
    pip install pipenv
  fi
else
  echo "Esse script só suporta Linux and Mac. Caso vocẽ esteja no Windows, Por favor instalar pipenv."
  exit 1
fi

# psycopg2 fails to install on my machine without manually specifying LDFLAGS for openssl
# using fish shell, for me that's `set -gx LDFLAGS "-L/usr/local/opt/openssl/lib"`
pipenv install --dev

# Verificando se o arquivo .env já contém o conteúdo necessário
if ! grep -q "FLASK_APP=lanchonetedarua.application:create_application" .env; then
  echo "FLASK_APP=lanchonetedarua.application:create_application
  FLASK_ENV=development
  ENV=dev
  DATABASE_URI=postgresql://postgres:Postgres2021!@localhost:5432/postgres" >> .env
fi

# Verificando se o arquivo .env.teste já contém o conteúdo necessário
if ! grep -q "ENV=test" .env.test; then
  echo "ENV=test
  DATABASE_URI=postgresql://postgres:Postgres2021!@localhost:5432/postgres_test" >> .env.test
fi

echo "Run the database migrations!"
echo "lanchonetedarua db create && lanchonetedarua db migrate"
echo "lanchonetedarua db create test && lanchonetedarua db migrate test"  
