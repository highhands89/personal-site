#!/usr/bin/env python3
"""
Automated Deployment Script for Namecheap Hosting
Uses environment variables for secure credential management
"""

import ftplib
import os
import sys
from pathlib import Path

def upload_file(ftp, local_path, remote_path):
    """Upload a single file"""
    try:
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_path}', file)
        print(f"✓ Uploaded: {remote_path}")
        return True
    except Exception as e:
        print(f"✗ Failed to upload {remote_path}: {e}")
        return False

def upload_directory(ftp, local_dir, remote_dir):
    """Upload a directory recursively"""
    try:
        # Try to create remote directory
        try:
            ftp.mkd(remote_dir)
        except:
            pass  # Directory might already exist
        
        # Change to remote directory
        ftp.cwd(remote_dir)
        
        # Upload files in current directory
        for item in os.listdir(local_dir):
            local_path = os.path.join(local_dir, item)
            remote_path = item
            
            # Skip hidden files and deployment scripts
            if item.startswith('.') or item in ['deploy.py', 'deploy.sh', 'DEPLOYMENT_INSTRUCTIONS.md']:
                continue
            
            if os.path.isfile(local_path):
                upload_file(ftp, local_path, remote_path)
            elif os.path.isdir(local_path):
                upload_directory(ftp, local_path, remote_path)
        
        # Go back to parent directory
        ftp.cwd('..')
        
    except Exception as e:
        print(f"✗ Error uploading directory {local_dir}: {e}")

def main():
    print("=" * 60)
    print("Automated Website Deployment Script")
    print("=" * 60)
    print()
    
    # Get credentials from environment variables
    ftp_host = os.getenv('FTP_HOST')
    ftp_user = os.getenv('FTP_USER')
    ftp_pass = os.getenv('FTP_PASS')
    remote_dir = os.getenv('FTP_REMOTE_DIR', 'public_html')  # Default to public_html
    
    # Validate credentials
    if not ftp_host:
        print("✗ Error: FTP_HOST environment variable not set")
        print("\nPlease set your FTP credentials as environment variables:")
        print("  export FTP_HOST='ftp.klcleeton.com'")
        print("  export FTP_USER='your_username'")
        print("  export FTP_PASS='your_password'")
        print("  export FTP_REMOTE_DIR='public_html'  # Optional, defaults to public_html")
        print("\nOr create a .env file (see setup instructions)")
        sys.exit(1)
    
    if not ftp_user:
        print("✗ Error: FTP_USER environment variable not set")
        sys.exit(1)
    
    if not ftp_pass:
        print("✗ Error: FTP_PASS environment variable not set")
        sys.exit(1)
    
    # Get project directory
    project_dir = Path(__file__).parent
    
    print(f"Connecting to: {ftp_host}")
    print(f"Remote directory: {remote_dir}")
    print()
    
    try:
        # Connect to FTP server
        print("Connecting to FTP server...")
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        print("✓ Connected successfully!")
        
        # Change to remote directory
        try:
            ftp.cwd(remote_dir)
        except:
            print(f"Creating {remote_dir} directory...")
            try:
                ftp.mkd(remote_dir)
                ftp.cwd(remote_dir)
            except Exception as e:
                print(f"✗ Error creating directory: {e}")
                sys.exit(1)
        
        print()
        print("Uploading files...")
        print("-" * 60)
        
        # Files to upload
        files_to_upload = [
            'index.html',
            'about.html',
            'media-kit.html',
            'contact.html',
            'style.css',
            'aboutStyle.css',
            'pitchStyles.css',
            'contactStyle.css',
            'slide.js',
            'contact.js',
            'favicon.ico'
        ]
        
        uploaded_count = 0
        skipped_count = 0
        
        # Upload individual files
        for filename in files_to_upload:
            filepath = project_dir / filename
            if filepath.exists():
                if upload_file(ftp, filepath, filename):
                    uploaded_count += 1
            else:
                print(f"⚠ Warning: {filename} not found, skipping...")
                skipped_count += 1
        
        # Upload img folder
        img_dir = project_dir / 'img'
        if img_dir.exists():
            print()
            print("Uploading img/ folder...")
            upload_directory(ftp, str(img_dir), 'img')
        
        # Upload assets folder
        assets_dir = project_dir / 'assets'
        if assets_dir.exists():
            print()
            print("Uploading assets/ folder...")
            upload_directory(ftp, str(assets_dir), 'assets')
        
        # Close connection
        ftp.quit()
        
        print()
        print("=" * 60)
        print("✓ Deployment complete!")
        print(f"✓ Files uploaded: {uploaded_count}")
        if skipped_count > 0:
            print(f"⚠ Files skipped: {skipped_count}")
        print()
        print(f"Visit your website: https://klcleeton.com")
        print("=" * 60)
        
    except ftplib.error_perm as e:
        print(f"✗ FTP Permission Error: {e}")
        print("Please check your credentials and directory permissions.")
        sys.exit(1)
    except ftplib.error_temp as e:
        print(f"✗ FTP Temporary Error: {e}")
        print("Please try again in a moment.")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
