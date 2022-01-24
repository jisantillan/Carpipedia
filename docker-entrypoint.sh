#!/bin/bash

echo "Recolectando archivos estáticos"
python manage.py collectstatic --noinput

echo "Aplicar migraciones de la base de datos"
python manage.py migrate

echo "Corriendo server..."
python manage.py runserver 0.0.0.0:8000