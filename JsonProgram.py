import json

data = '{"var1":"Vishal","var2":"NB"}'
# print(data)["var1"] 'NoneType' object is not subscriptable
parsed = json.loads(data)
print(parsed["var1"])
data2 = {"Name": "NB",
         "Age": 24,
         "Food": ("Apple", "Grapes")
    , "isBbad": False}  #Run this in chrome console

jscomp=json.dumps(data2)
print(jscomp)
