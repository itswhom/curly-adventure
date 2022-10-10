# JavaScript Notes

## Basic JS Event Workflow

[JavaScript Event Reference](https://developer.mozilla.org/en-US/docs/Web/Events)

1. What DOM node/element do we want to listen for events on?
2. What event should trigger additional code to run?
3. What code should be run once the trigger occurs?

Example from Dani Krossing [[link](https://www.youtube.com/watch?v=mlxi1WUSO_8)]
``` javascript
let menuBtn = document.querySelector(".menu-btn"); // 1. What node to listen to?
let menu = document.querySelector(".menu");
let menuStatus = false;

menu.style.marginLeft = "-300px";

function menuToggle() { // 3. What code should run once triggered?
        if (menuStatus == false) {
                menu.style.marginLeft = "0px";
                menuStatus = true;
        }
        else if (menuStatus == true) {
                menu.style.marginLeft = "-300px";
                menuStatus = false;
        }
}

menuBtn.addEventListener("click", menuToggle); // 2. What event triggers the code?

// call function when button is clicked
// same as in html: <a onclick="menuToggle()"> for example
// same as in js: menuBtn.addEventListener("click", menuToggle);
```

## onClick vs addEventListener("click")

From @annapeterson89: [[link](https://medium.com/@annapeterson89/addeventlistener-vs-onclick-which-one-should-you-draft-into-your-fantasy-football-team-16ea9ae71ee0)]

JS:
``` js
const first = document.getElementById("first");
const second = document.getElementById("second");
function handler1() {
alert("First handler");
}
function handler2() {
alert("Second handler");
}
first.addEventListener("click", handler1); // event listeners
first.addEventListener("click", handler2);
second.onclick = handler1; // event handlers
second.onclick = handler2;
```

HTML:
``` html
<div id="first">First Element</div>
<div id="second">Second Element</div>
```

Clicking *“First Element”* will trigger 2 alerts. Clicking on *“Second Element”* will trigger only the second alert! **With addEventListener, you can attach multiple events to the same element, but not with onclick.**

## Prevent Default Event Behavior

(from mmtuts)

Preventing default behavior, for example, clicking an `<a>` tag that links to "#" will reload the page, so we may want to disable that action.

``` js
let btn = document.querySelector(".test-btn"); // button at bottom linked to #
let form = document.querySelector(".test-form"); // form submit button

function changeBtnText(e) {// capture relevant object's events in var e
        e.preventDefault();// prevents default behavior contained in e
        btn.innerHTML = "YAY";
}

function stopFormSubmit(e) {
        e.preventDefault();// prevent form from being submitted
}

btn.onclick = changeBtnText;
form.onclick = stopFormSubmit;
```

## Anonymous Functions in EventListeners

 * If you are using a one-time function when a listener event occurs
 * If you need to call a function on a listener event, and need to pass in parameters

``` js
let btn = document.querySelector(".testBtn");

function firstFunction(e, name) {
        e.preventDefault();
        btn.innerHTML = name;
}

btn.addEventListener("click", function(e) { // passing parameters via listener
        firstFunction(e, "Daniel");
});
btn.addEventListener("click", function() { // multiple listeners can exist
        btn.style.backgroundColor = "yellow";
});
```