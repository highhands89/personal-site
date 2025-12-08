# Fixing Gmail Authentication Scopes Error

## Error Message
```
Gmail_API: Request had insufficient authentication scopes.
```

This means Gmail wasn't granted all the necessary permissions when you reconnected.

## Solution: Reconnect with Full Permissions

### Step 1: Disconnect Current Connection
1. Go to https://www.emailjs.com/
2. Navigate to **Email Services**
3. Click on your service (`service_fk6wcgq`)
4. Click **"Disconnect"** or **"Remove"** to completely remove the Gmail connection

### Step 2: Reconnect Gmail Properly
1. Click **"Add New Service"** or **"Connect"**
2. Select **"Gmail"** as the service type
3. Click **"Connect Account"**
4. **IMPORTANT:** When Google asks for permissions, make sure to:
   - ✅ Grant **ALL** requested permissions
   - ✅ Don't skip any permission requests
   - ✅ Click "Allow" for all scopes
   - ✅ Complete the full authorization flow

### Step 3: Verify Permissions
After connecting, EmailJS needs these Gmail scopes:
- `https://www.googleapis.com/auth/gmail.send` (Send emails)
- `https://www.googleapis.com/auth/gmail.compose` (Compose emails)

### Step 4: Test Connection
1. In EmailJS dashboard, click **"Send Test Email"**
2. If it works, your connection is good
3. If not, try disconnecting and reconnecting again

## Alternative: Use SMTP Instead of Gmail API

If OAuth keeps having scope issues, switch to SMTP (more reliable):

### Step 1: Generate Gmail App Password
1. Go to https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not already enabled)
3. Go to https://myaccount.google.com/apppasswords
4. Select:
   - **App:** Mail
   - **Device:** Other (Custom name) → "EmailJS"
5. Click **Generate**
6. **Copy the 16-character password** (it looks like: `abcd efgh ijkl mnop`)

### Step 2: Update EmailJS Service
1. In EmailJS, go to **Email Services**
2. **Delete** your current Gmail service
3. Click **"Add New Service"**
4. Choose **"Gmail"** or **"SMTP"**
5. Enter:
   - **Email:** your Gmail address (e.g., `yourname@gmail.com`)
   - **Password:** The App Password you generated (NOT your regular Gmail password!)
6. Save

### Step 3: Test
- Try your contact form again
- SMTP is more stable and doesn't have scope issues

## Why This Happens

- Google OAuth requires specific "scopes" (permissions)
- If you cancel or skip any permission requests, you get this error
- Sometimes Google's permission screen doesn't show all scopes clearly

## Best Practice: Use App Password (SMTP)

**Recommendation:** Use Gmail App Password with SMTP instead of OAuth:
- ✅ More reliable
- ✅ No scope issues
- ✅ Doesn't expire as often
- ✅ Easier to troubleshoot

## Still Having Issues?

1. **Check Google Account Permissions:**
   - Go to https://myaccount.google.com/permissions
   - Look for "EmailJS" or "Third-party apps"
   - Remove it if it exists
   - Reconnect fresh

2. **Try Different Browser:**
   - Sometimes browser extensions block OAuth
   - Try incognito/private mode
   - Or use a different browser

3. **Contact EmailJS Support:**
   - They can help troubleshoot scope issues
   - May have specific instructions for your account

