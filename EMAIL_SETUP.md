# Email Setup Instructions

The contact form is now configured to send emails to **contact@ironcreed.net**.

## Required: Update .env File

Open `.env` and configure these settings:

### Option 1: Gmail (Easiest for Testing)

1. Update `.env`:
```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-gmail@gmail.com
SMTP_PASS=your-app-password
```

2. Get a Gmail App Password:
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Copy the 16-character password
   - Paste it as `SMTP_PASS` in `.env`

### Option 2: Custom Domain Email (ironcreed.net)

If you have email hosting for your domain:

```
SMTP_HOST=mail.ironcreed.net (or your provider's SMTP server)
SMTP_PORT=587
SMTP_USER=contact@ironcreed.net
SMTP_PASS=your-email-password
```

Common providers:
- **GoDaddy**: smtp.secureserver.net
- **Namecheap**: mail.privateemail.com
- **Google Workspace**: smtp.gmail.com

### Option 3: SendGrid (For Production)

1. Sign up at https://sendgrid.com (free tier: 100 emails/day)
2. Create an API key
3. Update `.env`:
```
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASS=your-sendgrid-api-key
```

## Test Locally

1. Update `.env` with your SMTP settings
2. Restart the server: `npm start`
3. Go to http://localhost:3000
4. Submit the contact form
5. Check that you receive the email at contact@ironcreed.net

## Deploy to Production

**Note:** The current Firebase Hosting deployment is static-only and cannot run Node.js servers.

For the email feature to work in production, you need to:

1. **Deploy to a platform that supports Node.js:**
   - Vercel
   - Heroku
   - Railway
   - DigitalOcean App Platform
   - AWS Elastic Beanstalk

2. **Or use a serverless function:**
   - Firebase Cloud Functions
   - Netlify Functions
   - Vercel Serverless Functions

Would you like help setting up one of these options?
