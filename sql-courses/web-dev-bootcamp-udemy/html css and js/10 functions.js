// 1- write declarations and expressions = 2 - return, 3 - def
// scope and higher-order fxns

// fxn doSomething() { code}
// doSomething()

function doSomething() {
	console.log('hello world');
}
doSomething(); //running this in console will print it
//but fxn needs to return something in order for the browser to run it

doSomething // reference - typing fxn without parethesis shows the code in the fxn

// 102
function square(num) {
	console.log(num*num)
}
square(5)

function sayHi(name1, name2, name3) {
	console.log('hi ' + name1);
	console.log('hi ' + name2);
	console.log('hi ' + name3);
}
sayHi('bob', 'bill') //3rd line just says hi undefined

function area(length, width) {
	console.log(length * width);
}

// addToScore(num) or checkCredentials(email, pw)

// 103 - return keyword
4 + square(4) //this would return square(4) is undefined unless we use return

// fix so it returns. print returns 'undefined'
function square(num) {
	return num*num;
}

// store, return later
var result=square(104);
result

// a fxn declaration
function capitalize(str) {
	return str.charAt(0).toUpperCase() + str.slice(1);
}
var city = 'paris';
var capital = capitalize(city);

// fxn expression
var capitalize = function(str) {
	return str.charAt(0).toUpperCase() + str.slice(1);
}

var sayHi = function(){
	console.log('hello');
}
// call
sayHi()

// or decide that var is now equal to something else, cant use fxn anymore then
sayHi = 34;
// sayHi() //34

// 104 - fxns quiz

// fxn stops once your return 80. doesnt do any lines after that
function test(x) {
	return x*2;
	console.log(x);
	return x/2;
}
test(40);

// 105 - fxns pset

// 1- write fxn isEven()
function isEven(x) {
	return x%2==0;
}
isEven(4);
isEven(21);

// 2- write factorial()
function factorial(num) {
	var result=1
	// now multiple it by every num b/w result and num
	for(var i = 1; i<= num; i++) {
		result = result*i; // result *= i
	}
	return result;
}

// def result var
// calculate factorial, store val in result
// return result var

// could also count down
function factorialD(num) {
	if(num === 0) {
		return 1;
	}

	var result=num;
	// now multiple it by every num b/w result and num
	for(var i = num-1; i >= 1; i--) {
		result = result*i; // result *= i
	}
	return result;
}

// 3 - takes - replace them with _
function kebabToSnake(str) {
	// replace all - with _
	var newStr = str.replace(/-/g, '_');
	// return str
	return newStr;
}

	// for(var l=0; l < str.length; l++) {
	// 	if(l==='-') {
	// 		l === '_';
	// 	}
	// }

// 107 - scope - the context that some code is executed in
// variables, properties visible in the fxn

function doMath() {
	var x=40;
	console.log(x);
}
doMath() // in this fxn, in this scope, x=40
// inside the fxn x=40. in global scope, x is not defined

// fxn has its own scope, its own set of variables. can access global

var y=99;
function doMoreMath() {
	console.log(y); //y is defined globally, fxn takes it
}
doMoreMath(); //works, prints 99

function doMoreMath() {
	y=100;
	console.log(y); //y is defined globally, fxn takes it
}
doMoreMath(); // prints out the local variable y, not global variable y

y; // globally it was 99, we made it 100 in fxn.

var phrase = 'hi there'
function doSomething() {
	var phrase = 'goodbye';
	console.log(phrase);
}
doSomething() // it printed the local goodbye
phrase ; // since we added 'var' to phrase locally, outside is still original str

// 108 scope quiz

// num1
var num=8;
function doMath() {
	num += 1;
	if(num % 5 == 0) {
		return true
	}
	else {
		return false
	}
}

num += 1;
doMath() //returns true. we set it to 9, it runs on that

// if have 2 fxns
function hi() {
	var name='bob';
	console.log(name);
}

function bye() {
	console.log(name);
}

// run hi, obv get bob
hi();

// run bye, it will be undefined, name is not defined globally or locally
bye();
// name is not accessible in the scope of the bye fxn

// 109 - higher order fxns code along - pass fxns to other fxns

// setInterval - takes fxn, calls it every x milliseconds
function sing() {
	console.log('twinkle twinkle');
	console.log('how i wonder');
}
setInterval(sing, 7000);
// it returned the number 2

// dont need to put in sing(), we dont want to execute it, let this fxn execute it. we just pass value of sing
// to stop it, type in that 2 it gave us
clearInterval(2);

// write fxn directly in once - anonmyous fxn
setInterval(function() {
	console.log('this is an anon fxn');
	console.log('run this a few times');
}, 2000);