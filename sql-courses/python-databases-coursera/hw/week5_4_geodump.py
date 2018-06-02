import sqlite3
import json
import codecs
import os

os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\python-databases coursera')

# now that we have a db, read it and write all info to where.js
# where.js already had some logic to handle it as a map
# this just feeds it the data
#geodump.py

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# get all rows
cur.execute('SELECT * FROM Locations')

# opens existing js file that turns db into a display
fhand = codecs.open('data/geodata/where.js','w', "utf-8")

# 
fhand.write("myData = [\n")

count = 0

# for each row in what our select * returned
for row in cur :
    
    # data is str of the 2nd col in the db, the geodata
    data = str(row[1])

    # try to load that string into a list of lists    
    try: 
        js = json.loads(str(data))
    # if fails, just skip and let it thru next test
    except: 
        continue

    # if the list has a status but it isnt ok, skip to below    
    if not('status' in js and js['status'] == 'OK'): 
        continue

    # gets the results, checks 1st item, then geo>location>lat
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    
    # if either is 0, means broken, skip it
    if lat == 0 or lng == 0 :
        continue
    
    # this gets a cleaner address
    where = js['results'][0]['formatted_address']

    # replace ' with blank for readability
    where = where.replace("'","")
    
    # try to print location, lat, lng
    try:
        print where, lat, lng
        
        # would add to count
        count = count + 1
        
        # for all the rows that arent first
        # write a newline to the fhandler (will save it to where.js)
        if count > 1: 
            fhand.write(",\n")
        
        # format the 3 values so each row is '['lat', 'lng', 'loc']'
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        
        # write it to the output, first appearence of output
        fhand.write(output)

    except:
        continue

# write a newline, ]; newline
fhand.write("\n];\n")
cur.close()
fhand.close()
print count, "records written to where.js"
print "Open where.html to view the data in a browser"
