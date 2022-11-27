import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter URL:-')
count = int(input('Enter count:-'))
position = int(input('Enter position:-'))

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    cnt = 0
    ps = 0
    for tag in tags:
        ps = ps + 1
        if ps == position:
            url = (tag.get('href',None))
            print(url)
            
    
            
    
