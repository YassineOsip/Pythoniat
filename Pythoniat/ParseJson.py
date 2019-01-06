import json

data = [{"name" : "yassine" , "job" : "developer"}]


jsonn = json.dumps(data)
print(jsonn)
json_decode = json.loads(jsonn)
print(json_decode)