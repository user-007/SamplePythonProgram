import requests

prompt = input("Which year do you want to travel to?")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
