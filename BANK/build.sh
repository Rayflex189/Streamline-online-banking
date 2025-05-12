#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create default superuser
echo "from django.contrib.auth import get_user_model; \
from django.conf import settings; \
User = get_user_model(); \
username = settings.SUPERUSER_NAME; \
password = settings.SUPERUSER_PASSWORD; \
User.objects.filter(username=username).exists() or User.objects.create_superuser(username=username, password=password)" \
| python manage.py shell

# Collect static files
python manage.py collectstatic --no-input
