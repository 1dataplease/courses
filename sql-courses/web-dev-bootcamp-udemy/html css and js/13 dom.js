// 130 - select and manipulate process
// change <h1> color using js

// in css we write selector, apply styles
// in js we select, return, change

// 1 way
var h1 = document.querySelector('h1');
////doesnt work for some reason
// h1.style.color = 'pink';

// animation - every second the bg color changes
var body = document.querySelector('body'); //select
var isBlue = false;

// setInterval(function(){
// 	if(isBlue) {
// 		body.style.background = 'white';
// 	}
// 	else {
// 		body.style.background = '#3498db';
// 	}
// 	isBlue = !isBlue;
// }, 1000);


// 131 - selector methods

document.url;
document.links;
document.body;
document.head;

//// 5 main methods
// document.getElementById()
// document.getElementsByClassName()
// document.getElementsByTagName()
// document.querySelector()
// document.querySelectorAll()

// 1 - getElementById
// id can only appear 1 time per page - selects 1st li

// prints out <li id="highlight">adding methods to object</li>
// but it actually returns an object representation
var tag = document.getElementById('highlight');

// below prints out li#highlight
console.dir(tag);


// 2 - getElementsByClassName
// class can occur many times, returns a list of them
// techically a node list - like a lightweight array
// cannot do a forEach loop through it
// lots of properties inside each
var tagsByClass = document.getElementsByClassName('bolded');
// returns  [li.bolded, li.bolded]


// 3 - getElementsByTagName
// return list of 3 li elements on page
var tagsByTagName = document.getElementsByTagName('li');

// [li#highlight, li.bolded, li.bolded, highlight: li#highlight]
// not sure why 4 instead of 3
// they are js objects with properties, not just list
console.log(tagsByTagName[0]);


// 4 - querySelector
var tagByCssSyntax = document.querySelector('#highlight');
// only gives 1st match, only 1 element. not a list
var tagByCssSyntax2 = document.querySelector('.bolded');
var tagByCssSyntax3 = document.querySelector('h1');

// all emphasis tags inside an li with a class of bolded
// didnt work for this html pg
var spec = document.querySelector('li em.bolded');


// 5 - querySelectorAll
var all = document.querySelectorAll('li');
// returns as a list w 1 item below
var all = document.querySelectorAll('#highlight');


// 132 - exercise - 4 ways to select first p tag

// 1 - by class
var way1 = document.getElementsByClassName('special');

// 2 - by id
var way2 = document.getElementById('first');

// 3 - by queryselector
var way3 = document.querySelector('p');

// 4 - queryselectorall, 1st element
var way4 = document.querySelectorAll('p')[0];

// 5 (in video)
var way5 = document.querySelector('#first');
var way6 = document.querySelector('.special');

// 7 - multiple by TagName
var way7 = document.getElementsByTagName('p')[0];

// first paragraph after an h1
var way8 = document.querySelector('h1 + p');



// 134 - manipulationg style - select all h1 or img, change color, animate, enlarge on click

// change an elements style - make blue, font size

// this tag refers to 13 dom.htmls 1st li, it has an id highlight
var tag = document.getElementById('highlight');

// change that tags styles
// why does it say cannot read property style of null
// for now, need to type these into the console
tag.style.color = 'blue';
tag.style.border = '10px solid red';
tag.style.fontSize = '70px';
tag.style.background = 'yellow';
tag.style.marginTop = '200px';

// do same again for h1
var h1 = document.querySelector('h1');

// giant object, tons of properties
h1.style;
h1.style.color = 'yellow';
h1.style.border = '5px solid pink';

// if changing 5 properties on 1 tag, 
//		then seperate concerns
// html, css, js responsible for own domain
// can write in style on html tho for mturk
// can turn them on/off in css file with class 'highlight'
// that class has 5 elements to change

// in js, add 1 class, changes 5 properties
// instead - make a .class in css with colors
var tag = document.getElementById('highlight');

// add/remove classes with js

// add new class to the selected element
tag.classList.add('blue-color-red-border');

// classList is a read-only element containing classes of element
// it is not an array

// remove a class 
tag.classList.remove('blue-color-red-border');

// toggle class - easier than add/remove
// if no, turns on. if on, turns off
// it also returns true/false depending on status
tag.classList.toggle('blue-color-red-border');



// 135 - changing content/text of a tag

// in the html we have a word in a strong tag
// select the p tag not strong
var tag = document.querySelector('p');

// retrieve the text in the paragraph
tag.textContent; //

// alter the textContent
// both of these get rid of our strong tag tho
tag.textContent = 'topics for you:';

// same, done again
// document.querySelector('p')
// both of these get rid of our strong tag tho
var p = document.getElementsByTagName('p')[0];
p.textContent = 'topics for me:';

// this will show all 3 seperated by... spaces
var ul = document.querySelector('ul');
ul.textContent;

// maintain structure - how to keep the strong tag
var tag = document.querySelector('p');
tag.innerHTML; //'topics for strong me strong'

var ul = document.querySelector('ul');
ul.innerHTML;

// now change the text of h1 in chain
document.querySelector('h1').textContent = 'topics: '

// get all the html for the body
document.body.innerHTML

// get all text on page
document.body.textContent

// make textContent - 
document.body.innerHTML = '<h1>Goodbye</h1>';

// 136 - chang attributes like src, hred
// change source of an img tag

// <a href "google.com">I am a link</a>;
// <img src = 'logo.png'>

// grab the link
var link = document.querySelector('a');

// get the anchors link text, its href tag
link.getAttribute('href'); //google.com

// now change it to new link
link.setAttribute('href', 'http://www.dogs.com');

// change the img src
var img = document.querySelector('img');
img.setAttribute('src', 'map-of-tags.png');

// look at src of first img if many
img1 = document.getElementsByTagName('img')[0];

// change the text of the link
link.textContent = 'broken link to corgis';



// 138 - google

// change the logo to cat - could be canvas or multiple
// inspect - select img, this is the id
var logo = document.getElementById('#hplogo');
var logo = document.querySelector('#hplogo');

// set to new img
logo.setAttribute('src', 'http://kittens.com/catimg.jpg')

// change width and height so it takes same amt of original
// was 272x92
logo.style.width = '200px;'
logo.style.height = '92px;'
logo.style.border = '2px solid purple';

// change links to bing

// use a loop to change all hrefs

// 1st - select all anchor tags
var links = document.getElementsByTagName('a');

// cant just do setAttribute - can only do that on 1

// cant use for each because its not a real array

// get the text content of all the links on the page
for( var i = 0; i < links.length; i++) {
	console.log(links[i].textContent);
}

// 2 - make links new color and have a border
for( var i = 0; i < links.length; i++) {
	links[i].style.background = 'pink';
	links[i].style.border = '1px dashed purple';
	links[i].style.color = 'orange';

}

// 3 - change hrefs too
for(var i = 0; i < links.length; i++){
	// this just prints out every href in every link
	console.log(links[i].getAttribute('href'));
}

// some of them are to javascript:void(0) or null 
// or relative folder path

// change them all to bing.com
for(var i = 0; i < links.length; i++){
	links[i].setAttribute('href', 'http://bing.com');
}

