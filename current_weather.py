from pprint import pprint
import requests
import os

key = os.environ.get('WEATHER_KEY')

url = 'https://api.openweathermap.org/data/2.5/weather'
query = {'q': 'minneapolis', 'units': 'imperial', 'appid': key}

data = requests.get(url, params=query).json()

current_temp = data['main']['temp']

print(f'The current temperature is: {current_temp}F')
