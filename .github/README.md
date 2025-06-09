# GitHub Workflows for SocialAuth

This directory contains GitHub Action workflows for continuous integration and deployment of the SocialAuth Django application.

## Workflows

### 1. CI Workflow (`ci.yml`)

This workflow runs on every push to main, master, and develop branches, and on pull requests to these branches.

**What it does:**
- Sets up a MySQL database for testing
- Installs Python dependencies
- Runs database migrations
- Executes Django tests
- Performs linting with flake8

### 2. Deployment Workflow (`deploy.yml`)

This workflow runs on pushes to the main or master branch, and can be triggered manually.

**What it does:**
- Sets up SSH access to PythonAnywhere
- Deploys the latest code to your PythonAnywhere account
- Installs dependencies
- Applies migrations
- Collects static files
- Reloads the web application

## Setup for PythonAnywhere Deployment

### 1. Required GitHub Secrets

To use these workflows, you need to set up the following secrets in your GitHub repository:

- `SSH_PRIVATE_KEY`: SSH private key for accessing your PythonAnywhere account
- `PA_USERNAME`: Your PythonAnywhere username
- `PA_API_TOKEN`: API token from PythonAnywhere (can be generated in your account settings)

### 2. PythonAnywhere Configuration

1. Set up a MySQL database on PythonAnywhere
2. Configure the WSGI file (`pythonanywhere_wsgi.py`) with your actual values
3. Add your GitHub repository's SSH key to your PythonAnywhere account

### 3. Manual Deployment

You can manually trigger the deployment workflow from the "Actions" tab in your GitHub repository.

## Troubleshooting

If you encounter deployment issues:

1. Check the GitHub Actions logs
2. Verify your PythonAnywhere configuration
3. Ensure database credentials are correct in your WSGI file
4. Check that all required environment variables are set 