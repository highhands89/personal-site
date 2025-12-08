# EmailJS Setup Guide - Fixing Contact Form

Your contact form uses EmailJS to send emails. If it's not working, follow these steps:

## Current Configuration

- **EmailJS Public Key:** `x3LeslaSLVGHOt75r`
- **Service ID:** `service_fk6wcgq`
- **Template ID:** `template_0c9glu8`
- **reCAPTCHA Site Key:** `6LfhLX0lAAAAANbQ1K1fkZze0BbYHb5OZt1YMGF1`

## Troubleshooting Steps

### Step 1: Check Browser Console

1. Open your contact page
2. Press `F12` (or right-click → Inspect)
3. Go to the "Console" tab
4. Try submitting the form
5. Look for any red error messages

Common errors:
- `EmailJS is not defined` - EmailJS script not loading
- `Invalid service ID` - Service ID is wrong
- `Invalid template ID` - Template ID is wrong
- `Domain not whitelisted` - Need to add your domain to EmailJS

### Step 2: Verify EmailJS Account Setup

1. Go to https://www.emailjs.com/
2. Log in to your account
3. Check if your service is active:
   - Go to "Email Services"
   - Verify `service_fk6wcgq` exists and is connected to an email account
   - Make sure it's connected to YOUR email (where you want to receive messages)

### Step 3: Verify Email Template

1. In EmailJS dashboard, go to "Email Templates"
2. Check if `template_0c9glu8` exists
3. Verify the template has these variables:
   - `{{name}}`
   - `{{email}}`
   - `{{message}}`
   - `{{g-recaptcha-response}}` (optional, for reCAPTCHA)

### Step 4: Check Domain Whitelist

1. In EmailJS dashboard, go to "Account" → "General"
2. Under "Allowed Domains" or "Domain Restrictions"
3. Add your domain: `klcleeton.com`
4. Also add: `www.klcleeton.com`
5. Save changes

### Step 5: Test Email Service Connection

1. In EmailJS dashboard, go to "Email Services"
2. Click on your service (`service_fk6wcgq`)
3. Click "Test" or "Send Test Email"
4. If test fails, reconnect your email account

## Common Issues & Solutions

### Issue: "Service ID not found"
**Solution:** 
- Verify the Service ID in EmailJS dashboard
- Make sure the service is active and connected

### Issue: "Template ID not found"
**Solution:**
- Verify the Template ID in EmailJS dashboard
- Make sure the template exists and is published

### Issue: "Domain not whitelisted"
**Solution:**
- Add your domain to EmailJS allowed domains
- Wait a few minutes for changes to take effect

### Issue: "Email service not connected"
**Solution:**
- Reconnect your email account in EmailJS
- For Gmail, you may need an "App Password" instead of regular password
- For other providers, check their SMTP settings

### Issue: Form submits but no email received
**Solution:**
- Check spam/junk folder
- Verify the email address in EmailJS service settings
- Check EmailJS dashboard for sent emails (they log all sends)
- Verify email service is properly connected

## Setting Up EmailJS (If Starting Fresh)

If you need to set up EmailJS from scratch:

1. **Create Account:**
   - Go to https://www.emailjs.com/
   - Sign up for free account

2. **Add Email Service:**
   - Go to "Email Services"
   - Click "Add New Service"
   - Choose your email provider (Gmail, Outlook, etc.)
   - Follow connection instructions
   - **Note:** For Gmail, you'll need to:
     - Enable 2-factor authentication
     - Generate an "App Password"
     - Use the app password (not your regular password)

3. **Create Email Template:**
   - Go to "Email Templates"
   - Click "Create New Template"
   - Set up template with variables:
     ```
     From: {{email}}
     To: your-email@example.com
     Subject: New Contact Form Message from {{name}}
     
     Name: {{name}}
     Email: {{email}}
     Message: {{message}}
     ```
   - Save and note the Template ID

4. **Get Public Key:**
   - Go to "Account" → "General"
   - Copy your Public Key
   - Update it in `contact.html` (line 32)

5. **Update Configuration:**
   - Update `contact.js` with your Service ID and Template ID
   - Update `contact.html` with your Public Key

## Testing

After fixing, test the form:
1. Fill out all fields
2. Complete reCAPTCHA
3. Click "Send"
4. Check browser console for errors
5. Check your email (including spam folder)
6. Check EmailJS dashboard for sent logs

## Alternative: Simple Mailto Fallback

If EmailJS continues to have issues, you can add a simple mailto link as a fallback:

```html
<p>Or email directly: <a href="mailto:kl@rangetrainerpro.com">kl@rangetrainerpro.com</a></p>
```

## Need Help?

If you're still having issues:
1. Check the browser console for specific error messages
2. Verify all IDs match your EmailJS dashboard
3. Test EmailJS service connection directly in their dashboard
4. Check EmailJS documentation: https://www.emailjs.com/docs/

