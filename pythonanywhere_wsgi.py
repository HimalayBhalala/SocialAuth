"""
WSGI config for PythonAnywhere deployment.
It exposes the WSGI callable as a module-level variable named 'application'.
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/HimalayBhalala/SocialAuth'
if path not in sys.path:
    sys.path.insert(0, path)

# IMPORTANT: Set environment variables BEFORE importing Django
# Set your secret key securely - this MUST be set before Django is loaded
os.environ['SECRET_KEY'] = 'y7aovwgl0v0p8v@85klqnuoj6ndm@l02h4g2q^)&)c+lt#9w7p'

# Set other environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_authentication.settings'
os.environ['PYTHONANYWHERE_SITE'] = 'true'

# Add your PythonAnywhere specific database credentials
os.environ['DB_NAME'] = 'HimalayBhalala$default'
os.environ['DB_USER'] = 'HimalayBhalala'
os.environ['DB_PASSWORD'] = 'Social0000'  # Replace with your actual password
os.environ['DB_HOST'] = 'HimalayBhalala.mysql.pythonanywhere-services.com'

# Set DEBUG to False for production
os.environ['DEBUG'] = 'False'

# Optionally set other environment variables needed by your app
# os.environ['ALLOWED_HOSTS'] = 'himalaybhalala.pythonanywhere.com'

# Import and set up the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 