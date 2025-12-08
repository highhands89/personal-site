# GitHub Setup Guide

## Quick Setup

### Step 1: Run the Setup Script

```bash
cd "/Users/k.l.cleeton/Documents/Projects/Personal Site"
chmod +x setup_git.sh
./setup_git.sh
```

This will:
- Initialize git repository (if not already done)
- Add your GitHub repository as remote
- Stage all files
- Create a commit

### Step 2: Push to GitHub

After running the script, push your changes:

```bash
git push -u origin main
```

(Or `git push -u origin master` if your default branch is master)

## Authentication Options

### Option A: Personal Access Token (Recommended)

1. **Create a Personal Access Token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a name (e.g., "Personal Site Deployment")
   - Select scopes: Check `repo` (full control of private repositories)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again!)

2. **Use the token when pushing:**
   - When prompted for username: Enter your GitHub username
   - When prompted for password: Paste the token (not your GitHub password)

### Option B: GitHub CLI (gh)

1. **Install GitHub CLI:**
   ```bash
   brew install gh
   ```

2. **Authenticate:**
   ```bash
   gh auth login
   ```
   Follow the prompts to authenticate.

3. **Push:**
   ```bash
   git push -u origin main
   ```

### Option C: SSH Key (Most Secure)

1. **Generate SSH key (if you don't have one):**
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **Add SSH key to GitHub:**
   - Copy your public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to: https://github.com/settings/keys
   - Click "New SSH key"
   - Paste your public key

3. **Update remote URL to use SSH:**
   ```bash
   git remote set-url origin git@github.com:username/repo-name.git
   ```

4. **Push:**
   ```bash
   git push -u origin main
   ```

## Manual Git Commands

If you prefer to do it manually:

```bash
# Initialize repository (if not already done)
git init

# Add remote repository
git remote add origin https://github.com/username/repo-name.git

# Stage all files
git add .

# Commit changes
git commit -m "Update website with futuristic styling and improvements"

# Push to GitHub
git push -u origin main
```

## What Gets Committed

The `.gitignore` file ensures these are NOT committed:
- `.env` file (your FTP credentials)
- Deployment scripts (optional)
- OS files (.DS_Store, etc.)

Everything else (HTML, CSS, JS, images) will be committed.

## Troubleshooting

### "Repository not found"
- Check that the repository URL is correct
- Make sure you have access to the repository
- Verify your authentication credentials

### "Authentication failed"
- If using HTTPS: Make sure you're using a Personal Access Token, not your password
- If using SSH: Make sure your SSH key is added to GitHub

### "Branch 'main' does not exist"
- Try: `git push -u origin master` instead
- Or create the branch: `git checkout -b main` then push

## Need Help?

Share your GitHub repository URL and I can help you set it up!

