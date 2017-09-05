import urllib
from BeautifulSoup import *
count = 0
lst1 = list()
lst2 = list()
lst3 = list()
lst4 = list()
lst = list()
url = raw_input('')
a = 2

for i in range(1,a):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print tags
    for tag in tags:
        x = tag.get('href',None)
        lst.append(x)
        q = lst[2]
        q = url
        lst1.append(q)
        print lst
   
