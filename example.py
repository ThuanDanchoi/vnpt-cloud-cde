import cohere

co = cohere.Client("hQ3Cuu1x0GvcZ6zV7IGlFQ5cXDzawIht0tuj3PFe")

response = co.generate(
    model="command-xlarge-nightly", 
    prompt="Hello world!",  
    max_tokens=50,        
    temperature=0.5         
)

print(response.generations[0].text)
