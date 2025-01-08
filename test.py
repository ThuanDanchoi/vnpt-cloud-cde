import cohere

api_key = "hQ3Cuu1x0GvcZ6zV7IGlFQ5cXDzawIht0tuj3PFe"
co = cohere.Client(api_key)

try:
    response = co.generate(prompt="Test API")
    print(response.generations[0].text)
except Exception as e:
    print("Lỗi khi kết nối Cohere:", e)
