import os
from fastapi import FastAPI, HTTPException
from cohere import Client
from dotenv import load_dotenv
from pydantic import BaseModel
from rich import print

# Load the .env file
load_dotenv()

# Fetch the Cohere API key
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY environment variable is not set.")

# Initialize the Cohere client
co = Client(api_key=cohere_api_key)

# Initialize the FastAPI app
app = FastAPI()

# Define a request model
class CohereRequest(BaseModel):
    system_prompt: str
    user_prompt: str

@app.post("/generate")
async def generate_response(request: CohereRequest):
    """
    Generate a response using Cohere's API.
    """
    try:
        # Combine system and user prompts
        final_prompt = f"{request.system_prompt}\n\nUser: {request.user_prompt}\nAssistant:"

        # Generate response using Cohere's API
        response = co.generate(
            model="command-xlarge",
            prompt=final_prompt,
            max_tokens=300,
            temperature=0.7,
            stop_sequences=["User:"]
        )
        
        res_content = response.generations[0].text.strip()

        return {"response": res_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For testing the API locally
if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server for Cohere integration...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
