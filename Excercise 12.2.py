"""
Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. 
Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text 
and temperature in Celsius degrees. 
Take a good look at the API documentation. 
You must register for the service to receive the API key required for making API requests. 
Furthermore, find out how you can convert Kelvin degrees into Celsius.
"""

import json
import requests


city_name = input("Enter city name: ")
api_key = "bb39cfd32bb45e242a62209ddf4a095e"

request = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
response = requests.get(request).json()
#print(json.dumps(response, indent=2))

lat = response[0]["lat"]
lon = response[0]["lon"]
request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(request).json()
#print(json.dumps(response, indent=2))
description = (response["weather"][0]["description"])
temp = (response["main"]["temp"])
#print(description, temp)

temp_celcius = temp - 273.15
print(f"The weather of {city_name} is {description} with {temp_celcius} Celcius")





