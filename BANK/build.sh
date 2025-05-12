#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Create new migrations if needed
python manage.py makemigrations

# Fake migration for existing column (adjust migration name if needed)
python manage.py migrate bank_app --fake

# Apply any other migrations
python manage.py migrate