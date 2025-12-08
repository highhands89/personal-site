#!/bin/bash

# Setup script for deployment environment variables
# This creates a .env file with your FTP credentials

echo "=========================================="
echo "FTP Credentials Setup"
echo "=========================================="
echo ""

read -p "Enter FTP Host (e.g., ftp.klcleeton.com): " FTP_HOST
read -p "Enter FTP Username: " FTP_USER
read -s -p "Enter FTP Password: " FTP_PASS
echo ""
read -p "Enter Remote Directory [public_html]: " FTP_REMOTE_DIR
FTP_REMOTE_DIR=${FTP_REMOTE_DIR:-public_html}

# Create .env file
cat > .env << EOF
# FTP Deployment Credentials
# DO NOT commit this file to version control!

FTP_HOST=$FTP_HOST
FTP_USER=$FTP_USER
FTP_PASS=$FTP_PASS
FTP_REMOTE_DIR=$FTP_REMOTE_DIR
EOF

# Make .env readable only by owner
chmod 600 .env

echo ""
echo "✓ Credentials saved to .env file"
echo "✓ File permissions set to 600 (readable only by you)"
echo ""
echo "To deploy your website, run:"
echo "  source .env && python3 deploy.py"
echo ""
echo "Or add to your shell profile for permanent setup:"
echo "  echo 'source $(pwd)/.env' >> ~/.zshrc"

