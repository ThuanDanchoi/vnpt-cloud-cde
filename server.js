const express = require('express');
const bodyParser = require('body-parser');
const cohere = require('cohere-ai');
require('dotenv').config();

const app = express();
cohere.init(process.env.COHERE_API_KEY);

app.use(bodyParser.json());

app.post('/generate', async (req, res) => {
    const { prompt } = req.body;
    const response = await cohere.generate({
        model: 'xlarge',
        prompt: prompt,
        max_tokens: 100
    });
    res.json({ text: response.body.generations[0].text });
});

app.listen(8080, () => console.log('Server running on port 8080'));
