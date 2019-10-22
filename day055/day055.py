# Day55
import json

# json format
x = '{"name":"John", "id":200, "city":"New York"}'

# parse x
y = json.loads(x)

# convert to json

z = json.dumps(y)
print(x)
print(y['name'])
print(z)