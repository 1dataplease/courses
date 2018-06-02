# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:07:42 2017

@author: wainman
"""

#tracks.py
#this is to read the xml
import xml.etree.ElementTree as ET
import sqlite3

#1 - establish connection creating file, and a cursor to run sql
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

#create some empty tables to fill up the xml data with

#want a track table first
#track contains id, title, rating, len, count, album_id (fgn key)

#then build albums (tracks are on an album)
#albums has id, title (logical key, shortcuts to get to)
#albums belong to artist

#artist has id, name

#Genre belongs to track
#Genre has id, name

#build them in reverse

# drop artist, album, track tables if they exist
# for lecture, created artist, album, track
# in week3 hw1, create genre also
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# enter the file
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'data/Library.xml'

# looks thru entire dict for that data we want
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    # child refers to each line that has a key and a data
    for child in d:
        
        # if switched to found below, then just return line's text
        if found: 
            return child.text
            
        # if the childs tag is key (most are)
        # and if it has a str = to our input, change found to T
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# just give it a filename, ET can turn it into an object
stuff = ET.parse(fname)

#look for any where dict in dict in dict
d3 = stuff.findall('dict/dict/dict')

# this just prints out the num of times there are d in d in d
print 'Dict count:', len(d3)

#entry is the xml obj that represents a dict obj
for entry in d3:
    
    # if find none, not a real track line/tag, skip it
    if ( lookup(entry, 'Track ID') is None ):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # if all 3 of keys we found have empty data, skip it
    if name is None or artist is None or album is None : 
        continue

    print name, artist, album, count, rating, length

    # cant insert the same artist or album or track name twice
    # if something goes wrong ie name already in it, then ignore
    cur.execute(
    '''
    INSERT OR IGNORE INTO Artist (name)
    VALUES ( ? )
    ''', 
    #the ? is replaced by our data artist                
        ( artist, ) )
    
    #then select the artist id where name = artist
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))

    # assign this select statement to artist_id by grabbing 1st elem
    artist_id = cur.fetchone()[0]

    # album table
    # insert the album title and artist_id from above
    # album is lower table, points to artist_id
    cur.execute('''
    INSERT OR IGNORE INTO Album (title, artist_id) 
    VALUES ( ?, ? )
    ''', 
    ( album, artist_id ) )
    
    # select the album
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    
    #set var album_id: fetchonerow, grab first thing   
    album_id = cur.fetchone()[0]

    #track table
    # insert would fail if logical key already there
    # insert name, album_id, length, rating, count
    # all of which were gathered in the lookup
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )

    conn.commit()