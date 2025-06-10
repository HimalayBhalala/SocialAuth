# Manual Deployment to PythonAnywhere

This guide provides step-by-step instructions to set up SSH keys for automated deployment to PythonAnywhere.

## Step 1: Generate a new SSH key pair

Run these commands on your local machine:

```bash
# Create a new SSH key pair (no passphrase for automated deployment)
ssh-keygen -t rsa -b 4096 -f pythonanywhere_deploy_key -N ""

# Display the public key to copy
cat pythonanywhere_deploy_key.pub
```

## Step 2: Add the public key to PythonAnywhere

1. Log in to your PythonAnywhere account
2. Go to Account → SSH keys (in the top-right menu)
3. Add the public key content (copied from the previous step)
4. Click "Add" to save the key

## Step 3: Add the private key to GitHub repository secrets

1. Copy the private key content:
   ```bash
   cat pythonanywhere_deploy_key
   ```
2. Go to your GitHub repository
3. Click on Settings → Secrets → Actions
4. Create a new repository secret named `SSH_PRIVATE_KEY`
5. Paste the entire private key content (including BEGIN and END lines)
6. Click "Add secret" to save

## Step 4: Update your GitHub workflow file

Make sure your workflow file includes the proper steps to set up SSH keys:

1. The key should be stored in `~/.ssh/id_rsa`
2. Set the correct permissions (`chmod 600 ~/.ssh/id_rsa`)
3. Add the PythonAnywhere host key with `ssh-keyscan`

## Testing the connection

You can test the SSH connection from GitHub Actions by adding a step that runs a simple command:

```yaml
- name: Test SSH connection
  run: |
    ssh -o StrictHostKeyChecking=no -i ~/.ssh/id_rsa ${{ secrets.PYTHONANYWHERE_USERNAME }}@ssh.pythonanywhere.com "echo SSH connection successful"
```

## Troubleshooting

If you still have SSH connection issues:

1. Check that the key format is correct (starts with `-----BEGIN OPENSSH PRIVATE KEY-----`)
2. Verify the key has proper permissions (`chmod 600 ~/.ssh/id_rsa`)
3. Make sure you've added the key correctly to PythonAnywhere
4. Try adding debugging to your workflow:
   ```yaml
   - name: Debug SSH
     run: |
       ls -la ~/.ssh/
       ssh -v -o StrictHostKeyChecking=no -i ~/.ssh/id_rsa ${{ secrets.PYTHONANYWHERE_USERNAME }}@ssh.pythonanywhere.com
   ``` 