import requests

# r=requests.get("http://africau.edu/images/default/sample.pdf")
#
# with open("sample.pdf","wb") as f:
#     f.write(r.content)


# payload={'page':2,'count':25}
# r=requests.get("https://httpbin.org/get")
#
data = {'data': 'vishal','passkey':'Vishal @ 133'}
r = requests.post("https://httpbin.org/post", data=data)
r_dict=r.json()
print(r_dict['form'])

# print(r.text)
