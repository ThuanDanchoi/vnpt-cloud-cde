import cohere

API_KEY = "hQ3Cuu1x0GvcZ6zV7IGlFQ5cXDzawIht0tuj3PFe"
co = cohere.Client(API_KEY)

def generate_code(prompt):
    response = co.generate(
        model='command-xlarge',
        prompt=prompt,
        max_tokens=100,
        temperature=0.5
    )
    return response.generations[0].text

if __name__ == "__main__":
    prompt = "Write a Python function to calculate Fibonacci numbers"
    result = generate_code(prompt)
    print("Generated Code:\n", result)

