import urllib.request
url = urllib.request.urlopen("http://www.google.com")
print(len((url.read())))
