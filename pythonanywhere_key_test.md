# Troubleshooting PythonAnywhere SSH Key Authentication

If you're having issues with SSH key authentication to PythonAnywhere from GitHub Actions, follow these steps to identify and fix the problem.

## Step 1: Copy the Key from GitHub Actions

1. When you run the workflow, it will generate a new SSH key and display it in the log
2. Look for a section that looks like this:
   ```
   ==================================================================
   GENERATED PUBLIC SSH KEY - COPY THIS ENTIRE KEY:
   ==================================================================
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDDrTF6Cpn3... runner@GitHub-Actions
   ==================================================================
   ```
3. Copy this ENTIRE key, including the `ssh-rsa` at the beginning and the `runner@GitHub-Actions` at the end

## Step 2: Add the Key to PythonAnywhere

1. Log in to your PythonAnywhere account
2. Click on your username in the top right, then select "Account"
3. Click on the "SSH keys" tab
4. In the "Add a new SSH key" section, paste the ENTIRE key you copied
5. Click "Add" to save the key

## Step 3: Verify the Key was Added Correctly

1. Check that the key appears in your list of SSH keys on PythonAnywhere
2. The key should be displayed with a fingerprint that matches what was shown in the GitHub Actions log
3. Make sure there are no extra spaces or characters in the key

## Step 4: Rerun the GitHub Actions Workflow

After adding the key to PythonAnywhere:
1. Go back to your GitHub repository
2. Click on the "Actions" tab
3. Select the "Deploy to PythonAnywhere" workflow
4. Click "Run workflow" and choose the main branch

## Common Issues and Solutions

### 1. Key Copying Problems

**Issue**: Not copying the entire key, or adding extra spaces/characters.
**Solution**: Make sure to copy the entire key exactly as displayed, including the `ssh-rsa` prefix.

### 2. Wrong Username

**Issue**: The GitHub secret `PYTHONANYWHERE_USERNAME` doesn't match your actual PythonAnywhere username.
**Solution**: Double-check the username in your GitHub repository secrets.

### 3. PythonAnywhere Account Issues

**Issue**: SSH access might be restricted on your PythonAnywhere account type.
**Solution**: Verify that SSH access is enabled for your account type (available on paid accounts).

### 4. Manual SSH Testing

If you want to test the connection manually:

1. Create a file with the private key from the GitHub Actions log
2. Set proper permissions:
   ```bash
   chmod 600 private_key_file
   ```
3. Test the connection:
   ```bash
   ssh -i private_key_file username@ssh.pythonanywhere.com "echo Connection successful"
   ```

Remember that SSH keys generated in GitHub Actions are temporary and will be different each time the workflow runs. Make sure to use the most recent key displayed in the workflow logs. 