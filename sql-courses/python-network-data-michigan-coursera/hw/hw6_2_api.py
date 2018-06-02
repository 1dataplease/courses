import urllib
import json

#put in location like South Federal University
#it returns the placeID

#this is the site we are using, not google
serviceurl = 'http://python-data-dr-chuck.net/geojson?'

#enter location once script works
location = 'Saint Petersburg State University of Aerospace Instrumentation'
#location = raw_input('Enter location: ')

#if len(location) < 2:

#this adds to end of serviceurl to get to info_s url
url = serviceurl + urllib.urlencode({'sensor' : 'false',
                                     'address' : location})
print 'Retrieving', url #printing this url
urlhand = urllib.urlopen(url) #open url
data = urlhand.read() #reads the json
print 'Retrieved', len(data), 'characters'

#if data is bad, can blow up
try:
    js = json.loads(str(data))
except:
    js = None

#read inside of json, if status=ok or status not in json
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure to Retrieve ===='
    print data

#takes outer dictionary, pretty prints it w/ indent so readable
print json.dumps(js, indent=4)

#    lat = js['results'][0]['geometry']['location']['lat']
#    lng = js['results'][0]['geometry']['location']['lng']
#    print 'lat', lat, 'lng', lng
#    location = js['results'][0]['formatted_address']
#    print location

placeID = js['results'][0]['place_id']
print placeID
    
#output looks like
# enter location: sf,ca
# retrieving googleapis.com/(entry)
# retrieved 1500 characters
# lat 42 lng -80
# SF, CA, USA
# enter location:
