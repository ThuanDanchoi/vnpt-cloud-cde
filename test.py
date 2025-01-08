import cohere

api_key = "API_KEY_CUA_BAN"
co = cohere.Client(api_key)

try:
    response = co.generate(prompt="Test API")
    print(response.generations[0].text)
except Exception as e:
    print("Lỗi khi kết nối Cohere:", e)
