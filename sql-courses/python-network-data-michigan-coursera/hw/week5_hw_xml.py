#taking to urls designed to hand us data for our application

import xml.etree.ElementTree as ET
import urllib

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_292931.xml'

input = urllib.urlopen(url).read()

print 'Retrieving', input

stuff = ET.fromstring(input)
lst = stuff.findall('comments/comment')

#look for xpath syntax / replace tree
#counts = tree.findall('.//count')

chars = 0
sums = 0
for item in lst:
    chars = chars + len(item)
    sums = sums + int(item.find('count').text)
print 'Retrieved', chars, 'characters'    
print 'Count:', len(lst)
print 'Sum:', sums