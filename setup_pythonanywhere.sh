#!/bin/bash
# Setup script for Django on PythonAnywhere
# Run this after cloning your repository on PythonAnywhere

set -e # Exit on error

echo "=== Setting up Django on PythonAnywhere ==="
echo "This script will help set up your Django project on PythonAnywhere."

# Make sure we're in the right directory
cd ~/SocialAuth

# Create virtual environment if it doesn't exist
if [ ! -d ~/venv ]; then
    echo "Creating virtual environment..."
    python3 -m venv ~/venv
fi

# Activate virtual environment
source ~/venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p ~/staticfiles
mkdir -p ~/media

# Set permissions
echo "Setting permissions..."
chmod -R 755 ~/staticfiles
chmod -R 755 ~/media

# Check if we have a .env file
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp env.sample .env
    echo "Please edit the .env file with your actual settings!"
fi

# Run the permission fixing script
echo "Running permission fixing script..."
python fix_permissions.py

# Check if we need to copy the WSGI file
if [ -f pythonanywhere_wsgi.py ]; then
    echo "Copying WSGI file to correct location..."
    # This path may vary depending on your PythonAnywhere setup
    cp pythonanywhere_wsgi.py ~/var/www/username_pythonanywhere_com_wsgi.py
    echo "Please update the WSGI file path in your PythonAnywhere Web app configuration!"
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput || {
    echo "Static file collection failed. This is likely a permissions issue."
    echo "Please check your settings.py and ensure STATIC_ROOT points to a directory you can write to."
    echo "Common options: ~/staticfiles or ~/SocialAuth/staticfiles"
}

# Run migrations
echo "Running migrations..."
python manage.py migrate || {
    echo "Migrations failed. Check your database settings."
}

echo "=== Setup Complete ==="
echo "Next steps:"
echo "1. Configure your web app in the PythonAnywhere dashboard"
echo "2. Set the correct path to your WSGI file"
echo "3. Configure any environment variables in the PythonAnywhere dashboard"
echo "4. Reload your web app" 