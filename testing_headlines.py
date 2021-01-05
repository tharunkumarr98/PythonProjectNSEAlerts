import requests
new_API_Key = "d0b15badca204ad6a0d4711945ce3ac0"
parameters = {
    "apiKey": new_API_Key,
    "language": "en",
    "country": "IN",
    "category": "business",
    "q": "Jio"


}
reponse = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters)
print(reponse.json())
