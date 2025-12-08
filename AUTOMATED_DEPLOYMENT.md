# Automated Deployment Guide

This guide shows you how to set up automated deployment using environment variables.

## Quick Start

### Step 1: Set Up Your Credentials (One-Time Setup)

Run the setup script to create your `.env` file:

```bash
cd "/Users/k.l.cleeton/Documents/Projects/Personal Site"
chmod +x setup_env.sh
./setup_env.sh
```

This will prompt you for:
- FTP Host (e.g., `ftp.klcleeton.com`)
- FTP Username
- FTP Password
- Remote Directory (usually `public_html`)

Your credentials will be saved securely in a `.env` file.

### Step 2: Deploy Your Website

Once credentials are set up, deploy with one command:

```bash
python3 deploy_auto.py
```

That's it! The script will automatically:
- Load your credentials from `.env`
- Connect to your FTP server
- Upload all files
- Upload all folders (img/, assets/)
- Show you a summary

## Alternative: Manual Environment Variables

If you prefer to set environment variables manually:

### macOS/Linux (zsh/bash):

```bash
export FTP_HOST='ftp.klcleeton.com'
export FTP_USER='your_username'
export FTP_PASS='your_password'
export FTP_REMOTE_DIR='public_html'

python3 deploy.py
```

### Make it Permanent (Optional)

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
# FTP Deployment Credentials
export FTP_HOST='ftp.klcleeton.com'
export FTP_USER='your_username'
export FTP_PASS='your_password'
export FTP_REMOTE_DIR='public_html'
```

Then you can just run `python3 deploy.py` anytime.

## Security Notes

- ✅ The `.env` file is in `.gitignore` - your credentials won't be committed
- ✅ `.env` file permissions are set to 600 (readable only by you)
- ✅ Never share your `.env` file or commit it to version control
- ✅ You can change your FTP password anytime in Namecheap cPanel

## Troubleshooting

### "FTP_HOST environment variable not set"
- Make sure you've run `setup_env.sh` or set environment variables
- Check that `.env` file exists in your project directory

### "Permission denied"
- Check your FTP credentials in Namecheap cPanel
- Verify the remote directory name (usually `public_html`)

### "Connection refused"
- Verify your FTP host address
- Check if FTP is enabled in your Namecheap hosting
- Try using your server IP instead of domain name

## What Gets Uploaded

The script uploads:
- ✅ All HTML files (index.html, about.html, etc.)
- ✅ All CSS files (style.css, aboutStyle.css, etc.)
- ✅ All JavaScript files (slide.js, contact.js)
- ✅ The `img/` folder with all images
- ✅ The `assets/` folder with all images
- ✅ favicon.ico

It skips:
- ❌ Hidden files (starting with `.`)
- ❌ Deployment scripts
- ❌ Documentation files (.md files)

## One-Command Deployment

After initial setup, deploying is as simple as:

```bash
python3 deploy_auto.py
```

Or if you've set permanent environment variables:

```bash
python3 deploy.py
```

## Need Help?

If you encounter issues:
1. Check that your `.env` file exists and has correct credentials
2. Verify FTP access in Namecheap cPanel
3. Test FTP connection manually with FileZilla first
4. Check the error messages - they usually tell you what's wrong

