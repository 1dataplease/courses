-- 1 - make table
-- /**groceries - 4 banana, 1 pb, 2 dark choc bars**/

-- want id int primary key col, name of groceries, num of them
-- CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER);

-- -- to fill in - insert into $table values (r1c1, r1c2, r1c3)
-- INSERT INTO groceries VALUES (1, 'bananas', 4);
-- INSERT INTO groceries VALUES (2, 'peanut butter', 4);
-- INSERT INTO groceries VALUES (3, 'dark chocolate bars', 2);

-- -- look at
-- SELECT * FROM groceries;

-- 2 - add items, add a col for aislenum
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER);

INSERT INTO groceries VALUES (1, 'bananas', 4, 7);
INSERT INTO groceries VALUES (2, 'peanut butter',1, 4);
INSERT INTO groceries VALUES (3, 'dark chocolate bars',2, 2);
INSERT INTO groceries VALUES (4, 'ice cream', 1,12);
INSERT INTO groceries VALUES (5, 'cherries', 6,2);
INSERT INTO groceries VALUES (6, 'chocolate syrup', 1,4);

-- order it by aisle, make sure larger > 5
SELECT name FROM groceries
WHERE aisle > 5
ORDER BY aisle;

-- 3 - aggregate fxns

-- get total num of items we buy, by aisle
-- dont use name, because an aisle as 2 names, it doesnt include both. only look at nums and what u grouped by
SELECT name, aisle, SUM(quantity) from groceries GROUP BY aisle;

-- most we get of any 1 item - max
SELECT MAX(quantity) from groceries;

-- 4 - new db
CREATE TABLE exercise_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, type text, minutes integer, calories integer, heart_rate integer);

-- only inserting cols2:end. 1st one is autoincrementing
insert into exercise_logs (type, minutes, calories, heart_rate) values ('biking', 30, 100, 110);

insert into exercise_logs (type, minutes, calories, heart_rate) values ('biking', 10, 30, 105);

insert into exercise_logs (type, minutes, calories, heart_rate) values ('dancing', 15, 200, 120);

-- where burning most calories
select * from exercise_logs 
where calories > 50
order by calories;

-- where burned more than 50 and less than 15 minutes
select * from exercise_logs 
where calories > 50 and minutes < 30
order by calories;

-- or
select * from exercise_logs 
where calories > 50 or heart_rate > 100
order by calories;


-- 5 - in
insert into exercise_logs (type, minutes, calories, heart_rate) values ('biking', 30, 100, 110);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('biking', 10, 30, 105);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('dancing', 15, 200, 120);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('dancing', 15, 165, 120);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('climbing', 30, 72, 90);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('climbing', 25, 70, 90);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('rowing', 30, 70, 90);
insert into exercise_logs (type, minutes, calories, heart_rate) values ('hiking', 36, 80, 85);

-- only outdoor
select * from exercise_logs
where type="biking" or type="hiking" or type = "rowing";

-- easier
select * from exercise_logs
where type in ('biking', 'hiking', 'rowing');

-- indoor ones
select * from exercise_logs
where type not in ('biking', 'hiking', 'rowing');

-- new one
create table drs_favorites
    (id integer PRIMARY KEY, type TEXT, reason TEXT);

insert into drs_favorites(type, reason) values
    ('biking', 'improves endurance and flexibility');

insert into drs_favorites(type, reason) values
    ('hiking', 'improves cardiovascular health');

-- see exercise types that are also in drs_favorites
-- in
select * from exercise_logs
where type in 
(select type from drs_favorites);

-- only select cardiovascular reasons
-- subquery
select * from exercise_logs
where type in 
(select type from drs_favorites
where reason = 'improves cardiovascular health');

-- if text is close - inexact match
-- like
select * from exercise_logs
where type in 
(select type from drs_favorites
where reason like '%cardiovascular%');

-- 6 
-- group by
-- see how many cols burned for each type activity
select type, sum(calories) as total_calories_burned from exercise_logs
group by type;

-- doing below would only sum activities where calories > 150 in 1 log
select type, sum(calories) as total_calories from exercise_logs
where calories > 150
group by type;

-- only show activities where calories > 150 (1oz choc)
select type, sum(calories) as total_calories_burned from exercise_logs
group by type
having total_calories_burned > 150;

-- use aggregate for all exercises where we burn > 70 on avg
select type, avg(calories) as avg_calories_burned from exercise_logs
group by type
having avg_calories_burned > 70;

-- all exercises where we logged at least 2 rows/sessions for that type exercise
select type, count(*) as logged from exercise_logs
group by type
having logged >= 2;

-- 7
-- max heartrate is 220-age, see if it ever went above it (# of cases)
select count(*) from exercise_logs
where heart_rate > 220 - 30;

-- see if it went into target zone - 50-90% of max
select count(*) from exercise_logs
where heart_rate > (.5 * (220-30))
and heart_rate < (.9 * (220 - 30));

-- see summary of all of them, how many were in each zone
-- create a column saying the zone, then group by

-- case - create new col temporarily
-- then group by the new col, see count of type in each group
select count(*), 
case 
when heart_rate > 220-30 then 'above max'
when heart_rate > round(.9 * (220-30)) then 'above target'
when heart_rate > round(.5 * (220-30)) then 'within target'
else 'below target'
end as 'hr_zone'
from exercise_logs
group by hr_zone;

--8
--joining b/w 2 new tables (from an article)

-- create students
create table students (id integer PRIMARY KEY,
first_name text,
last_name text,
email text,
phone text,
birthdate text);

-- insert students
insert into students (first_name, last_name, email, phone, birthdate) values ('pete', 'rabbit', 'pete@rabbit.com', '555-6666', '2002-06-24');

insert into students (first_name, last_name, email, phone, birthdate) values ('alice', 'wonderland', 'alice@wonderland.com', '555-4444', '2002-07-04');

-- their grades
create table student_grades (id integer primary key,
student_id integer,
test text,
grade integer)

-- insert their grades
insert into student_grades (student_id, test, grade)
    values (1, 'nutrition', 95);
insert into student_grades (student_id, test, grade)
    values (2, 'nutrition', 92);
insert into student_grades (student_id, test, grade)
    values (1, 'chemistry', 85);
insert into student_grades (student_id, test, grade)
    values (2, 'chemistry', 95);

select * from student_grades;

-- delete if ran same one twice
delete from student_grades
    where id=2;

-- reset the auto-increment col
-- first find highest auto-incremented number, redo doesnt work

-- easier to drop whole table, re-add it
drop table student_grades;

-- cross join
-- returns the cartesian product
-- for every row in table1, creates row in table2
-- 4 + 4 = 8 rows
-- least useful
select * from students, student_grades;

-- implicit inner join
-- only match rows if student_id matches student
-- filters it down to what we want
-- not best practice tho
select * from students, student_grades
where students.id = student_grades.student_id;

-- explicit inner join
-- uses join keyword
select * from students
join student_grades
on students.id = student_grades.student_id;

-- same but only cols and rows we want
select first_name, last_name, test, grade from students
join student_grades
on students.id = student_grades.student_id
where grade > 90;

-- but if there was a grade col in both tables
-- safer to tell it
select students.first_name, students.last_name, student_grades.test, student_grades.grade from students
join student_grades
on students.id = student_grades.student_id
where grade > 90;

--9
--left outer joins

-- projects
-- has student_id col to relate it to students table
create table student_projects (id integer primary key,
student_id integer,
title text);

-- add only one
insert into student_projects (student_id, title)
    values (1, 'carrot catapult');

-- inner join
-- only creates rows if matching records in 2 tables
-- see who did the project
-- join projects to students to see
select students.first_name, students.last_name, student_projects.title
from students
join student_projects
on students.id = student_projects.student_id;

-- want every student to be on list, even if no project
-- record on table1, but not on table2)
-- left outer join
select students.first_name, students.last_name, student_projects.title
from students
left outer join student_projects
on students.id = student_projects.student_id;

-- right outer join
-- keeps everything in table2
-- would say project2 - null for first/last name

-- full outer join
-- match rows, fill in nulls both ways


--10
-- change rows w update and delete

-- diary app needs users and diary logs table
create table users (id integer primary key,
name text);

create table diary_logs (id integer PRIMARY key,
user_id integer,
date text,
content text);

-- after the user submits a diary log
insert into diary_logs(user_id, date, content)
    values(1, '2015-04-01',
        'i had a fight with some guy, ate food');

insert into diary_logs(user_id, date, content)
    values (1, '2015-04-02', 'we made up, were cool, we ate');

select * from diary_logs;

-- they want to go back and update old diary log
update diary_logs
    set content = 'i had a fight with that guy'
    where id=1;

-- now delete the entire log entry
delete from diary_logs
    where id=1;

-- some apps never really delete, they have a deleted col
-- set deleted='true'
-- in select, only see deleted='false'


-- 11
-- altering table
-- months later, want to add an emotion col
-- couldnt edit create stmt, rerunning it would remove data

alter table diary_logs add emotion text;

-- now can add values in new posts
insert into diary_logs (user_id, date, content, emotion)
    values (1, '2015-04-03', 'i went to disneyland', 'happy');

-- so now any rows without it say NULL
-- if we want, we can have it set to something else
-- alter table diary_logs add emotion text default 'pre_feature';

-- drop entire table - if all data got to new table
-- drop table diary_logs;


--12
-- joining tables to themselves with self joins

--not in vid, first alter students adding buddy_id
alter table students add buddy_id text;

--not in vid, add buddy_id to 2 existing students
update students
    set buddy_id = 2
    where id=1;

update students
set buddy_id = 1
where id=2;


-- insert 2 new students
insert into students
    values (3, 'aladdin', 'agorah', 'aladdin@agorah.com', '555-3333', '2001-05-10', 4);

insert into students
    values (4, 'simba', 'kingston', 'simba@kingston.com', '555-1111', '2001-12-24', 3);

-- check that it worked name, buddy_id
-- buddy_id is related to 1st col
select id,first_name, last_name, buddy_id from students;

-- show name of each student next to their buddys email
-- would have to 1st join students table with itself

-- have to prefix col name with alias next to join stmt
select students.first_name, students.last_name, buddies.email
from students
join students buddies;

-- way too many rows, on - filter down by saying buddy_id = id
-- also change name of email to buddys email
select students.first_name, students.last_name, buddies.email as buddy_email
from students
join students buddies
on students.buddy_id = buddies.id;


-- 13
-- combining joins and self joins

-- add 3 more projects
insert into student_projects (student_id, title)
    values (2, 'mad hattery');
insert into student_projects (student_id, title)
    values (3, 'carpet physics');
insert into student_projects (student_id, title)
    values (4, 'hyena habitats');

-- for reviewing each others work
-- but all it shows is 1,2 ; 3,4. should be 4 names
-- at end want 2 rows, each with the 2 partner cols
-- want to see 2 project titles in each row
create table project_pairs (id integer primary key,
project1_id integer,
project2_id integer);

insert into project_pairs (project1_id, project2_id)
    values (1,2);
insert into project_pairs (project1_id, project2_id)
    values (3,4);

select * from project_pairs;

-- join project_pairs w student_projects
-- join on the projects title to get name like before
-- but this only shows 8 rows, not 2
select * from project_pairs
join student_projects;

-- select titles
-- joining project(containing names ) 
-- on thisone.project1-id = a.id
-- then do it again
-- on this tables project2id = other tables id
select a.title, b.title from project_pairs
join student_projects a
on project_pairs.project1_id = a.id
join student_projects b
on project_pairs.project2_id = b.id;


--14
-- students table and grades table

-- selecting everything shows grade id, studentid, test, grade
select * from student_grades;

-- want to see name, email, each grade

-- cross join
-- for each row in 1st, created row in 2nd
select * from student_grades, students;





































