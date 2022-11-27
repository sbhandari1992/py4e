import urllib.request, urllib.parse, urllib.error
import json

surl = 'http://py4e-data.dr-chuck.net/json?'

loc = input('Enter location:')

url = surl + urllib.parse.urlencode({'address': loc,'key': 42})
print(url)
data = urllib.request.urlopen(url).read().decode()
js = json.loads(data)
print(js)
print(json.dumps(js, indent=4))

print(js['results'][0]['place_id'])
