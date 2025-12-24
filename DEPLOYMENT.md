# Ironcreed - Firebase Deployment Guide

## Prerequisites
✅ Firebase CLI installed (already done)
✅ Google/Firebase account
✅ Custom domain purchased

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add Project" or "Create a project"
3. Enter project name: `ironcreed` (or your preferred name)
4. Follow the setup wizard (you can disable Google Analytics if not needed)
5. Click "Create Project"

## Step 2: Login to Firebase

Open terminal and run:
```bash
firebase login
```

This will open a browser window for authentication.

## Step 3: Initialize Firebase Project

In your project directory (c:\Ironcreed), run:
```bash
firebase init hosting
```

Follow the prompts:
- **Select Firebase project**: Choose the project you created in Step 1
- **What do you want to use as your public directory?**: Press Enter (current directory ".")
- **Configure as a single-page app?**: y (Yes)
- **Set up automatic builds and deploys with GitHub?**: n (No, unless you want GitHub integration)
- **Overwrite index.html?**: n (No! We already have our index.html)

After initialization, update `.firebaserc` file with your actual project ID:
```json
{
  "projects": {
    "default": "your-actual-project-id"
  }
}
```

## Step 4: Deploy to Firebase

Deploy your website:
```bash
firebase deploy
```

After deployment, you'll get a URL like: `https://ironcreed.web.app`

## Step 5: Connect Your Custom Domain

1. In [Firebase Console](https://console.firebase.google.com/), select your project
2. Go to **Hosting** in the left sidebar
3. Click **Add custom domain**
4. Enter your domain (e.g., `ironcreed.com`)
5. Firebase will provide DNS records to add

### DNS Configuration

Add these records to your domain registrar's DNS settings:

**For root domain (ironcreed.com):**
- Type: `A`
- Name: `@`
- Value: (Firebase will provide IP addresses)

**For www subdomain:**
- Type: `CNAME`
- Name: `www`
- Value: (Firebase will provide the target)

### Verification
Firebase will provide a TXT record for domain verification:
- Type: `TXT`
- Name: `@`
- Value: (Firebase verification code)

**Note**: DNS changes can take 24-48 hours to propagate globally, but often work within 1-2 hours.

## Step 6: SSL Certificate

Firebase automatically provisions a free SSL certificate for your custom domain. This may take a few hours after DNS verification.

## Quick Commands Reference

### Deploy website
```bash
firebase deploy
```

### Deploy only hosting
```bash
firebase deploy --only hosting
```

### Open Firebase Console
```bash
firebase open hosting:site
```

### View deployment history
```bash
firebase hosting:channel:list
```

## Updating Your Website

Whenever you make changes to your website:

1. Edit your files (index.html, styles.css, script.js)
2. Run: `firebase deploy`
3. Changes will be live in seconds!

## Preview Before Deploying

Test your deployment locally:
```bash
firebase serve
```

Then visit `http://localhost:5000`

## Rollback (if needed)

View previous releases:
```bash
firebase hosting:channel:list
```

## Additional Firebase Features You Can Add

- **Firebase Authentication**: Add user login
- **Cloud Firestore**: Store app data
- **Cloud Functions**: Add backend logic
- **Analytics**: Track user behavior
- **Performance Monitoring**: Monitor site speed

## Support

- Firebase Documentation: https://firebase.google.com/docs/hosting
- Firebase CLI Reference: https://firebase.google.com/docs/cli

---

🚀 Your Ironcreed website is ready to go live!
