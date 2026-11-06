"""
WSGI config for jewelryshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewelryshop.settings')

application = get_wsgi_application()

# Auto-apply migrations and seed initial data on container startup
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)

    # Load initial catalog if categories table is empty
    from store.models import Category
    if not Category.objects.exists():
        try:
            call_command('loaddata', 'store_catalog.json')
            print("Successfully loaded store_catalog.json")
        except Exception as data_err:
            print(f"Catalog fixture error (safe to ignore if already loaded): {data_err}")

    # Create admin superuser if not exists
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'Admin@12345')
        print("Superuser created successfully: admin / Admin@12345")
except Exception as e:
    sys.stderr.write(f"Startup initialization note: {e}\n")
