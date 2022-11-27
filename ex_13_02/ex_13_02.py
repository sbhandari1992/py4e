import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter - ")
js_url = urllib.request.urlopen(url)
data = js_url.read().decode()

js = json.loads(data)
dic = js["comments"]
sum = 0
for v in dic:
    sum = sum + (v["count"])
print(sum)
