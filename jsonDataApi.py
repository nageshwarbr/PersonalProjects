import json
import requests

response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
source = json.loads(response.text)
data = json.dumps(source,indent=2,sort_keys=True)
print(data)
