#!/bin/bash
# init-db.sh

# Esperar a que la base de datos esté disponible
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "Esperando a que la base de datos esté disponible..."
  sleep 2
done

# Ejecutar migraciones
alembic upgrade head
