import os
from cohere import Client
from rich import print
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Cohere API client
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY environment variable is not set.")

co = Client(api_key=cohere_api_key)

# Collect system prompt context
print("Enter your system prompt context below. As an example it should be something like:")
print("'You are an experienced frontend developer who cares about readability'")
system_prompt = input("Leave blank for default: ")
if not system_prompt:
    system_prompt = "You are an experienced frontend developer who cares deeply about code readability."

# Collect user prompt
user_prompt = input("Enter your prompt: ")

# Combine prompts
final_prompt = f"{system_prompt}\n\nUser: {user_prompt}\nAssistant:"

# Generate response from Cohere API
response = co.generate(
    model="command-xlarge",  # Specify the Cohere model
    prompt=final_prompt,
    max_tokens=300,
    temperature=0.7,
    stop_sequences=["User:"]
)

# Print the generated response
print("\nHere is the response:\n")
print(response.generations[0].text.strip())
