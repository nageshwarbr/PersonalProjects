import requests
import json

r = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo")
text = r.text
# print(type(text))
parsed = json.loads(text)
print(text)
print(r.status_code)
# print(parsed["zip"])
