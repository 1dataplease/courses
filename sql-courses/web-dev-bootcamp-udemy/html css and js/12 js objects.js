// 121 - model a single person like name, age, city
var person = ['bo', 19, 'missouri'];

// to retrieve their hometown
person[2]

// would have to connect mult ppl by indexnumber, coder might not know or put a person in wrong num
// better to use when theres a logical order
var person2 = ['bob', 'la', 22]

// better to use json or dict type format - can connect multiple ppl by name/age/city. no order
var person = {
	name: 'jim',
	age: 32,
	city:'kc'
};

// 2 ways to retrieve data from object

// 1 - use bracket notation like array
console.log(person['name']);
// 2 - use dot notation
console.log(person.name);

// 3 differences
// 1 - cannot use dot-notation when property starts w/ a number
// doesnt find object's 1st-thing
// object.1st-thing

// 2 - cannot use dot-notation when looking up a variable (that has the name of our objects key)
var str = 'name'
// doesnt find person.name
// person.str 

// 3 - cannot use dot-notation for property names w/ spaces
// doesnt find it
// someObject.fav color


// how to update data
// add 1 to age
person.age += 1;
// update city
person.city = 'london';


// initialize object
// make empty object, then add to it
var person3 = {};
person3.name = 'joe';
person3.age = 34;
person3.city = 'sf';
// other way
var person4 = new Object();

// objects (like arrays) can hold arrays, str, num, other objects



// 122 - compare syntax b/w array and object
// key-value pairs
var dog = {
	name: 'bubba',
	breed: 'mutt'
}
// instead of dogList[1]
dog.name;
dog['name'];

// list/array is a type of object thats ordered, and always num

// array - push, unshift
dogs = ['bo', 'jo'];
dogs.push['wayne']; // returns 3

// object - assign any key and any value u want
dog.age = 5;

// array - change jo to joanne
dogs[1] = 'joanne'

// object = change to lab
dogs.breed = 'lab'


// 123 - objs or arrays inside of objs arrays
// array has site of posts,comments,likes, friends
var posts = [
	{
		title: 'cats are ok',
		author: 'me',
		comments: ['cool', 'booo']
	},
	{
		title: 'f u man',
		author: 'cat lover',
		comments: ['hell yea', 'lol']
	}
]

// posts is as array of 2 objects - each has author, comm, title
posts.length

// get title of first post
posts[0].title

// get 2nd comment of 2nd post
posts[1].comments[1]


// 124 - objects exercises
// ex 1
var someObject = {};
someObject._name = 'hedwig';
someObject.age = 6;

var prop = 'color';
someObject[prop] = 'red';

// ex 2
var someObject = {
	friends: [
	{name: 'malfoy'},
	{name: 'crabbe'},
	{name: 'goyle'}
],
color: 'baby blue',
isEvil: true
};

// get malfoy
// friends is an array of 3 seperate key-value pairs all name
// first one [0] gives us {name: malfoy} then get just malfoy
someObject.friends[0].name

// 125
// write a movieDB array
// array movies, lots of objects in it w title, rating, hasWatched
// then iterate thru it to print 
// you have watched 'title' - rating or
// you have not seen 'title' - rating
var movies = [
	{title: 'Finding Nemo', hasWatched: true, rating: 4.5},
	{title: 'Blade Runner', hasWatched: false, rating: 5}
]

function buildString(movie) {
	var startSentence = 'You have ';

	if(movie.hasWatched) {
		startSentence += "watched ";
	}

	else{
		startSentence += 'not seen ';
	}

	startSentence += '"' + movie.title + '" - ';
	startSentence += movie.rating + ' stars';
	return startSentence;
}

movies.forEach(function(movie){
	console.log(buildString(movie))
});


// 127 - keyword this
// underscorejs.org is a library, has fxns
// groups or namespaces them all together 
// _.map
// _.reduce
// so u know they all come from this library

// in javascript - this
// making app that has comments in object, also methods like print

var comments = {};
comments.data = ['good job', 'lame', 'bye', 'cool'];
// see comments is an array
comments;

//could define in it a fxn, exists outside of comments object
function print(arr){
	arr.forEach(function(el){
		console.log(el);
});
}

// to print comments.data, would have to do
print(comments.data);

// instead, want to 
comments.print = function(arr){
	arr.forEach(function(el){
		console.log(el);
});
}

// dont need an argument
comments.print = function(){
	this.data.forEach(function(el){
		console.log(el);
});
}

// in this case 'this' refers to the object comments
// which has data inside of it

// just shows the fxn
comments.print;

// runs this fxn/method
comments.print();

// 126 - adding methods to objects

var obj = {
	name: 'chuck',
	age: 45,
	isCool: false,
	friends: ['bob', 'tina'],
	add: function(x,y){
		return x+y;
	}
}

// to call it
obj.add(10,5);

// console is an object, log is a method on that object

// why have them inside of objects?
// help keep code organized, group logically
// want a speak method for both dogs and for cats
// add as method to dogs obj and cats obj
function speak(){
	return 'woof';
}
speak();

var dogSpace = {};
dogSpace.speak = function(){
	return 'woof';
}

var catSpace = {};
catSpace.speak = function(){
	return 'meow'
}
// have a delete for posts, for users, for comments


// 13 - dom manipulation
// 128 exs
// js meets html + css

// interactive game, real to-do list, form, animations
// use js to manipulate the dom. understand the select, manipulate
// scrolling, dropdown, form validations, interactive
// ex. google word recommendations, submenu, patatap-sounds


// 129 - defining dom - document object model
// interface b/w js and html+css

// browser turns every html tag into a js object we can manipulate

// type in console on any site
document
// shows html as text, not the objects, to get that
// print out the entire document oject in the object syntax
console.dir(document)

// the body property has many subproperties
// childNodes: div, script, div


// 130 - select and manipulate process
// change <h1> color using js

// in css we write selector, apply styles
// in js we select, return, change

// 1 way
var h1 = document.querySelector('h1');
h1.style.color = 'pink';

// animation - every second the bg color changes
var body = document.querySelector('body'); //select
var isBlue = false;

setInterval(function(){
	if(isBlue) {
		body.style.background = 'white';
	}
	else {
		body.style.background = '#3498db';
	}
	isBlue = !isBlue;
}, 1000);


// 131 - selector methods

document.url
document.links
document.body
document.head

// 5 main methods
document.getElementById()
document.getElementsByClassName()
document.getElementsByTagName()
document.querySelector()
document.querySelectorAll()

























