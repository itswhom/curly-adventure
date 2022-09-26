# JavaScript

## What is JavaScript?

JavaScript was made in 1995 by Netscape web browser. It lets you perform actions within a web browser. *Play* a video. *Sign up* for a newsletter. *Like* a comment. *Expand* a menu.

JavaScript also comes into play with Node.js, Express.js, React, and more.

## Some basic JavaScript

 * Must start with a letter, $, or _
 * camelCase is best practice

Ask user for input:
``` js
let gotInput = prompt("Enter some data");
```
This gathers the data as a string, so to convert to a number:
``` js
let numInput = Number(gotInput);
```
Popup alert syntax:
``` js
alert("Boo! Here's an alert.");
```
## Conditionals
Basic if/else syntax:
``` js
if (someCondition === true) {
    print("execute this code");
} else if (someCondition === false) {
    print("this is pretty redundant but ok");
} else {
    print("some other result");
}
```
## Inserting JS Into HTML
You can enter the following to get a .js file loaded on your html page:
``` js
<script type="text/javascript" src="script.js"></script>
```
## Print to JS Console
Print output to the Javascript console with:
``` js
console.log("hiiii");
```
## Functions
There are built in functions, like `alert()` and `prompt()`. You can also create your own functions.

 * `alert` is a function
 * `alert()` is a function being called
 * `alert("Hi")` is a function being called with an argument "Hi"

Create your own function with a declaration:
``` js
function sayHello() {
    console.log("Hello");
}
```
After creating a function, you need to actually call it in order to run the code within. For the above function, run it with `sayHello()`. You can also create a function with an expression. This is called an anonymous function:
``` js
var sayBye = function() {
    console.log("Bye");
}
```
Arguments can be added to a function to accept inputs:
``` js
function sing(song) {
    console.log(song);
}

sing("Laa dee daa");
sing("hellooooooo");
sing("backstreet's back all right");
```
Functions are very useful when they return values:
``` js
function multiply(a, b) {
    return a * b
}

multiply(5, 10);
```
Return also exits the function it's in, so it is often used to break out of a function.
## Arrays
Set up an array with:
``` js
var list = ["tiger","cat","bear"];
```
Access array items with:
``` js
console.log(list[1]);
> "cat"
```
Multi-dimensional arrays:
``` js
var bigArray = [
    ["tiger","cat","bear"];
]
console.log(bigArray[0,2]);
> bear
```
List methods:
 * `list.shift()` - returns and removes the first item and moves all indices to the left one
 * `list.pop()` - returns and removes the last item in the array
 * `list.push("elephant")` - adds argument to the end of the array and returns number of items
 * `list.concat(["bee","deer"]` - adds the array in the argument to the variable array
 * `list.sort()` - sorts the original variable array
## Objects
Objects are a collection of properties:
``` js
var user = {
    name: "John",
    age: 34,
    hobby: "Soccer",
    isMarried: false,
};
```
To grab the properties of an object:
``` js
console.log(user.name);
console.log(user.age);
// etc
```
Add properties to an object:
``` js
user.favouriteFood = "spinach";
```
If you include a function as the value of a class property, this is called a method. In the following example, shout() would be a method of user:
``` js
var user = {
    name: "John",
    shout: function() {
        console.log("AHHHHH!");
    };

};
// call with:
user.shout();
```
## Loops

For loop example:
``` js
for (var i=0; i < todos.length; i++) {
    console.log(i);
}
```

While loop example:
``` js
var counterOne = 0;
while (counterOne < 10) {
    console.log(counterOne);
    counterOne++
}
```

Do loop example:
``` js
var counterTwo = 10;
do {
    console.log(counterTwo);
    counterTwo--;
} while (counterTwo > 0);
```

ForEach loop example:
``` js
function logTodos(todo, i) {
    console.log(todo, i);
}
todos.forEach(logTodos);
todosImportant.forEach(logTodos);
```
## Misc Links

[W3C Array Methods](https://www.w3schools.com/jsref/jsref_obj_array.asp)

