import urllib
import json
import xml.etree.ElementTree as ET

##read the json data located at a url
## get the sum of all the count values for each student

#this is the prefix to the url with location data
serviceurl = 'http://python-data.dr-chuck.net/geojson?'


##when testing
#url_s = 'http://python-data.dr-chuck.net/comments_42.json'
##this is what we enter into the prompt later
url_s = 'http://python-data.dr-chuck.net/comments_292935.json'

#when submitting this hw
#url = raw_input('Enter location: ')
print 'Retrieving'+url_s


#this the json/url as a a url_handler, then as a string
page_s = urllib.urlopen(url_s).read()

#to convert a json string to an object to work with, loads
data = json.loads(page_s)

#goes through each single line
val = 0
for comment in data['comments']: 
    val = val + comment['count']
print val