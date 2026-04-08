import requests

api_key = "bfc3b4fc154fb833a00c2425e5b229e3"

municipality = input("Enter the name of a municipality: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

response = requests.get(url).json()

description = response["weather"][0]["description"]
temperature = response["main"]["temp"]

print(f"Weather: {description}")
print(f"Temperature: {temperature} °C")

