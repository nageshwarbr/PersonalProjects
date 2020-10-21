import json

people_string = '''
{"people":[
{
"name":"Johann",
"phone":"9802939329",
"emails":["jhan@gm.com","johann@hm.com"],
"has_license":false},
{
"name":"Damien",
"phone":"9888839329",
"emails":null,
"has_license":true
}
]
}
'''
data = json.loads(people_string)
# print(data['people'])
# print(type(data))
#
# for names in data['people']:
#     print(names['name'])

for persons in data['people']:
    del persons['phone']
print(data)

data=json.dumps(data,indent=2,sort_keys=True)
print(data)