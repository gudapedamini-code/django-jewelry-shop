#!/usr/bin/env bash
set -o errexit

# Apply database migrations on container startup
python manage.py migrate --noinput

# Load catalog (categories, products, coupons) if not already loaded
python manage.py loaddata store_catalog.json || true

# Start Gunicorn WSGI server
exec gunicorn jewelryshop.wsgi:application
