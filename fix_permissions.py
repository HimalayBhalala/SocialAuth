#!/usr/bin/env python3
"""
Script to check and fix permissions for Django static and media directories on PythonAnywhere.
Run this script on PythonAnywhere when you encounter permission issues.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_and_create_dir(path):
    """Check if directory exists and create it if needed with proper permissions."""
    path = Path(path)
    
    if path.exists():
        print(f"✓ {path} exists")
    else:
        try:
            print(f"Creating {path}...")
            # Create directory with full permissions for the owner
            path.mkdir(parents=True, exist_ok=True)
            print(f"✓ Created {path}")
        except PermissionError:
            print(f"✗ Permission denied when creating {path}")
            return False
    return True

def fix_permissions(path):
    """Fix permissions on a directory to ensure the web process can write to it."""
    try:
        # Make sure we have ownership and proper permissions
        subprocess.run(['chmod', '-R', '755', str(path)], check=True)
        print(f"✓ Fixed permissions for {path}")
        return True
    except (subprocess.SubprocessError, PermissionError) as e:
        print(f"✗ Failed to fix permissions for {path}: {e}")
        return False

def main():
    # Define directories to check/create
    username = os.environ.get('USER', 'HimalayBhalala')
    home_dir = Path(f'/home/{username}')
    
    directories = [
        home_dir / 'staticfiles',
        home_dir / 'media',
        home_dir / 'SocialAuth' / 'staticfiles',
        home_dir / 'SocialAuth' / 'media',
    ]
    
    # Check and create directories
    for directory in directories:
        if check_and_create_dir(directory):
            fix_permissions(directory)
    
    print("\nDirectories checked and permissions fixed where possible.")
    print("\nIf you're still having issues, you might need to:")
    print("1. Contact PythonAnywhere support")
    print("2. Update your Django settings.py to use directories you have access to")
    print("3. Configure your web app correctly in the PythonAnywhere dashboard")

if __name__ == "__main__":
    main() 