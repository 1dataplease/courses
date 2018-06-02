# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:13:05 2017
@author: wainman
"""

import sqlite3
import os
import pandas as pd
import xml.etree.ElementTree as ET
import json
import urllib
import time
import codecs

os.chdir('C:\\Users\\wainman\\Desktop\\tw\\classes\\python-databases coursera')

##1-1
##objects, like classes, intro - howd we'd use it without objects
##input, process, output
#usf = input('enter the us floor number: ')
#wf = usf - 1
#print 'non-us floor number is', wf

#make a list of dictionaries, movies attributes are key:value pairs
movies = []

movie1 = {}
movie1['director'] = 'james cameron'
movie1['title'] = 'avatar'
movie1['release date'] = '18 december 2009'
movie1['run time'] = '162 minutes'
movie1['rating'] = 'PG-13'

movie2 = {}
movie2['director'] = 'david fincher'
movie2['title'] = 'the social network'
movie2['release date'] = '01 october 2010'
movie2['run time'] = '120 minutes'
movie2['rating'] = 'PG-13'

movies.append(movie1)
movies.append(movie2)

# but we could misspell. easier to write code like this

#here are requirements of data for all movies / data model / schema
attr_keys = ['title', 'director', 'rating', 'run time', 'release date']

#this will seperate then print the ugly looking list containing dicts
print '========'
print movies
# this seperate, then print the data requirements for all movies
print '======='
print attr_keys

#seperate each movie, then each line has attr: movie[attr]
for movie in movies:
    print '======'
    for attr in attr_keys:
        print attr, ': ', movie[attr]

print '======'


#1-2 - what is an object
#fxn is only code
#obj is code and data

#ex. program that uses sql - hide that complexity
#input -> object -<> str <> dict -> object2 -> output


#1-3 - terminology

#class - a template/blueprint describes pattern, all attrs of one type. 
#ex: dog, football-team, course

# method or msg - a defined ability or fxn the class can do
# ex: bark, sign-FA, view video1
#all strings have a startswith method

# field or attribute - a bit of data in a class
#ex: height, location, cost

# object or instance - a value or case or instance of a class
#ex: lassie, 49ers, data-analysis-mich
# the variable, x,y,z- 40 instances of a string object or string class


#1-4 - simple python objects
#write a sample class

class PartyAnimal:
    
    # each party animal object has this bit of data when first assigned
    x = 0

    #optional constructor - used to set up variables
    def __init__(self):
        print 'i am constructed'

    # after creating the object PartyAnimal() and assigning it to variable    
    #this is the one fxn or method it has
    # this takes current value, adds 1, prints so far 2, 3, etc.
    # the parameter is conventionally self, more after this
    # 
    def party(self):
        self.x = self.x + 1
        print 'so far', self.x
        
    #optional destructor - this will print / destruct at the end of the program
    def __del__(self):
        print 'i am destructed', self.x

#create an object or instance
an = PartyAnimal()

# below is like a short-form of PartyAnimal.party(an)
an.party()
an.party()
an.party()

# show what the type is (an is an instance), then show what its methods are
print 'type: ', type(an)
print 'dir: ', dir(an)

#self refers obj to its self. self.x is x within self. self is global within obj

#were making new types of variables - more than just int, bool, etc

#create instance or object of list class, assign to x
x = list()

# says the type of class
type(x)

# show all the capabilities like the methods/operations list the x obj can do
# underscore ones are used by python itself, not by us
dir(x)


#1-5 - object lifestyle

# objects created used, discarded
# methods that get called
#   at the moment of creation (constructor)
#   at the moment of destruction (destructor), seldom used

#constructors primary purpose
# set up some instance variables to have the proper initial values 
#   when the instance is created

# class is the template for objects
# create lots of objects
# store each distinct object in its own variable
# call this by having multiple objects of the same class
# each object has its own copy of the object variables

#now add instance variable name
# add parameter name when constructing

class NamedPartyAnimal:
    
    # each party animal object has this bit of data when first assigned
    x = 0
    name = ""
    
    #optional constructor - used to set up variables
    def __init__(self, nam):
        self.name = nam
        print self.name, 'is constructed'

    # after creating the object PartyAnimal() and assigning it to variable    
    #this is the one fxn or method it has
    # this takes current value, adds 1, prints so far 2, 3, etc.
    # the parameter is conventionally self, more after this
    # 
    def party(self):
        self.x = self.x + 1
        print self.name, 'party count', self.x

s = NamedPartyAnimal('sally')
s.party()

j = NamedPartyAnimal('jon')
j.party()
s.party()


#1-6 - inheritance
# class b can extend class a

#when we make new class, can reuse an existing class
# inherit all the methods, add our own bit to make new class

#subclass
#specialized version of a class, inheriting attributes and methods from parent
# while introducing new ones

class FootballFan(NamedPartyAnimal):
    points = 0
    
    def touchdown(self):
        self.points += 7
        print self.name, 'scored', self.points, 'points'
        self.party()

b = FootballFan('bill')
b.party()
b.touchdown()

#touchdown made him party first, getting to 2. then has 7 points. corrected

# can group data and functionality together to 
# create independent objects of a class


#2-1 - basic sql
# read into db. easier to re-analyze anytime

# use python to read/write files
#sqlitebrowser.org
#chrome plug-in 

#relation databases
#model data by storing rows and columns in tables
# efficiently retrieve data from tables
# in particular where there are multiple tables and relationships bw them
# involved in the query

#used to have small data, tapes for each days bank balances
# disc-drives
#random access medium/memory
# to get to s, dont have to read a-r

#db - contains many tables
# table/relation - set that contains tuples/rows and attributes/columns
# tuple/row - set of fields that represents an 'object' like person or song
# attribute/column/field - one of many elements of data on the row object

# model data at a connection point

# 7 min

#schema
#rules of each columns data type, and the column names

#CRUPD
#create table, retrieve data, insert data, delete data


#2-2 - using databases

#large project - website to track something
# app developer - write app, look+feel, fix bugs
#   write code that talks to the database data server w sql

# dba - schema, tune, monitor
#   can talk to the database - has database tools for speed etc

#small project

# write sql, talk to the db thru the software - create, put data in sqlite browser
# then write the python programs to talk to the db file

# input files like csv or network, clean it, use py to write data into db
# py script to read data, make a pretty file -> r, excel, d3.js pictures

# database model/schema is the structure/format - formal language

#db systems - oracle, mysql (simpler), sqlserver or access, hsql, sqlite, postgres
# marai db is similar to mysql, which oracle owns now - website stuff

#sqlite is enbedded db, part of many apps and in python


# 2-3 0 single table crud

# can get sqlite-manager in mozilla

# in dbbrowser for sqlite
# new db > save as 2-3-sql1-from-lecture > execute sql

#CREATE TABLE Users(
#name VARCHAR(128),
#email VARCHAR(128)
#);

# browse data > insert 4 rows of data
# or can do it in sql queries
#INSERT INTO Users (name, email)
#VALUES ('Kristin', 'kf@umich.edu');

#delete
#DELETE FROM Users 
#WHERE email='fred@umich.edu';

#change value in cell
#UPDATE Users
#SET name="Charles"
#WHERE email = 'csev@umich.edu';

#retrieve
#SELECT * FROM Users
#WHERE email = 'csev@umich.edu';

#order by
#SELECT * FROM Users
#ORDER BY name


##week2 HW1 - our 1st db
##instructions
##1 - create a db Ages with 
#CREATE TABLE Ages ( 
#  name VARCHAR(128), 
#  age INTEGER
#)

##2 - insert only these rows with these commands
#INSERT INTO Ages (name, age) VALUES ('Phinehas', 32);
#INSERT INTO Ages (name, age) VALUES ('Roan', 25);
#INSERT INTO Ages (name, age) VALUES ('Rheanan', 34);
#INSERT INTO Ages (name, age) VALUES ('Elli', 29);
#INSERT INTO Ages (name, age) VALUES ('Riya', 40);
#INSERT INTO Ages (name, age) VALUES ('Millan', 21);

##3 - run
#SELECT hex(name || age) AS X FROM Ages ORDER BY X

##4 - find first row, enter long string that looks like 53656C696E613333
#456C6C693239


#week2 HW2 - email counter
#reads data/mbox.txt, counts emails per domain
#   for speed, consider moving commit operation outside the loop

#create connection
# it creates a sqlite file with title emaildb in the wd
conn = sqlite3.connect('data/emaildb.sqlite')
# create cursor, then can send commands through our cursor 
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# txt to read in. txt has many emails sent/recieved
# we input the filename
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'data/mbox.txt'

# file handler is the open version of the filename we input
fh = open(fname)


# where org = ? finds 

for line in fh:
    # for line in file, only look at lines starting w 'from'
    if not line.startswith('From: '): continue
        
    # turn each line into a list, each word in line is element
    pieces = line.split()
    
    #email always in 2nd piece or word of the line    
    email = pieces[1]
    
    # strip any whitespace surrounding it    
    email = email.strip()
    
    # org is everything after the @
    org = email[email.find('@')+1:]
    
    # ? is placeholder, (org, ) is whats substituted in for the ?
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))

    # this brings 1 row into memory as a list
    # this allows us to run different commands ~ row conditions
    row = cur.fetchone()
    
    # if we got 0 rows, insert org and count 1
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    
    # if that row was already in, then count += 1
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))

    # write it back to the disk
    conn.commit()

# https://www.sqlite.org/lang_select.html

#this is what shows the org, count orderered by highest
# only show the top 25 orgs so it doesnt go on too long
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 25'

#print break line, then counts
print
print "Counts:"

#for row in the above selection of queries
# print string of the org, count
for row in cur.execute(sqlstr) :
    # use str because can have funny characters not quite utf8
    print str(row[0]), row[1]

cur.close()

#was previously getting 508 because had a partial copy of mbox
#now correctly getting 536


#3-1 - designing a data model
#logical model
#music mgr app

#db design - clean, ez understand, ppl can tune

# building data model
# draw picture of data objects
#figure out how to represent them and their relationships

#dont put the same string data in twice, use relationship instead
# when theres 1 ex of it in real world, should only be 1 in db

#ex. how do we get to my songs in itunes
# track, len, artist, album, genre, rating, count

# efficiency
#not good having same artist name, album, genre many times

# data model exercise - start with ui, change data model to rep it

# for each piece of info - rep thing in real world? or attr of thing?

# 0 - where to start - the thing most essential to the application
# what is each row
# plays songs

# 1 - build track table
# track attrs include len, count, rating

# 2 - what isnt part of track necessarily
# album, artist, genre are real things on their own

# 3 - albums have tracks, album table
# tracks belong to albums, albums belong to artists

# 4 - genre?
# changing a track, it only changes the one song
# each track can have its own genre


#3-2 - implementing data model in tables
# physical model
# each table, go thru cols, possibly assign 
# primary, logical, foreign key

# track table: primary key ID, logical key title, album_id fgn key
# also len, count, rating
# genre_id fgn key

# album table: primary key ID, logical key title, artist_id fgn key

# artist table: primary key ID, logical key name

# genre table: primary key ID, logical key name

# 1 - open sqldb - use existing db (or new db, used new db)
#work from outward in, artists, genre, album, tracks

##artist table first
#CREATE TABLE 'Artist' (
#id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#name TEXT
#);
#
##genre table
#CREATE TABLE 'Genre' (
#id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#name TEXT
#);
#
#CREATE TABLE 'Album' (
#id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#title TEXT
#);
#
#CREATE TABLE 'Track' (
#id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#title TEXT,
#album_id INTEGER,
#genre_id INTEGER,
#len INTEGER, count INTEGER, rating INTEGER
#);


#3-3 - inserting data into tables we created

## in dbrowser
## not specifying id field, it auto increments
##1st artist table
#INSERT INTO Artist (name) values ('Led Zepplin');
#INSERT INTO Artist (name) values ('AC/DC');
#
##2nd genre table
#INSERT INTO Genre (name) values 'Rock';
#INSERT INTO Genre (name) values 'Metal';
#
##3rd album title - we need to put in a foreign key for artist
## we added Led Zep 1st, so that artist_id is 1
#INSERT INTO Album (title, artist_id) values ('IV', 2);
#INSERT INTO Album (title, artist_id) values ('Who Made Who', 1);
#
##4th track table
## cols are title, rating, len, count, album_id, genre_id
#INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
#VALUES ('Black Dog', 5, 297, 0, 2, 1);
#
#INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
#VALUES ('Stairway', 5, 482, 0, 2, 1);
#
#INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
#VALUES ('About to Rock', 5, 313, 0, 1, 2);
#
#INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
#VALUES ('Who Made Who', 5, 207, 0, 1, 2);


#3-4 joins

#by removing replicated data, faster - web of info

## if we want to see the album title and artist name together
## 'from table1 join table 2' similar to saying 'from both'
## have to do an 'on' or 'where' so fgn key on 1st matches to name
## can do where instead of on
#SELECT Album.title, Artist.name
#FROM Album
#JOIN Artist
#ON Album.artist_id = Artist.id;
#
## get track title and genre name
#SELECT Track.title, Genre.name
#FROM Track
#JOIN Genre
#ON Track.genre_id = Genre.id;
#
##what would happen if you select on clause
## would give all combinations
## nrows = len-table 1 * len-table-2 
#
## on/where picks only the ones that match
#
## track title, artist name, album title, genre name
#SELECT Track.title as track, Artist.name as artist, 
#Album.title as album, Genre.name as genre
#FROM Track
#JOIN Artist, Album, Genre
#ON Track.genre_id = Genre.id AND Track.album_id = Album.id
#AND Album.artist_id = Artist.id;

#reconstruct replication, dont store replication
# start ui, logical data model, phy data model, connect w nums, join


#3-4 - multi-table tracks
# connect xml and databases

# pull out his itunes library, put it in music db
# file > library > export to get xml file
# for hw1, use his library.xml though

#xml is a property list, dict of k-v pairs like date, track id
# anything w key track id, extract name, artist, size, time etc

#CREATE TABLE Artist (
#    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    name    TEXT UNIQUE
#);
#
#CREATE TABLE Genre (
#    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    name    TEXT UNIQUE
#);
#
#CREATE TABLE Album (
#    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    artist_id  INTEGER,
#    title   TEXT UNIQUE
#);
#
#CREATE TABLE Track (
#    id  INTEGER NOT NULL PRIMARY KEY 
#        AUTOINCREMENT UNIQUE,
#    title TEXT  UNIQUE,
#    album_id  INTEGER,
#    genre_id  INTEGER,
#    len INTEGER, rating INTEGER, count INTEGER
#);


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
if ( len(fname) < 1 ):
    fname = 'data/Library.xml'

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

# see hw/week3_hw_music_db.py for modified version of above code
# to get genre info as well


#4-1 - many to many relationships in sql

#we were using the one-to-many data model
# 1 album has many tracks 
# fgn key on the many/track side, allows for many tracks

# in a map, one line on the one table, 3 lines sticking out to many table

# sometimes tho there can be many artists on an album
# or a book with many authors

# then we need to add a 'connection or junction table' with 2 fgn keys

# so we would have a many authors to the one books table
# AND 
# a a many books to the one authors table

# this table has 2 fgn keys in it, and no primary key

#create new db and tables regarding courses, users

#CREATE TABLE User (
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    name  TEXT,
#    email TEXT);
#
#CREATE TABLE Course (
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    title TEXT);
#
#CREATE TABLE Member (
#    user_id  INTEGER,
#    course_id INTEGER,
#    role INTEGER,
#    PRIMARY KEY (user_id, course_id)
#    );
#
## insert data now
#INSERT INTO User (name, email)
#VALUES ('Jane', 'jane@tsugi.org');
#
#INSERT INTO User (name, email)
#VALUES ('Ed', 'ed@tsugi.org');
#
#INSERT INTO User (name, email)
#VALUES ('Sue', 'sue@tsugi.org');
#
#INSERT INTO Course (title)
#VALUES ('Python');
#
#INSERT INTO Course (title)
#VALUES ('SQL');
#
#INSERT INTO Course (title)
#VALUES ('PHP');
##
### member table 
###jane, ed, sue all in python. jane is teacher
#INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
#INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
#INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);
#
##jane and ed in sql. ed is teacher
#INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
#INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);
#
## ed and sue in php. sue is teacher
#INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
#INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0);
#
## connected them together, now get name, role, title
#SELECT User.name, Member.role, Course.title
#FROM User JOIN Member JOIN Course
#ON Member.user_id = User.id AND Member.course_id = Course.id
#ORDER BY Course.title, Member.role DESC, User.name;
#############

# 4-2 - many2many roster demo

#json is a list of a list - name, course, role until next course
# [[person1, person2], [person1, person2]]

#establish primary key in user table, primary key in course table
# then insert a row

## week4_2_roster_hw_preview.py
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# 3 tables user, member, course
# user has auto id, name
# course has auto_id, title
# memer has user_id, course_id, role (1/0) and primary key is (user, course)
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

#choose the json file, assign to filename
fname = str(raw_input('Enter file name: '))
if len(fname) < 1:
    fname = 'data/roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#create the str containing /n and ] etc
#open filename . read()
str_data = open(fname).read()

# this turns a str in json format into a json object
# list of lists of unicode
json_data = json.loads(str_data)

for entry in json_data:

    # each list/row is a person-class enrollment
    # with 3 data - name, title, role
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name, title)

    # if not already in,
    # insert each name into the 'name' col of the User table
    cur.execute('''
    INSERT OR IGNORE INTO User (name)
    VALUES ( ? )''', (name, ))
    
    #grab the id (that was auto-created above)
    # assign it to new var user_id
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    # insert the title into the course table
    cur.execute('''
    INSERT OR IGNORE INTO Course (title)
    VALUES ( ? )''', (title, ))
    
    # grab the course_id, assign to var
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # insert the user_id, course_id, role into the Member table
    # easier than cheat_sheet, writing down in table, manually adding
    cur.execute('''
    INSERT OR REPLACE INTO Member (user_id, course_id, role)
    VALUES ( ?, ?, ? )''',
    (user_id, course_id, role))

    conn.commit()

## no week4hw2

## 5-1 - ch 15 - geocoding
# data file/web -> db -> cleaner db -> vizualization and analysis

# might need api key or rate limit or be unreliable (start/restart)
# thats why we want to put it in db, data is saved if breaks 1/2 thru
# just keep running , starting at lower line, until full
# several days to get 10k bits of data
# might need multiple steps/scripts

#ex
# 2500/d google geodata + where.data -> geoload.py -> geodata.sqlite -> 
# geodump.py -> records written to where.js, where.html -> map

# cache is local copy of something elsewhere

#geodump.py loops thru sql, adds. adds to js file to make map page


#5-2 - page rank and web searching

# pg with lots of incoming links / better pgs get higher on google

# write simple crawler, compute simple pg rank algo, visualize network
# pagerank.zip

# web crawl, index building, searching

# creates copy of visited pages for later processing 
# that will index dl'd pgs for fast searches

# put html pgs into db instead of py or csv

# webcrawl policy
# selection policy - which pgs to dl
# re-visit - when to check for changes to pgs
# politeness policy - how to avoid overloading sites
# parallelization - how to coordinate several distributed crawlers

# way to talk with crawlers
# robots.txt - says dont go here, plz

# indexer cleans / pulls text apart / looks at keywords / detect spam

# keep it on 1 page and they pt to each other

# web -> spider.py w startpt link -> spider.sqlite
# sp_reset script, sp_rank script, sp_json script, sp_dump.py -> rows
# sp_json -> force.js and with ur force.html + d3.js -> map

# sp_reset sets pg ranks back to initial value, to adjust for new pgs

# then sp_dump.py shows pg_rank, what link led to


# 5-3 - gb of email data
# gmane - mailing lists
# crawl web-based archive

#1 crawl 2 analysis/cleanup 3 viz data
# no rate limit, non-rate-limited copy

# 1 get local copy db of data
# game.org -> gmane.py -> content.sqlite

# to analyze, take hours to read and parse
# 2 so make 2nd db w/ gmodel.py
# content2.sqlite

# 3 then can look at # of emails per user w gbasic.py

# 4 create the wordmap w gword.py > gword.js w gword.html w d3.js

# 5 create line graph of words w gline.py > gline.js w gline.html w d3.js


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
    # breaks here if not online
    uh = urllib.urlopen(url, context=scontext)
    # read the above string and change it from pointer to a string
    # data is from the url
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
    # print where connection died; restart the program manually
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print '==== Failure To Retrieve ===='
        print data
        break

    # finally inserting the address and data into locations db
    # each line in the file = data = tuple (0address, 1data)
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    conn.commit()
    
    # just so it doesnt outrun itself
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can \
visualize it on a map."

# zooms thru the ones we already had. can check db, gets bigger

#11 min of 5-4

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










