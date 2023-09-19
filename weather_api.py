import requests

# API key

url = 'http://api.weatherapi.com/v1/current.json?key=231a56d097934e9083e52248231709&q=egypt&aqi=no'
response = requests.get(url)

weather_data = response.json()

temp = weather_data.get("current").get("temp_c")

print(weather_data)
