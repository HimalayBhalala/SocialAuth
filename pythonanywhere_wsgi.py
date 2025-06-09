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

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_authentication.settings'
os.environ['PYTHONANYWHERE_SITE'] = 'true'

# Add your PythonAnywhere specific database credentials
os.environ['PA_DB_NAME'] = 'HimalayBhalala$default'
os.environ['PA_DB_USER'] = 'HimalayBhalala'
os.environ['PA_DB_PASSWORD'] = 'Social0000'  # Replace with your actual password
os.environ['PA_DB_HOST'] = 'HimalayBhalala.mysql.pythonanywhere-services.com'

# Set your secret key securely
os.environ['SECRET_KEY'] = 'y7aovwgl0v0p8v@85klqnuoj6ndm@l02h4g2q^)&)c+lt#9w7p'  # Use your secure key

# Import and set up the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 