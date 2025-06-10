# Fixing SSH Issues with PythonAnywhere Deployment

This guide addresses the specific error you're encountering with SSH host key verification and permission denied errors.

## The Issues

1. **Host Key Verification Failure**: The error message indicates that the SSH host key for PythonAnywhere has changed, which triggers a security warning.
2. **SSH Key Loading Error**: The "error in libcrypto" message suggests there's an issue with the format or permissions of your SSH key.

## Solution 1: Updated GitHub Workflow

I've updated your GitHub workflow to:

1. Remove any existing known_hosts entries for PythonAnywhere
2. Fetch the latest host key directly
3. Manually set up the SSH key with proper validation
4. Use `-o StrictHostKeyChecking=accept-new` to automatically accept new host keys
5. Add verbose SSH output for better debugging

This should fix both issues automatically when you run the workflow.

## Solution 2: Manual SSH Key Testing

If you want to test this locally:

```bash
# Remove old host key
ssh-keygen -f ~/.ssh/known_hosts -R ssh.pythonanywhere.com

# Add new host key
ssh-keyscan -t rsa ssh.pythonanywhere.com >> ~/.ssh/known_hosts

# Test connection with verbose output
ssh -v -i ~/pa_deploy_key your_username@ssh.pythonanywhere.com "echo Connection successful"
```

## Solution 3: Regenerate SSH Keys

If you're still having issues, regenerate the SSH keys with these exact steps:

```bash
# Generate a new key with the correct format
ssh-keygen -t rsa -b 4096 -m PEM -f ~/.ssh/pythonanywhere_key -N ""

# Copy the public key to clipboard
cat ~/.ssh/pythonanywhere_key.pub

# View the private key (to copy to GitHub)
cat ~/.ssh/pythonanywhere_key
```

Make sure to:
1. Add the public key to PythonAnywhere's SSH keys section
2. Add the private key (including BEGIN/END markers) to your GitHub secret

## Solution 4: Format Check for SSH Private Key

Ensure your private key has the correct format. It should:

1. Start with `-----BEGIN OPENSSH PRIVATE KEY-----` or `-----BEGIN RSA PRIVATE KEY-----`
2. End with `-----END OPENSSH PRIVATE KEY-----` or `-----END RSA PRIVATE KEY-----`
3. Have all the content in between with no modifications
4. Be added to GitHub secrets without any whitespace modifications

## Solution 5: Alternative SSH Implementation

If all else fails, you can use a different approach by:

1. Adding a deploy key to your GitHub repository
2. Using HTTPS authentication with a personal access token
3. Using the PythonAnywhere API directly instead of SSH

## Troubleshooting

If you still have issues:

1. Check the verbose SSH output for specific errors
2. Verify the SSH key format and permissions
3. Make sure the public key is correctly added to PythonAnywhere
4. Try a direct connection from your local machine to isolate GitHub Actions-specific issues 