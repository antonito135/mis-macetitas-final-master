import requests

response = requests.get('https://dbd-api.herokuapp.com/survivors').json()

print(response)