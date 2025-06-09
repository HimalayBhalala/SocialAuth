#!/bin/bash
set -e

# Function to echo error message and exit
error_exit() {
    echo "ERROR: $1" >&2
    exit 1
}

# Read secrets from files and set as environment variables
if [ -f "/run/secrets/django_secret_key" ]; then
    export SECRET_KEY=$(cat /run/secrets/django_secret_key)
    echo "Read SECRET_KEY from Docker secret"
else
    # If we're not using Docker secrets, check for environment variable
    if [ -z "$SECRET_KEY" ]; then
        error_exit "SECRET_KEY is not set. Cannot start application safely."
    fi
fi

# Read database password
if [ -f "/run/secrets/db_password" ]; then
    export DB_PASSWORD=$(cat /run/secrets/db_password)
    echo "Read DB_PASSWORD from Docker secret"
fi

# Set a default DEBUG value if not provided
if [ -z "$DEBUG" ]; then
    echo "WARNING: DEBUG environment variable not set. Defaulting to 'False'."
    export DEBUG=False
fi

echo "Environment variables validated successfully."

# Wait for database to be ready
echo "Waiting for database to be fully ready..."
sleep 5

# Database connection test
echo "Database connection test..."
python -c 'import time; import os; os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_authentication.settings"); import django; django.setup(); from django.db import connection; 
for i in range(30): 
    try: connection.ensure_connection(); print("Database connected successfully!"); break
    except Exception as e: print(f"Waiting for database... {e}"); time.sleep(2)
    if i == 29: raise Exception("Could not connect to database")' || echo "Database connection test failed, but continuing..."

# Run migrations
echo "Running database migrations..."
python manage.py migrate || echo "Migrations failed, continuing..."

# Create superuser if not exists
echo "Creating superuser if not exists..."
python manage.py shell -c '
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(email="admin@example.com").exists():
    User.objects.create_superuser("admin@example.com", "admin", "admin123")
    print("Superuser created: admin@example.com/admin123")
else:
    print("Superuser already exists")
' || echo "Superuser creation failed, continuing..."

# Run collectstatic now that we have environment variables
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear || echo "Collectstatic failed, continuing..."

# Execute the command passed to docker run
echo "Starting application with command: $@"
exec "$@" 