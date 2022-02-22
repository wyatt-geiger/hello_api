"""This program is used to display a forecast of every 3 hour interval for the next 5 days. It asks the user to enter
a city and a two-letter country code and pulls the data from a live website using an API. These results are then displayed
to the user and include information such as the temperature, a formatted timestamp, weather description, and wind speed
for every 3 hour interval."""

import requests
import os
import logging
from datetime import datetime
# import necessary libraries

def weather_key(city, country):

    key = os.environ.get('WEATHER_KEY') # get the key value stored in the WEATHER_KEY environment
    query = {'q': f'{city},{country}', 'units': 'imperial', 'appid': key}
    # query string that uses a dictionary to store location, units, and the API key

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    # variable to store the API url

    data = requests.get(url, params=query).json()
    # creates a request using the url and the sets the parameters of the url to what's contained inside the query string

    return data['list']
    # returns API request to be used later in the program

def forecasts(list_of_forecasts):

    for forecast in list_of_forecasts:
        temp = forecast['main']['temp']
        timestamp = forecast['dt']
        desc = forecast['weather'][0]['description']
        wind_speed = forecast['wind']['speed']
        forecast_date = datetime.fromtimestamp(timestamp)
        # using the API request from weather_key method, this for statement looks through the API
        # and gathers the request information. information the API is stored as a list, and
        # all components are called upon like a list would be

        print(f"Date: {forecast_date} --- Forecasted temperature: {temp}F --- Weather Description: {desc} --- Wind Speed: {wind_speed} mph")
        # print statement using a format string that displays the forecast every 3 hours for the next 5 days
        # this will be printed multiple times for every 3 hour interval

def main():

    try:
        city = input('Which city\'s forecast would you like to view? ')
        country = input('Which two letter country code is that city located in? ')
        # asks the user for a city and country code

        list_of_forecasts = weather_key(city, country)
        # uses the user input to generate the list of forecasts

        forecasts(list_of_forecasts)
        # method to print every forecast in the list of forecasts

    except KeyError as e: # error handler
        logging.log(40, 'KeyError -- invalid input')
        # error logger
        print('You did not enter a valid city and/or country code.')
        # error message for the user

main()