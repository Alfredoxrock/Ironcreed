const express = require('express');
const path = require('path');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static site from project root
app.use(express.static(path.join(__dirname)));

// Configure email transporter
const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    secure: false, // true for 465, false for other ports
    auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS
    }
});

// Contact form endpoint
app.post('/api/contact', async (req, res) => {
    const { name, email, message } = req.body || {};

    console.log('Contact submission received:');
    console.log({ name, email, message });

    // Send email
    try {
        await transporter.sendMail({
            from: process.env.SMTP_USER,
            to: 'contact@ironcreed.net',
            subject: `New Contact Form Submission from ${name}`,
            text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
            html: `
                <h3>New Contact Form Submission</h3>
                <p><strong>Name:</strong> ${name}</p>
                <p><strong>Email:</strong> ${email}</p>
                <p><strong>Message:</strong></p>
                <p>${message.replace(/\n/g, '<br>')}</p>
            `,
            replyTo: email
        });

        console.log('Email sent successfully');
        res.json({ ok: true, message: 'Thanks — we received your message.' });
    } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).json({ ok: false, message: 'Error sending message. Please try again later.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
