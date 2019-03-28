import json
import requests
from flask import jsonify
# Get the response from the API endpoint.
response= requests.get("https://secret-harbor-51991.herokuapp.com/videos")
data = response.json()
#data = jsonify(all=response.txt)
#print(data)

#print(data["number"])
print(data[0]["name"])
print(data[0]["author"])
print(data[0]["url"])
print(data[0]["content"])


