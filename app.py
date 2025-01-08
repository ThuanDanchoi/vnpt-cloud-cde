import os
from flask import Flask, request, jsonify
import cohere
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
co = cohere.Client(os.getenv("COHERE_API_KEY"))

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    response = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=100
    )
    return jsonify({'text': response.generations[0].text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
