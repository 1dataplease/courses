// 1 - use code to define arrays; remove or add elements from/to it
// 2 - use pop, push, shift, unshift - builtin methods
// 3 - to-do list using arrays

// 111 - array is first data structure
var person1 = 'bob';
var person2 = 'bo'; 
var person3 = 'bill'; 
var friends = ['bob', 'bo', 'bill'];
console.log(friends[0]); //bob
friends[1] + ' <3 ' + friends[2]; // bo hart bill

// can update array values
friends[0] = 'bobby'; 
friends[2] = 'billy';

var colors = ['red', 'orange', 'yellow'];
colors[1];

// add in a new element
colors[3] = 'green';
colors[10] = 'purple'; // adds in 6 undefineds, then purple

var newarray = [];
var newerarray = new Array() //uncommon

// arrays can hold any type of data
var random_stuff = [49, true, 'harry', null];

// arrays have a length property
random_stuff.length //4


// 112 array methods - push/pop, shift/unshift, indexOf, slice

// if want to add blue to colors, have to track length
// push - just add it on the end
colors.push('blue'); //adds blue to end and returns length 6
colors;

// pop just removes last element, 0 arguments
colors.pop(); //returns 'blue', and removed it

//unshift adds it to the front of an array
colors.unshift('infrared');

//shift removes the first item of an array
colors.shift(); // returns 'infrared'

// indexOf - takes str or num, tries to find it returning index
random_stuff.indexOf('harry'); //returns indexof 2
// return -1 if not present

// slice - copy parts of an array
var fruits = ['banana', 'orange', 'lemon', 'apple'];
var citrus = fruits.slice(1,3); //orange and lemon
var fruitcopy = fruits.slice(); // copies entire array


// 113 - array exercises
console.log(fruits[fruits.length]); // returns undefined

// 114 - simple to-do-list app - see files in this folder

// 115 - array iteration
// comments stored in array, code loops thru and
// makes some html content like p or li, div
// for each blog in array of blogs, make a post
// for loop, forEach

var colors = ['red', 'orange', 'yellow', 'green'];

// print each
for(var i=0; i < colors.length; i++) {
	console.log(colors[i]);
}

// // example of a code in html use
//for(var i=0; i < comments.length; i++) {
	// makeCommentHTML(comment[i]);
// }

//// for each
// a method for any array
// takes a fxn as an argument
// mostly we pass in an anon fxn like a lambda
// that fxn is called for every element in the array

colors.forEach(function(color){
	// color is a placeholder, call it whatever
	console.log(color);
})

// repeat this print we asked for 4 times (each item in array)
colors.forEach(function(){
	// color is a placeholder, call it whatever
	console.log('inside the foreach');
})

// repeat this print x4 - adds each item to end
colors.forEach(function(dogs){
	// color is a placeholder, call it whatever
	console.log('inside the foreach: ' + dogs);
})

// another way tp define and pass in fxn
function printColor(color) {
	console.log('*********');
	console.log(color);
	console.log('*********');
}
printColor('purple');
colors.forEach(printColor);
printColor(colors[0]);
printColor(colors[1]);

// same way of doing same w for loop
for(var i = 0; i < colors.length; i++) {
	console.log(colors[i]);
}

colors.forEach(function(color){
	console.log(color);
});

// same with while loop
count = 0
while(count < colors.length) {
	console.log(colors[count]);
	count++;
}


// for loop - dealing with a num, use it to access array
// forEach - dealing with an anon fxn name you make up


// 116 - ex - whats this print out
var numbers = [1,2,3,4,5,6,7,8,9,10];

// prints 3,6,9. nothing to do w colors array
numbers.forEach(function(color){
	if(color % 3 === 0) {
		console.log(color);
	}
})

// same but in a forloop
for(i=0; i< numbers.length; i++){
	if(numbers[i] % 3 === 0) {
		console.log(numbers[i])
	}
}


//117 - to do list, array iteration

// 118 - ps

// 1 - fxn that takes 1 argument - an array. fxn prints it 1 line at time
// in reverse order
function printReverse(array){
	for(var i= array.length - 1; i >= 0; i--) {
		console.log(array[i])
	}
}

printReverse(['a', 'b', 'c']);


// 2 - isUniform - takes array, returns true if all elements same
function isUniform(array){
	var first = array[0];

	for(var i=1; i < array.length; i++) {
		if(first !== array[i]){
			return false;
		}
	}
	return true;
}

// doesnt work, always returns true
// function isUniform2(array){
// 	var first = array[0];

// 	array.forEach(function(element) {
// 		if(element !== first){
// 			return false;
// 		}
// 	});
// 	return true;
// }

isUniform(['a', 'b', 'c']);
isUniform(['a', 'a', 'a']);


// 3 - sumArray takes array of nums, returns the sum
function sumArray(array) {
	var sum = 0;
	for(i = 0; i < array.length; i++) {
		sum += array[i];
	}
	return sum;
}

function sumArray2(array) {
	var sum = 0;
	array.forEach(function(element){
		sum += element;
	});
	return sum;
}

sumArray([1,2,3]);
sumArray2([11,2,3]);


// 4 - max of nums
function max(array) {
	var currentMax = array[0];
	for(i = 0; i < array.length; i++) {
		if(array[i] > currentMax) {
			currentMax = array[i];
		}
	}
	return currentMax;
}

max([12, 123, 1, 9]);



// 120 - optional - how forEach works. build own version of it

colors.forEach(function(color){
	// color is a placeholder, just a name for each element in the array
	console.log(color);
});

// template to start, define own
myForEach(arr, function()) {
	console.log(color);
}

// how we would run it
myForEach(arrNums, function(num) {
	console.log(num);
});

// defining it
function myForEach(arr, fxn) {
	for(var i=0; i < arr.length; i++){
		fxn(arr[i]);
	}
}

// running my version of it - runs the alert function, we didnt pass in string/name tho
myForEach(colors, alert);

// most the time we dont pass in a fxn name, we pass in an anon fxn
myForEach2

// this temporarily creates an anon fxn, doesnt get used and it disappears
(function() {
	console.log('im a fxn');
});

// to actually run the above, add 2 parentheses after it
(function() {
	console.log('im a fxn');
})();
























