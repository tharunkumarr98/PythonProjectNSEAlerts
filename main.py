from nsetools import Nse
from pprint import pprint
import smtplib
import requests
with open("credentials.txt") as cred:
    data = cred.readlines()
    new_API_Key = "d0b15badca204ad6a0d4711945ce3ac0"
    user_name = data[1]
    password = data[2]
    to_ADD = data[3]
print(type(password))
parameters = {
    "apiKey": new_API_Key,
    "language": "en",
    "country": "IN",
    "category": "business",
    "q": "Reliance"


}
response = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters)
response.raise_for_status()
response_dictionary = response.json()
news =""
for i in range(len(response_dictionary['articles'])):
    print(i)
    source_url = response_dictionary['articles'][i]['url']
    description = str(response_dictionary['articles'][i]['author'])
    source_website_name = response_dictionary['articles'][i]['source']['name']
    news += source_website_name + "\n" + description + "\n" + source_url + "\n"
# fetching data from NSE
nse = Nse()
pprint(nse.get_quote('RELIANCE'))
msg = nse.get_quote('RELIANCE')
day_opening_price = str(msg["open"])
day_closing_price = str(msg["closePrice"])
change_in_price = str(msg["change"])
sending_message = "Opening Price: " + day_opening_price + "\n" +"Closing Price: " + \
                  day_closing_price + "\n" + "Change in Price (%): " + change_in_price + "\n\n" + f"{news}"


# creating alert and sending email

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = user_name, password = password)
    connection.sendmail(from_addr = user_name,
                        to_addrs= to_ADD , msg = f"Subject: Reliance Price alert \n\n {sending_message}")
