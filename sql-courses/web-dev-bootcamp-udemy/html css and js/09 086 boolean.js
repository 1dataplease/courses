//rule of thumb - always use ===; is safer and specific

var x = 99;

// == performs type coercion
x == "99" //true

// === does not coerce the datatype
x === "99" //false

var y = null
y == undefined //true
y === undefined //false

// weird examples
true == '1' //the only string number where this is true
true == '12' //false

0 == false //true, because lack and false, different datatype same value
null == undefined //true
NaN == NaN //false

//087 - logical operators

// && is AND
// || is OR
// ! is NOT

//ex 1
var x=10;
var y="a";
y === 'b' || x>=10; //true

//ex 2
var x=3;
var y=8;
!(x=='3' || x===y) && !(y != 8 && x <= y); //F

// every value is truthy or falsy
!'hi world'; //f
!0 //t
!-1 //f
!NaN //t
!'' //t
!null //t

//ex 3
var str ='';
var msg = 'haha';
var isFunny = 'false';

!((str || msg) && isFunny); //f

// 87 - logical operators / conditionals
var age = prompt('how old u');

if(age < 18) {
	console.log('cannot enter');
}
//below only runs if the above statement is false
else if(age < 21 && age >= 18) { // dont need && age >=18
	console.log('enter but no drinks')
}
else if(age == 21) {
	console.log('happy 21st birthday, come in, free drink!')
}
else {
	console.log('come in, have drinks')
}

if(age % 2 === 1) {
	console.log('your age is odd')
}
//dont know how to calculate perfect square without sqrt fxn

// 089 - simple number guessing game









