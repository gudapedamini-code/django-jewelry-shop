#!/usr/bin/env bash
set -o errexit

# Apply database migrations on container startup
python manage.py migrate --noinput

# Load catalog (categories, products, coupons) if not already loaded
python manage.py loaddata store_catalog.json || true

# Automatically create admin superuser if none exists (works on Free Tier without Shell)
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Admin@12345')
    print('Superuser created: admin / Admin@12345')
" || true

# Start Gunicorn WSGI server
exec gunicorn jewelryshop.wsgi:application
