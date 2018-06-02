import urllib
import sqlite3
import json
import time
import ssl
import os

os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\python-databases coursera')

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("data/where.data")
count = 0
for line in fh:
    if count > 200 : break
    address = line.strip()
    print ''
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (buffer(address), ))

    try:
        data = cur.fetchone()[0]
        print "Found in database ",address
        continue
    except:
        pass

    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url
    
    # breaks here if not online
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1
    try: 
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except: 
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print '==== Failure To Retrieve ===='
        print data
        break

    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    conn.commit() 
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can visualize it on a map."
#5-4 geocoding api demo
# more details on notes from 5-1

#import urllib, time

# base service api to use
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

# conn is like a file handler
conn = sqlite3.connect('geodata.sqlite')

# cursor is like subconnection
cur = conn.cursor()

# if doesnt exist, create table locations w cols address and geodata
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

#where.data is typed in locations from survey
fh = open("data/where.data")
count = 0
for line in fh:
    
    #just do 200 so it doesnt run for forever
    if count > 200 :
        break
    
    # just strip the whitespace out. each line is an address typed in
    address = line.strip()
    
    print ''

    # 1st time thru, we wont have this info
    # for this address
    # get geodata col from locations table
    # buffer address turns it from unicode to whatever our setup is
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", 
                (buffer(address), ))

    # TRY to read what we selected for above (since not in db yet)
    try:
        data = cur.fetchone()[0]
        print "Found in database ",address
        continue
    # wont have it 1st time thru, pass to below
    except:
        pass

    print 'Resolving', address

    # create var url that is url + urllib.urlencode(no sensor, address)
    url = serviceurl + urllib.urlencode({"sensor":"false", 
    "address": address})

    print 'Retrieving', url

    # this opens the above url, gives context of py2 if needed
    # url handler
    uh = urllib.urlopen(url, context=scontext)
    # read the above string and change it from pointer to a string
    data = uh.read()

    print 'Retrieved',len(data),'characters', \
    data[:20].replace('\n',' ')
    
    # count is to keep track for going to 200
    count = count + 1
    
    # check if we got good data
    # if this doesnt work, its bad json, handle with below if stmt
    try:
        # if unicode, converts to str.
        # then turn the str data into a list of lists
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except: 
        continue

    # status variable is in json
    # if its not there or not 'ok' AND status is not zero results
    # print, go to next location row
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print '==== Failure To Retrieve ===='
        print data
        break

    # finally inserting the address and data into locations db
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    conn.commit() 
    
    # just so it doesnt outrun itself
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can \
visualize it on a map."