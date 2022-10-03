# DOM Manipulation

## DOM Selectors

Accessing the DOM elements are done using `document` object.

 * getElementsByTagName
 * getElementsByClassName
 * getElementById

 * querySelector
 * querySelectorAll

 * getAttribute
 * setAttribute

## Changing Styles
 * style.{property} //ok

 * className //best
 * classList //best

 * classList.add
 * classList.remove
 * classList.toggle

## Bonus
 * innerHTML //DANGEROUS

 * parentElement
 * children

**It is important to CACHE selectors in variables**

## Callback Functions
When adding event listeners, do not use the `()` after the function name, because we are not trying to run the function yet. Example:
``` js
button.addEventListener("click", addListAfterClick);
input.addEventListener("keypress", addListAfterKeypress);
```

## Misc Links

[HTML DOM (Document Object Model)](https://www.w3schools.com/js/js_htmldom.asp)

