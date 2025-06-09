#!/bin/bash
# Script to run Django development server with SQLite for local testing

# Activate virtual environment
source social_venv/bin/activate

# Set environment variables
export USE_SQLITE_FALLBACK=true
export DEBUG=true
export SECRET_KEY=$(cat secrets/django_secret_key.txt)

# Create static directory if it doesn't exist
mkdir -p static

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create superuser if needed
python manage.py shell -c '
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(email="admin@example.com").exists():
    User.objects.create_superuser("admin@example.com", "admin", "admin123")
    print("Superuser created: admin@example.com/admin123")
else:
    print("Superuser already exists")
'

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run development server
echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000 