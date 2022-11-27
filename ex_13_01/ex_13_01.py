import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter - ")
xml = urllib.request.urlopen(url)
data = xml.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
sum = 0
for items in results:
    nums = int(items.find('count').text)
    sum = sum + nums
print("Sum : ",sum)
