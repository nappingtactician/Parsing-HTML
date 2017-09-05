import urllib
from BeautifulSoup import *
count = 0
url = raw_input('')
html =  urllib.urlopen(url).read()
print html
soup = BeautifulSoup(html)
tags = soup('span')

for tag in tags:
    for i in tag:
        w = int(i)
        count = count + w
print count
        
    
