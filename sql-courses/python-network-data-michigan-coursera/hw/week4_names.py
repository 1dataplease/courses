import urllib
from BeautifulSoup import *

#url1 = raw_input('Enter - ')

#one of these must be active, the other commented out
#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Matthias.html'



loops = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))

#html = urllib.urlopen(url2).read()
#soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
#tags = soup('a')

#current_pos = 1
#current_loop = 0

#names_on_page = []
#names = []

for i in range(loops):
    names_on_page = []
    names = []    
    
    html_reader = urllib.urlopen(url).read()
    parser = BeautifulSoup(html_reader)
    a_tags = parser('a')
    for tag in a_tags:
        site = tag.get('href', None)
        names_on_page.append(site)
    names.append(names_on_page[pos-1])
    print 'Retrieving:', names_on_page[pos-1]
    url = names_on_page[pos-1]

print '\nThe answer to the assignment for this execution is ', url

#for tag in tags:
#
#    tag.get('href')    
#    tag_str = str(tag)
#    ##more stuff    
#    
#    current_pos = current_pos + 1
#    if current_pos == pos:
#        print 'Retrieving:', tag.get('href', None)   
#        current_loop += 1
#        urllib.urlopen(tag.get('href', None))
#        current_pos = 0
#    if current_loop == loops:
#        break

