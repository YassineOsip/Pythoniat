import requests
r  = requests.get("https://data.fixer.io/api/latest")
print(r.json)
print(r.text)
print(r.status_code)
print(r.history)
