#!/usr/bin/env python3
"""
Script to fix PythonAnywhere WSGI file by replacing placeholder username
with the actual PythonAnywhere username.
"""
import os
import sys

def fix_wsgi_file():
    username = os.environ.get('PA_USERNAME')
    if not username:
        print("Error: PA_USERNAME environment variable not set.")
        print("Usage: PA_USERNAME=your_username python fix_pythonanywhere.py")
        sys.exit(1)
    
    wsgi_file = "pythonanywhere_wsgi.py"
    backup_file = "pythonanywhere_wsgi.py.bak"
    
    # Create backup
    if os.path.exists(wsgi_file):
        with open(wsgi_file, 'r') as f:
            original_content = f.read()
            
        with open(backup_file, 'w') as f:
            f.write(original_content)
        
        print(f"Created backup of WSGI file: {backup_file}")
        
        # Replace USERNAME placeholder with actual username
        new_content = original_content.replace('USERNAME', username)
        
        # Write the updated content
        with open(wsgi_file, 'w') as f:
            f.write(new_content)
        
        print(f"Updated WSGI file with username: {username}")
        print("Please ensure your database password is correct in the WSGI file.")
    else:
        print(f"Error: WSGI file {wsgi_file} not found")
        sys.exit(1)

if __name__ == "__main__":
    fix_wsgi_file() 