import urllib.request

url = "https://www.google.com"
req1 = urllib.request.Request(url)
resp1 = urllib.request.urlopen(req1)
resp_read = resp1.read()

print(resp_read)