import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

json_response = response.json()

print(f"Joke: {json_response['value']}")


