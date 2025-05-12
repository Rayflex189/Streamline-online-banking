#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run database migrations (core apps first)
python manage.py migrate contenttypes --no-input
python manage.py migrate auth --no-input
python manage.py migrate sessions --no-input
python manage.py migrate admin --no-input

# Your app migrations
python manage.py makemigrations
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input
