#!/usr/bin/env python3
"""
Script to create a proper WSGI file for PythonAnywhere deployment.
"""
import os
import sys

def create_wsgi_file():
    """Create a WSGI file with the correct settings."""
    username = os.environ.get('PA_USERNAME', '')
    if not username:
        print("Error: PA_USERNAME environment variable not set.")
        return False
    
    wsgi_dir = os.path.expanduser("~/var/www")
    if not os.path.exists(wsgi_dir):
        os.makedirs(wsgi_dir, exist_ok=True)
    
    wsgi_path = os.path.join(wsgi_dir, f"{username}_pythonanywhere_com_wsgi.py")
    
    wsgi_content = f'''"""
WSGI config for PythonAnywhere deployment.
It exposes the WSGI callable as a module-level variable named 'application'.
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/{username}/SocialAuth'
if path not in sys.path:
    sys.path.insert(0, path)

# IMPORTANT: Set environment variables BEFORE importing Django
# Set your secret key securely - this MUST be set before Django is loaded
os.environ['SECRET_KEY'] = 'y7aovwgl0v0p8v@85klqnuoj6ndm@l02h4g2q^)&)c+lt#9w7p'

# Set other environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_authentication.settings'
os.environ['PYTHONANYWHERE_SITE'] = 'true'

# Add your PythonAnywhere specific database credentials
os.environ['DB_NAME'] = '{username}$default'
os.environ['DB_USER'] = '{username}'
os.environ['DB_PASSWORD'] = 'Social0000'  # Replace with your actual password
os.environ['DB_HOST'] = '{username}.mysql.pythonanywhere-services.com'

# Set DEBUG to False for production
os.environ['DEBUG'] = 'False'

# Import and set up the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''
    
    with open(wsgi_path, 'w') as f:
        f.write(wsgi_content)
    
    print(f"Created WSGI file at: {wsgi_path}")
    return True

if __name__ == "__main__":
    create_wsgi_file() 