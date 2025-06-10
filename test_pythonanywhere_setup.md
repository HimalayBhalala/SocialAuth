# PythonAnywhere Setup Verification

Follow these steps to verify your PythonAnywhere setup is working correctly:

## 1. Add SSH Key to PythonAnywhere

1. Copy the public key content:
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDNGfJUhgzneqtkZp6qkdbLmql3VD5s+VIun3x/G7WKZ6v8FG0UbTmqLR1Pjkj4q1YpnkVElWbHtrXCRHlEl9VMlLO2pIjVcARCyok724dHp47yw0CsBftR2qNHjltcQTUyxDS9wWu91qipiXbSYKn4MRSAiodlzjA/tfv2MgWx57L1gNCKMXZZNsBegzSefPwOWgcqhDJlXl2d9vcq/NXT/uWRDruucNK7E4UroayQ58nxClHSysFkBe5x4ZxKeJ0ERZ4bzmnVGsxrxZSNkhCv7l3ygclamMtcUbFMdNxixBnWhray9MDo7SXCJjgEzqvGEUsKnExolPUpEXK/mHYB6Tc/NFZWpN/r/DARqYbmDR773FPHSYniNa83J77hQXB2wyvS0yRAEuFSVVvHtH39S4KXuGPKxDShik/mXktbjjhipA8EZMjPCLZ+lea4Co27K+UFrCblc+si9Mxe67cHZ5DcsJla6wKmtkqMKxyUWAn6oRqI8emLb6EGF15j+fXL0xjiul1bQpNM4DmnL/EahqTfsRGNBWvPKSsYGQxzaq8aDGDvDTvNWTwB7dGQfPrh2whAKN/flLkLSNkeV3Zhf83qJZ+TkYzZydtLrQ9INKyQuEMNNta938cwoHB+Z7gKesI99Lr3nRaZhQ0+22LUIdH1hSKNf1i9i4D2M4z2Pw==
```

2. Go to your PythonAnywhere account
3. Click on Account → SSH keys
4. Add the public key

## 2. Add Secrets to GitHub

1. Go to your GitHub repository
2. Click on Settings → Secrets → Actions
3. Add these secrets:
   - `SSH_PRIVATE_KEY`: The entire content of your private key
   - `PYTHONANYWHERE_USERNAME`: Your PythonAnywhere username
   - `PYTHONANYWHERE_API_TOKEN`: Your PythonAnywhere API token

## 3. Test the Connection Manually

If you want to test the connection from your local machine, use:

```bash
ssh -i ~/pa_deploy_key your_username@ssh.pythonanywhere.com "echo Connection working"
```

## 4. First-Time Web App Setup

1. Log in to PythonAnywhere
2. Go to Web → Add a new web app
3. Choose:
   - Domain: your_username.pythonanywhere.com
   - Python version: 3.10
   - Framework: Manual configuration
4. Configure the WSGI file to point to: `/var/www/your_username_pythonanywhere_com_wsgi.py`

## 5. Run the GitHub Workflow

1. Push the changes to your GitHub repository
2. Go to Actions → Deploy to PythonAnywhere
3. Click "Run workflow"
4. Monitor the workflow for any errors

## Troubleshooting

If you encounter any issues:

1. Check the GitHub Actions logs for errors
2. Verify your SSH key is properly formatted
3. Make sure the SSH key is added to PythonAnywhere
4. Check the PythonAnywhere error logs
5. Try connecting manually to debug any SSH issues 