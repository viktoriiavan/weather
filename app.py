import requests

api_key = ""
api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Write your city:")

response = requests.get(
 url = api_url,
 params={
     "q": city,
     "appid": api_key,
     "units": "metric"
 }   
)

weather_data = response.json()
print(city, "temperature is", weather_data['main']['temp'])