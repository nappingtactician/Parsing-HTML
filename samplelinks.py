import urllib
from BeautifulSoup import *
j = 0
a = list()
url = raw_input('')
for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    q = tags[17].get('href',None)
    a.append(q)
    url = q
for name in a:
    w = name.split('_')
    e = w[2].split('.')
    print e[0]
       
