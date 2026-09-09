import requests
import json

url = "http://universities.hipolabs.com/search?country=Brazil"

req = requests.get(url)

data = req.json()

json.dump(data, open("universidade_brasil.json", "w"))

