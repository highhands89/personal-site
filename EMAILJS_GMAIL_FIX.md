# Fixing Gmail Connection in EmailJS

## Error Message
```
Gmail_API: Invalid grant. Please reconnect your Gmail account
```

This means your Gmail OAuth token has expired and needs to be reconnected.

## Quick Fix: Reconnect Gmail

1. **Go to EmailJS Dashboard:**
   - Visit https://www.emailjs.com/
   - Log in to your account

2. **Navigate to Email Services:**
   - Click "Email Services" in the left sidebar
   - Find your service: `service_fk6wcgq`
   - Click on it to edit

3. **Reconnect Gmail:**
   - Click "Reconnect" or "Edit" button
   - You'll be redirected to Google to authorize
   - Sign in with your Gmail account
   - Grant permissions to EmailJS
   - You'll be redirected back to EmailJS

4. **Verify Connection:**
   - The service should show as "Connected"
   - Status should be green/active

5. **Test:**
   - Go back to your contact form
   - Try submitting again

## Alternative: Use App Password (More Reliable)

If OAuth keeps expiring, you can use Gmail App Passwords instead:

### Step 1: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Enable "2-Step Verification" if not already enabled

### Step 2: Generate App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Other (Custom name)"
3. Name it "EmailJS" or "Contact Form"
4. Click "Generate"
5. Copy the 16-character password (no spaces)

### Step 3: Update EmailJS Service
1. In EmailJS dashboard, go to Email Services
2. Edit your service (`service_fk6wcgq`)
3. Choose "Gmail" as service type
4. Enter:
   - **Email:** your Gmail address
   - **Password:** the App Password you just generated (not your regular password!)
5. Save

### Step 4: Test
- Try your contact form again
- It should work now!

## Why This Happens

- Gmail OAuth tokens expire for security
- They typically expire after:
  - 6 months of inactivity
  - When you revoke access
  - When Google security policies change
  - When you change your Google password

## Prevention

- **Use App Passwords:** More stable, don't expire as often
- **Check periodically:** Reconnect before tokens expire
- **Monitor EmailJS dashboard:** They'll notify you if connection fails

## Still Having Issues?

1. **Check EmailJS Dashboard:**
   - Go to Email Services
   - Verify service status is "Active"
   - Check if there are any error messages

2. **Try Test Email:**
   - In EmailJS dashboard, click "Send Test Email"
   - This will tell you if the connection works

3. **Check Gmail Settings:**
   - Make sure "Less secure app access" is enabled (if using password)
   - Or use App Password (recommended)

4. **Contact EmailJS Support:**
   - If nothing works, contact EmailJS support
   - They can help troubleshoot connection issues

