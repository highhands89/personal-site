#!/bin/bash

# Deployment Script for Namecheap Hosting
# This script uploads all files to your Namecheap hosting via FTP

echo "=========================================="
echo "Website Deployment Script"
echo "=========================================="
echo ""

# Get FTP credentials from user
read -p "Enter FTP Host (e.g., ftp.klcleeton.com): " FTP_HOST
read -p "Enter FTP Username: " FTP_USER
read -s -p "Enter FTP Password: " FTP_PASS
echo ""
read -p "Enter Remote Directory (usually 'public_html'): " REMOTE_DIR

echo ""
echo "Starting upload..."

# Install lftp if not available (for better FTP support)
if ! command -v lftp &> /dev/null; then
    echo "Installing lftp..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install lftp
    else
        echo "Please install lftp: sudo apt-get install lftp (Linux) or brew install lftp (Mac)"
        exit 1
    fi
fi

# Create a temporary FTP script
FTP_SCRIPT=$(mktemp)
cat > "$FTP_SCRIPT" << EOF
set ftp:ssl-allow no
open -u $FTP_USER,$FTP_PASS $FTP_HOST
cd $REMOTE_DIR
mirror -R --delete --verbose --exclude-glob=".git*" --exclude-glob="*.md" --exclude-glob="deploy.sh" .
quit
EOF

# Execute FTP upload
lftp -f "$FTP_SCRIPT"

# Cleanup
rm "$FTP_SCRIPT"

echo ""
echo "=========================================="
echo "Upload complete!"
echo "Visit your website to verify: https://klcleeton.com"
echo "=========================================="

