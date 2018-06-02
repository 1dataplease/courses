// jquery api documentation homepage
// .text() gets combined text contents of each element

// grab the text(Content) from h1
$("h1").text();

// get all the text inside a ul with spaces in bw
$("ul").text();

// get all text from lis, returns it as 1 string
$("li").text();

// can replace text without selecting then textContent
$("h1").text("New Text");

// after running above and below in console
// this will return new text
$("h1").text();

// can change all lis
$("li").text('hey');

// html - gets or sets contents of 1st or every element
$("ul").html();
// returns a string of <lihey<li * 3

// replace current ul with new one
$("ul").html("<li>I hacked your ul</li>");

// could replace it with 2 lis
$("ul").html("<li>I hacked your ul</li> <li>aha</li>");

// if select both lis, change html of both to be anchor
$("li").html("<a href='google.com'>Click for google</a>");

// text doesnt treat what you pass it as html. just str
$("li").text("<a href='google.com'>Click for google</a>");

// if user typing it in, treat it as html not text



// 161 - attr and val
// get/set val of attr in 1st element or every matched element

// get the img, pass in alt, pass in new value for alt
$("img").attr("alt", "sorry, doesnt display");

// can also have an object storing alt and title
imgObject = {
	alt: 'sorry doesnt work',
	title: 'title'
}
$("img").attr(imgObject);

// or can do it without storing obj as a variable
$("img").attr({
	alt: 'sorry',
	title: 'title'
});

// look at the current width
$("img").css("width");

// select the img, make it smaller - possible 2 ways
$("img").css("width", "100px");
$("img").attr("width", "100px");

// now look at it and change to new picture
$("img").attr("src", "lib/scary.png");

// change to new pic and new width
$("img").attr({
	"src" : "lib/scary.png",
	"width" : "100px"
});

// select the input (type=text), change the type value
// get the type
$("input").attr("type");

// change it to be a checkbox
$("input").attr("type", "checkbox");

// change value
$("input").attr("value", "typed in already");

// only change the 1st img to the scary one
// there cannot be a space b/w img and first
$("img:first").attr("src", "lib/scary.png");
// also works, a little faster since css-native
$("img:first-of-type").attr("src", "lib/scary.png");

// second-of-type doesnt work

// last im
$("img").last().attr("src", "lib/scary.png");

// summarize attr - just 1 arg, then it returns value; getter
// 2 args - updates every element we've selected; setter

// text for textContent
// html for innerHTML
// val - jquery wrapper for value

// select the text input, see what the value is
$("input").val();

// set new value
// like clearing the value
// enter adds new li, erases content in there
$("input").val("new text in here");

// works on all elements that have a value attribute
// checkbox, color inputs, 
// dropdown menus / select element w options

// know what choice they selected in dropdown
$("select").val();



// 162 - classes, wrappers for .add .remove .toggle

// 125