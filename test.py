import requests

# Replace with your API key and the city you want
api_key = "99ad70778da1442c33c5f732cea9e11f"
city = "London,GB"

# URL to get weather data
url = f"https://api.openweathermap.org/data/2.5/weather?lat=40.7128&lon=-74.0060&appid=YourAPIKey"

response = requests.get(url)
data = response.json()

print(data)
