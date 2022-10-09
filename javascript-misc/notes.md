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
first.addEventListener("click", handler1);
first.addEventListener("click", handler2);
second.onclick = handler1;
second.onclick = handler2;
```

HTML:
``` html
<div id="first">First Element</div>
<div id="second">Second Element</div>
```

Clicking *“First Element”* will trigger 2 alerts. Clicking on *“Second Element”* will trigger only the second alert! **With addEventListener, you can attach multiple events to the same element, but not with onclick.**
