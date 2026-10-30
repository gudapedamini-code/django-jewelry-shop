#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files into STATIC_ROOT
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
