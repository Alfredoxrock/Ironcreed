const { onRequest } = require("firebase-functions/v2/https");
const { defineSecret } = require("firebase-functions/params");
const nodemailer = require("nodemailer");
const cors = require("cors")({ origin: true });

// Define secrets
const smtpUser = defineSecret("SMTP_USER");
const smtpPass = defineSecret("SMTP_PASS");

exports.sendContactEmail = onRequest(
    { secrets: [smtpUser, smtpPass] },
    (req, res) => {
        // Configure email transporter
        const transporter = nodemailer.createTransport({
            host: "smtp.gmail.com",
            port: 587,
            secure: false,
            requireTLS: true,
            auth: {
                user: smtpUser.value(),
                pass: smtpPass.value(),
            },
        });
        cors(req, res, async () => {
            if (req.method !== "POST") {
                return res.status(405).json({
                    ok: false,
                    message: "Method not allowed",
                });
            }

            const { name, email, message } = req.body;

            if (!name || !email || !message) {
                return res.status(400).json({
                    ok: false,
                    message: "Name, email, and message are required",
                });
            }

            try {
                await transporter.sendMail({
                    from: smtpUser.value(),
                    to: "contact@ironcreed.net",
                    subject: `New Contact Form Submission from ${name}`,
                    text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
                    html: `
          <h3>New Contact Form Submission</h3>
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Message:</strong></p>
          <p>${message.replace(/\n/g, "<br>")}</p>
        `,
                    replyTo: email,
                });

                console.log("Email sent successfully");
                return res.json({
                    ok: true,
                    message: "Thanks — we received your message.",
                });
            } catch (error) {
                console.error("Error sending email:", error);
                return res.status(500).json({
                    ok: false,
                    message: "Error sending message. Please try again later.",
                    error: error.message,
                });
            }
        });
    });
