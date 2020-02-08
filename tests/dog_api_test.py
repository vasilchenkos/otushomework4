import requests

response = requests.get("https://dog.ceo/api/breed/hound/images")

print(response)