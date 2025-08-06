import json as js

json_data = '{"name":"June","contact":{"email":"june@example.com","city":"Paris"}}'

data = js.loads(json_data)

print(data["contact"])