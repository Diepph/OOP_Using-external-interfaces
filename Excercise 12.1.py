"""
Write a program that fetches and prints out a random Chuck Norris joke for the user.
Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.
"""
import json
import requests

#keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()

print(json.dumps(response, indent=2))

print(response["value"])