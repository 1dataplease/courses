-- 2-2 basic sql
-- browser makes network rqst to webserver.
-- pulls php file from web server
-- db server is mysql, fills up the document object model

-- learn the language bw php and mysql
-- user dba - php browser or mysql cl - sql - db server mysql

-- if running on linux server, usually run on cl
-- phpMyAdmin

-- port 8888 and 8889 in mamp
-- tools > phpMyAdmin
-- can go to sql or can paste in below from cl
-- donesnt work on windows
-- /Applications/MAMP/Library/bin/mysql -u root -p

CREATE DATABASE People DEFAULT CHARACTER SET utf8;

CREATE TABLE Users (
name VARCHAR(128),
email VARCHAR(128)
);

-- only in cl
--DESCRIBE Users;

INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu');
INSERT INTO Users (name, email) VALUES ('Sally', 'sally@umich.edu');
INSERT INTO Users (name, email) VALUES ('Somesh', 'somesh@umich.edu');
INSERT INTO Users (name, email) VALUES ('Caitlin', 'cait@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');

DELETE FROM Users WHERE email='ted@umich.edu';

--update/change data
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu';

-- any e
select * from users where name like '%e%'

-- limit clause - request first n rows
-- this'll show z->a
select * from users order by email desc limit 2;

-- get the 2nd one and the 3rd one
select * from users order by email limit 1,2;

-- getting 1st and 4th would be 0,3


-- 2-3 data types in sql
-- text, binary (both have sm and large), numeric, auto_incr

-- char
-- char allocates entire space - faster for small strs known len
-- if very little variance in the char length, can use this
-- varchar
-- varchar allocates variable amt of space depending on data length
-- give it a clue might be 4-512 chars
-- both can be latin, azn, etc

-- tinytext up to 255, text up to 65k, mediumtext up to 16mb
-- longtext up to 4gb of chars

-- byte / binary
-- rarely used: byte or binary types
-- character is 8-32 bits depending on character set
-- byte is 8 bits of info
-- byte(n) up to 255 bytes
-- varbinary(n) up to 65k bytes
-- small igs, not indexed or sorted

--blob
-- can store binary large object or blob
-- pdf, img, word doc, movie
-- no transaltion, indexing or char set
-- tinyblob(n) up to 255
-- blob up to 65k, medium, large

-- integers
-- tinyint(-128, 128) ; smallint (-32768), INT (2Bill),
--BIGINT (10**18 ish)

-- floats
-- float (32 bit) up to 10**38 w 7 digits accuracy
-- double (64 bit) up to 10**308 w 14 digits accuracy
-- dont store money in float, use scaled integers

-- dates
-- timestamp - num of secs since 1970
-- 'yyyy-mm-dd hh:mm:ss' (1970, 2037) 2B secs
-- datetime - 'yyyy-mm-dd hh:mm:ss', more space, year
-- date
-- time
now() -- gets timestamp


-- 2-3 db keys and indexes
--  how to use this data in each col

-- need to have an int primary key in this table
-- so that when we join together tables
-- can efficiently add a reference to row
-- in other table as a foreign key

DROP TABLE Users;

CREATE TABLE Users (
user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
name VARCHAR(128),
email VARCHAR(128),
PRIMARY KEY(user_id),
INDEX(email)
);

-- then added rows back in - see lines 28 to 32

-- index means we're going to lookup with where clauses a lot
-- hints how we're going to use it so db can be quicker
-- scanning all data to find 1 row could take time
-- starts using shortcuts - hashes or trees

--types of indices
-- primary key - little space, exact match, no dups
-- fast for int fields 

-- index
-- good for individual row lookup, sorting/grouping results
-- works w exact matches or prefix lookups
-- suggest hash or btree

-- b-tree in log time. small amt that pts to larger chunks
-- good for sorted material, prefix 'ch' material

-- hashes
-- fxn that makes dicts fast
-- calcs based on the key, produces a number ex 0:15
-- can have >1 key hashed to same place

-- alter table 
-- if tables slow
-- and u forgot to add a primary key and an index
-- strings want btree, otherwise hash
-- dont need to put in 'using btree'
-- ALTER TABLE Users ADD INDEX (email) USING BTREE;


-- the performance gain
-- make >1 table, start connecting them together

-- creating db, copying+pasting hw1 led to answer
-- 493f4a0d01c55fddba656d6e89436ac96d271e13


-- 3-1
-- relational db design

-- buy tracks

-- redo of other class

-- 3-3 5min
DROP TABLE Artist;
DROP TABLE Album;
DROP TABLE Genre;
DROP TABLE Track;

CREATE TABLE Artist (
artist_id INTEGER NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
PRIMARY KEY(artist_id)
) ENGINE = InnoDB;

CREATE TABLE Album (
album_id INTEGER NOT NULL AUTO_INCREMENT,
title VARCHAR(255),
artist_id INTEGER,
PRIMARY KEY(album_id),
INDEX USING BTREE (title),

CONSTRAINT FOREIGN KEY (artist_id)
	REFERENCES Artist (artist_id)
	ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;

-- dont need to do the constraint n below
-- col artist_id in the album table references it in artist tb

CREATE TABLE Genre (
genre_id INTEGER NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
PRIMARY KEY(genre_id),
INDEX USING BTREE (name)
) ENGINE = InnoDB;

CREATE TABLE Track (
track_id INTEGER NOT NULL AUTO_INCREMENT,
title VARCHAR(255),
len INTEGER,
rating INTEGER,
count INTEGER,
album_id INTEGER,
genre_id INTEGER,
PRIMARY KEY(track_id),
INDEX USING BTREE (title),

CONSTRAINT FOREIGN KEY (album_id) 
	REFERENCES Album (album_id)
	ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT FOREIGN KEY (genre_id) 
	REFERENCES Genre (genre_id)
	ON DELETE CASCADE ON UPDATE CASCADE

) ENGINE = InnoDB;

-- track table, we say that the title is the logical key
-- logical key, we want to index using btree if string

-- tell it album_id pts to album (album_id)
-- same for genre

-- couldnt add fgn key constraint
-- need to start from leaves of database then go inward;

-- add the artists
INSERT INTO Artist (name) values ('Led Zepplin');
INSERT INTO Artist (name) values ('AC/DC');

--2nd genre table
INSERT INTO Genre (name) values ('Rock');
INSERT INTO Genre (name) values ('Metal');

--3rd album title - we need to put in a foreign key for artist
-- we added Led Zep 1st, so that artist_id is 1
INSERT INTO Album (title, artist_id) values ('IV', 2);
INSERT INTO Album (title, artist_id) values ('Who Made Who', 1);
--
--4th track table
-- cols are title, rating, len, count album_id, genre_id
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Black Dog', 5, 297, 0, 2, 1);
--
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Stairway', 5, 482, 0, 2, 1);
--
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('About to Rock', 5, 313, 0, 1, 2);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Who Made Who', 5, 207, 0, 1, 2);

-- track table does have vertical duplication in 
-- alum_id and genre_id
-- its ok because they are integers

-- now bring back together


-- 3-4 relational db design 4

-- see album and artist, different name for id cols
SELECT Album.title, Artist.name
FROM Album
JOIN Artist
ON Album.artist_id = Artist.artist_id;

-- see track and genre
SELECT Track.title, Genre.name
FROM Track
JOIN Genre
ON Track.genre_id = Genre.genre_id;

--  no on clause - shows all combos. 2X4 = 8 rows
-- on clause throws away non-matching rows
SELECT Track.title, Track.genre_id, 
Genre.genre_id, Genre.name
FROM Track JOIN Genre

-- get track, artist, album, genre
-- remember track has genre and album in it
-- album has artist in it
SELECT Track.title as track, Artist.name as artist, 
Album.title as album, Genre.name as genre
FROM Track JOIN Artist JOIN Album JOIN Genre
ON Track.genre_id = Genre.genre_id
AND Track.album_id = Album.album_id
AND Album.artist_id = Artist.artist_id;

-- remember, have to use join instead of a comma
-- have to use AND instead of a comma

-- on delete cascade on update cascade
-- same as saying that it points to other table
-- if id changes or gets wiped out in table1
-- please also wipe it out in table2 that has fn key
-- pointing to table 1

DELETE FROM Genre WHERE name="Metal";

-- cascade would also remove the 2 metal tracks in track db

-- on delete (default)
-- on delete restrict
-- sql would run an error, doesnt let u delete metal

-- on delete cascade
-- adjust the child rows by removing/updating to keep consistent

-- on delete set null
-- set the fgn key cols in the child rows to null


-- week3hw

-- add a 3rd artist
INSERT INTO Artist (name) values ('Radiohead');

-- artist_id is 9, want it to be 3 instead?

-- add 3 more albums
INSERT INTO Album (title, artist_id) values ('In Rainbows', 9);
INSERT INTO Album (title, artist_id) values ('OK Computer', 9);
INSERT INTO Album (title, artist_id) values ('Hail to the Thief', 9);

-- those are album_id 3,4,5

-- get to 20 total tracks (16 more, from current 4)
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Paranoid Android', 5, 297, 0, 4, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('2+2=5', 5, 297, 0, 5, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Go To Sleep', 5, 297, 0, 5, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Sail to the Moon', 5, 297, 0, 5, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('There There', 5, 297, 0, 5, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('15 Step', 5, 297, 0, 3, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Body Snatchers', 5, 297, 0, 3, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Nude', 5, 297, 0, 3, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Reckoner', 5, 297, 0, 3, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Jigsaw Falling Into Place', 5, 297, 0, 3, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Weird Fishes Archipelligo', 5, 297, 0, 3, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Paranoid Android2', 5, 297, 0, 4, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Paranoid Android3', 5, 297, 0, 4, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Paranoid Android4', 5, 297, 0, 4, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Paranoid Android5', 5, 297, 0, 4, 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
VALUES ('Paranoid Android6', 5, 297, 0, 4, 1);

-- each track needs a  genre: i called them all rock

-- after that
SELECT * FROM Track

-- and the query in row 284
SELECT Track.title as track, Artist.name as artist, 
Album.title as album, Genre.name as genre
FROM Track JOIN Artist JOIN Album JOIN Genre
ON Track.genre_id = Genre.genre_id
AND Track.album_id = Album.album_id
AND Album.artist_id = Artist.artist_id;

-- recall that artist's id connects to fgn key in album
-- album's id connects to track
-- genres id connects to track also 

-- use GROUP BY to show num of tracks each artist has in 
-- each genre
SELECT Artist.name, Album.title as album, Count(Track.track_id)
FROM Track JOIN Artist JOIN Album JOIN Genre
ON Track.genre_id = Genre.genre_id
AND Track.album_id = Album.album_id
AND Album.artist_id = Artist.artist_id
GROUP BY Artist.artist_id, Genre.genre_id


-- 5-1 - many2many relationships

-- new db

CREATE TABLE Account (
account_id INTEGER NOT NULL AUTO_INCREMENT,
email VARCHAR(128) UNIQUE,
name VARCHAR(128),
PRIMARY KEY(account_id)
) ENGINE = InnoDB CHARACTER SET=utf8;

CREATE TABLE Course (
course_ID INTEGER NOT NULL AUTO_INCREMENT,
title VARCHAR(128),
PRIMARY KEY(course_id)
) ENGINE = InnoDB CHARACTER SET=utf8;


-- the connecting table so course many members and viceversa

CREATE TABLE Member (
account_id INTEGER,
course_id INTEGER,
role INTEGER,

CONSTRAINT FOREIGN KEY (account_id) REFERENCES 
Account (account_id)
ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT FOREIGN KEY (course_id) REFERENCES 
Course (course_id)
ON DELETE CASCADE ON UPDATE CASCADE,

PRIMARY KEY(account_id, course_id)
) ENGINE = InnoDB CHARACTER SET=utf8;

-- add in ppl and courses and member info

INSERT INTO account (name, email)
VALUES ('Jane', 'jane@tsugi.org');

INSERT INTO account (name, email)
VALUES ('Ed', 'ed@tsugi.org');

INSERT INTO account (name, email)
VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title)
VALUES ('Python');

INSERT INTO Course (title)
VALUES ('SQL');

INSERT INTO Course (title)
VALUES ('PHP');


INSERT INTO Member (account_id, course_id, role) VALUES (1,1,1);
INSERT INTO Member (account_id, course_id, role) VALUES (2,1,0);
INSERT INTO Member (account_id, course_id, role) VALUES (3,1,0);

INSERT INTO Member (account_id, course_id, role) VALUES (1,2,0);
INSERT INTO Member (account_id, course_id, role) VALUES (2,2,1);

INSERT INTO Member (account_id, course_id, role) VALUES (2,3,1);
INSERT INTO Member (account_id, course_id, role) VALUES (3,3,0);

# connected them together, now get name, role, title
SELECT Account.name, Member.role, Course.title
FROM Account JOIN Member JOIN Course
ON Member.account_id = Account.account_id AND Member.course_id = Course.course_id
ORDER BY Course.title, Member.role DESC, account.name;


-- see instructions for week5_hw

DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
user_id INTEGER NOT NULL AUTO_INCREMENT KEY,
name VARCHAR(128) UNIQUE
) ENGINE=InnoDB CHARACTER SET=utf8;

CREATE TABLE Course (
course_id INTEGER NOT NULL AUTO_INCREMENT KEY,
title VARCHAR(128) UNIQUE
) ENGINE=InnoDB CHARACTER SET=utf8;

CREATE TABLE Member (
user_id INTEGER,
course_id INTEGER,
role INTEGER,
CONSTRAINT FOREIGN KEY (user_id) REFERENCES User (user_id)
ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT FOREIGN KEY (course_id) REFERENCES Course (course_id)
ON DELETE CASCADE ON UPDATE CASCADE,

PRIMARY KEY (user_id, course_id)
) ENGINE=InnoDB CHARACTER SET=utf8;

-- normalize it (so each user gets diff data)
-- insert data, creating and linking all fgn keys

-- first users table - name and auto user_id
INSERT INTO User (name) VALUES ('Taliesin'); --si106, Instructor
INSERT INTO User (name) VALUES ('Denver');
INSERT INTO User (name) VALUES ('Juwairiyah');
INSERT INTO User (name) VALUES ('Kainui');
INSERT INTO User (name) VALUES ('Zoya');
INSERT INTO User (name) VALUES ('Aisha');
INSERT INTO User (name) VALUES ('Artemis');
INSERT INTO User (name) VALUES ('Danna');
INSERT INTO User (name) VALUES ('Dennis');
INSERT INTO User (name) VALUES ('Tyler');
INSERT INTO User (name) VALUES ('Kirstin');
INSERT INTO User (name) VALUES ('Allisha');
INSERT INTO User (name) VALUES ('Carra');
INSERT INTO User (name) VALUES ('Idahosa');
INSERT INTO User (name) VALUES ('Iliana');

-- course table - title and auto course_id
INSERT INTO Course (title) VALUES ('si106');
INSERT INTO Course (title) VALUES ('si110');
INSERT INTO Course (title) VALUES ('si206');


-- members table - user_id, course_id, role
INSERT INTO Member (user_id, course_id, role)
VALUES(1, 1, 1);

INSERT INTO Member (user_id, course_id, role)
VALUES(2,1,0);
-- Denver, si106, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(3,1,0);
-- Juwairiyah, si106, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(4,1,0);
-- Kainui, si106, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(5,1,0);
-- Zoya, si106, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(6,2,1);
-- Aisha, si110, Instructor

INSERT INTO Member (user_id, course_id, role)
VALUES(7,2,0);
-- Artemis, si110, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(8,2,0);
-- Danna, si110, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(9,2,0);
-- Dennis, si110, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(10,2,0); 
-- Tyler, si110, Learner

INSERT INTO Member (user_id, course_id, role)
VALUES(11,3,1);
-- Kirstin, si206, Instructor


INSERT INTO Member (user_id, course_id, role)
VALUES(12,3,0);
-- Allisha, si206, Learner


INSERT INTO Member (user_id, course_id, role)
VALUES(13,3,0);
-- Carra, si206, Learner


INSERT INTO Member (user_id, course_id, role)
VALUES(14,3,0);
-- Idahosa, si206, Learner


INSERT INTO Member (user_id, course_id, role)
VALUES(15,3,0);
-- Iliana, si206, Learner


-- testing code for week5hw, worked

SELECT User.name, Course.title, Member.role
FROM User JOIN Member JOIN Course
ON User.user_id = Member.user_id AND Member.course_id = Course.course_id
ORDER BY Course.title, Member.role DESC, User.name