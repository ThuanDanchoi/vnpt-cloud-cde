import os
import cohere
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(COHERE_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the AI Text Generation API! Use the /generate-text endpoint to generate text."})

@app.route("/generate-text", methods=["POST"])
def generate_text():
    try:
        data = request.json
        prompt = data.get("prompt", "Default prompt if none provided")

        response = cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )

        generated_text = response.generations[0].text.strip()
        return jsonify({"generated_text": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

