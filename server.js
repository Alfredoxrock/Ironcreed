const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static site from project root
app.use(express.static(path.join(__dirname)));

// Simple contact endpoint
app.post('/api/contact', (req, res) => {
    const { name, email, message } = req.body || {};
    console.log('Contact submission received:');
    console.log({ name, email, message });

    // In a real app, store or email this data. For now return success.
    res.json({ ok: true, message: 'Thanks — we received your message.' });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
