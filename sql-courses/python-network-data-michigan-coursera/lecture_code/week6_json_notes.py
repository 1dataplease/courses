##Video 1: the below code is basically json1.py
import json

#json represents data as nested lists and dictionaries
data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
        },
    "email": {
        "hide": "yes"
        }
}'''



#deserialize it w load from string (str data)
#after you json.loads(str_in_json_form), 
#   it looks same but u can use it 2 get info
info = json.loads(data)

#output 'info' is dictionary with 3 keys, and 3 keyvalues 
#(one of keyvalues is list of 2)
#info[name], info[phone] w/ 1 keyvalue, info[email] w/ 2 keyvalues

print "Name:", info["name"]
print "Hide:", info["email"]["hide"]+'\n\n'

##the below code is basically json2.py

#this time, we are reading in a list that has dictionaries for each person
input_str = '''[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    } ,
    { "id" : "009",
    "x" : "7",
    "name": "Chuck"
    }
]'''

#json.loads(data_string)
#input is  data/input_str
json_info = json.loads(input_str)

#output json_info is a dict that looks the same
#array in json / list in python
print "User count:", len(json_info),'\n'

#iterate thru object 'item' in json_info list
for item in json_info:
    print "Name", item["name"]
    print "Id", item["id"]
    print "Attribute", item["x"]+'\n'



#json easier to work with. xml is more expressive

##Video 2+3: service-oriented architecture and web services
## take data from other sites/sources

# apps publish the rules other apps must follow to use service (API)
# they have servers, we hit their urls

# how orgs share data
 # provide service layer b/w systems
# sharing data can require adaptations/tweaks/duplicated data

# a service layer/cloud - works for existing software systems
# data in each application, they can be consumed by others

# ex researchers across institutions - myGrid

## Video 4 : accessing apis in python

#app prog interface
#defined set of rules to interface with a proram
#type in str, google api gives info


##the below is basically 
#geojson.py

#this url gets a json pg (derived from google api docs)
info_s = '''http://maps.googleapis.com/maps/api/geocode/json?\
sensor=false&address=Ann+Arbor%2C+MI'''

import urllib

#this opens the link, reads the contents (STILL A STRING)
g_json = urllib.urlopen(info_s).read()

#now u can parse this to return parts like location
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

#keep looping (until run out of api uses)
while True:
    #enter an address
    address = raw_input('Enter location: ')
    if len(address) < 2: break
    
    #adds address to end of serviceurl
    #to get to that json page containing location data
    #the urlencode adds the formatting automatically    
    url = serviceurl + urllib.urlencode({'sensor' : 'false',
                                         'address' : address})
#    printing this location url
    print 'Retrieving', url 
#    opens the location url, this is now a url handler
    url_2_read = urllib.urlopen(url)
#    turns url handler into a json string
    data = url_2_read.read()
    print 'Retrieved', len(data), 'characters'
    
    #try to load, but if cant, then js is just none
    # turns json str data into json object js
    try:
        js = json.loads(str(data))
    except:
        js = None
    
    #read in json, if status=ok or status not in json
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure to Retrieve ===='
        print data
        continue
    
    #takes outer dictionary, pretty prints w/ indent
    print json.dumps(js, indent=4)
    
    #1st result->geometry->location->lat/lng
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print 'lat:', lat, 'lng:', lng
    #take 1st location->formatted_address
    location = js['results'][0]['formatted_address']
    print location
    
#output would look like
# enter location: sf,ca
# retrieving googleapis.com/(entry)
# retrieved 1500 characters
# lat 42 lng -80
# SF, CA, USA
# enter location:

#6-6
#api and rate limiting

#limit rqsts/day, or they might demand api key

#dev.twitter.com/overview
#apps.twitter.com/app
#1. get the consumer and tokey key and secret (4 total)
#2. use these tokens to create urls 
#(with oauth num in it)
#it also gives us a hidden.py file with these 4 things

#the below is
## twurl.py
#only after getting twitter api done
#import hidden
import oauth

#how to do oauth signing py
#parameters is a dict
#username is a parameter, count is a parameter
#augment adds this stuff to make url, add sig, hit url w GET

def augment(url, parameters) :
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'],
                             secrets['token_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(\
    consumer, token=token, http_method='GET', http_url = url,\
    parameters = parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()

#below is
##twtest.py
    
from twurl import augment

print '* Calling Twitter...'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name' : 'makeitwain3000',
               'count' : '2'} )
print url

##api.twitter.com/1.1/statuses/user_timeline.json?count=2

#this is the body
connection = urllib.urlopen(url) 
data = connection.read()
print data

#get headers / metadata of http request
#tells us rate limit only 100 left in x-rate-limit-remaining
headers = connection.info(dict)
print headers

# look at json, friends list
# dev.twitter.com/rest/reference/get/friends/list

## twitter2.py

import json
import twurl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) :
        break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct,
                         'count' : '5'} )
    print 'Retrieving', url
    
    connection = urllib.urlopen(url)
    data = connection.read()         #reads the json body
    headers = connection.info().dict  # reads the header dict
    
    print 'Remaining', headers['x-rate-limit-remaining']
    
    js = json.loads(data)
    print json.dumps(js, indent = 4) #pretty prints json array of objcts
    #json turned into a py list, loop thru    
    for u in js['users']:
        print u['screen_name']
        s = u['status']['text']
        print '  ', s[:50]
        

#