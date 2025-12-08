#!/bin/bash

# Git Setup Script for Personal Site
# This script helps you set up git and push to GitHub

echo "=========================================="
echo "Git Repository Setup"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install it first."
    exit 1
fi

# Check if already a git repo
if [ -d ".git" ]; then
    echo "Git repository already initialized."
    read -p "Do you want to add/update remote? (y/n): " update_remote
    if [ "$update_remote" = "y" ]; then
        read -p "Enter GitHub repository URL: " repo_url
        git remote remove origin 2>/dev/null
        git remote add origin "$repo_url"
        echo "✓ Remote added: $repo_url"
    fi
else
    # Initialize git repo
    echo "Initializing git repository..."
    git init
    
    # Add remote
    read -p "Enter GitHub repository URL: " repo_url
    git remote add origin "$repo_url"
    echo "✓ Remote added: $repo_url"
fi

# Add all files (except those in .gitignore)
echo ""
echo "Staging files..."
git add .

# Show status
echo ""
echo "Files to be committed:"
git status --short

echo ""
read -p "Enter commit message (or press Enter for default): " commit_msg
commit_msg=${commit_msg:-"Update website with futuristic styling and improvements"}

# Commit
echo ""
echo "Committing changes..."
git commit -m "$commit_msg"

echo ""
echo "=========================================="
echo "Setup complete!"
echo ""
echo "To push to GitHub, run:"
echo "  git push -u origin main"
echo ""
echo "Or if your default branch is 'master':"
echo "  git push -u origin master"
echo ""
echo "You may be prompted for GitHub credentials."
echo "=========================================="

