# Deployment Instructions for Namecheap Hosting

## Quick Start Guide

### Method 1: Using Namecheap File Manager (Easiest - No Software Needed)

1. **Log into Namecheap**
   - Go to https://www.namecheap.com
   - Click "Sign In" (top right)
   - Enter your credentials

2. **Access Your Hosting**
   - Click "Account" → "Dashboard"
   - Find your domain (klcleeton.com)
   - Click "Manage" next to your domain
   - Click "cPanel" or "Hosting"

3. **Open File Manager**
   - In cPanel, find "Files" section
   - Click "File Manager"
   - Navigate to the `public_html` folder (this is your website's root directory)

4. **Upload Your Files**
   - Click "Upload" button in the top toolbar
   - Select ALL files from your project folder:
     - `index.html`
     - `about.html`
     - `media-kit.html`
     - `contact.html`
     - `style.css`
     - `aboutStyle.css`
     - `pitchStyles.css`
     - `contactStyle.css`
     - `slide.js`
     - `contact.js`
     - `favicon.ico`
   - Upload the `img/` folder (with all images inside)
   - Upload the `assets/` folder (with all images inside)
   - Wait for all uploads to complete

5. **Verify Your Website**
   - Visit https://klcleeton.com
   - Check that all pages load correctly
   - Test navigation between pages
   - Verify images display properly

---

### Method 2: Using FTP Software (FileZilla)

1. **Get Your FTP Credentials**
   - In cPanel, go to "Files" → "FTP Accounts"
   - Note down:
     - FTP Host (usually `ftp.klcleeton.com` or your server IP)
     - Username
     - Password
     - Port (usually 21)

2. **Download FileZilla**
   - Go to https://filezilla-project.org/download.php?type=client
   - Download and install FileZilla Client

3. **Connect to Your Server**
   - Open FileZilla
   - Enter your FTP credentials:
     - Host: Your FTP host
     - Username: Your FTP username
     - Password: Your FTP password
     - Port: 21
   - Click "Quickconnect"

4. **Upload Your Files**
   - On the RIGHT side (Remote site), navigate to `public_html`
   - On the LEFT side (Local site), navigate to your project folder
   - Select all files and folders
   - Drag them to `public_html` on the right side
   - Wait for upload to complete

5. **Verify Your Website**
   - Visit https://klcleeton.com
   - Check everything works correctly

---

## File Structure on Server

Your files should be organized like this in `public_html`:

```
public_html/
├── index.html
├── about.html
├── media-kit.html
├── contact.html
├── style.css
├── aboutStyle.css
├── pitchStyles.css
├── contactStyle.css
├── slide.js
├── contact.js
├── favicon.ico
├── img/
│   ├── gold-wheelchair.png
│   └── KLCleeton.jpg
└── assets/
    ├── heroImg.jpg
    ├── speaker.png
    ├── cam.png
    ├── pouch.png
    ├── asset 2.jpg
    └── asset 3.jpg
```

---

## Troubleshooting

### Images Not Showing?
- Make sure `img/` and `assets/` folders are uploaded
- Check file names match exactly (case-sensitive)
- Verify images are inside the folders, not loose files

### Styling Not Working?
- Clear your browser cache (Ctrl+Shift+Delete)
- Make sure all CSS files are uploaded
- Check file names match exactly

### Pages Not Loading?
- Verify all HTML files are in `public_html` (not a subfolder)
- Check file permissions (should be 644 for files, 755 for folders)
- Look at cPanel error logs: "Errors" → "Error Log"

### SSL/HTTPS Issues?
- In cPanel, go to "SSL/TLS Status"
- Enable SSL certificate (Let's Encrypt is free)
- Force HTTPS redirect if needed

---

## Quick Checklist

Before going live, verify:
- [ ] All HTML files uploaded
- [ ] All CSS files uploaded
- [ ] All JavaScript files uploaded
- [ ] `img/` folder uploaded with images
- [ ] `assets/` folder uploaded with images
- [ ] `favicon.ico` uploaded
- [ ] Website loads at your domain
- [ ] All pages work (Home, About, Media Kit, Contact)
- [ ] Images display correctly
- [ ] Styling looks correct
- [ ] Links work properly

---

## Need Help?

If you run into issues:
1. Check cPanel error logs
2. Verify file names match exactly
3. Ensure files are in `public_html` root
4. Clear browser cache
5. Check file permissions

