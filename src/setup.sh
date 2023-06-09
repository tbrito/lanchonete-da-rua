#!/bin/sh

# psycopg2 fails to install on my machine without manually specifying LDFLAGS for openssl
# using fish shell, for me that's `set -gx LDFLAGS "-L/usr/local/opt/openssl/lib"`
pipenv install --dev

echo "FLASK_APP=lanchonetedarua.application:create_application
FLASK_ENV=development
ENV=dev
DATABASE_URI=postgresql://postgres:Postgres2021!@localhost:5432/postgres" >> .env

echo "ENV=test
DATABASE_URI=postgresql://postgres:Postgres2021!@localhost:5432/postgres_test" >> .env.test

echo "Run the database migrations!"
echo "lanchonetedarua db create && lanchonetedarua db migrate"
echo "lanchonetedarua db create test && lanchonetedarua db migrate test"