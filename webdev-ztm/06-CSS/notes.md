# CSS

## Basic Layout
```
Selector {
    Property: Value;
}
```

## Ordering your CSS

It is good practice to start with more general tags at the top of your CSS file, such as `body`, and work your way down to more specific tags, like `p`.

## Link to CSS

External: In the head tag of the html file:

`<link rel="stylesheet" type="text/css" href="path/to/file/style.css">`

Internal Inline: In a tag like header, you can include the style directly:

`<header style="background-color: black;">`

Internal Head: In the head you can use a `script` tag to include your CSS data.

## Meaning

CSS stands for Cascading Style Sheets. Cascading, because final styling depends on the order of value assignment in the parsing of the css file. As the styles are read, later values for identical properties will overwrite the ones that came before it.

## Separation of Concerns

It's considered best practice to keep a separate .css file, to separate things out. Use HTML for content, and CSS for formatting.

## CSS Cheat Sheet

```
CSS Cheat Sheet

Reference:
https://www.w3schools.com/cssref/css_selectors.asp
https://css-tricks.com/almanac/

Cascading Style Sheets at the most basic level it indicates that the order of CSS rules matter.

Most Common Selectors
---------------------
.class
#id
*
element
element, element
element element
element > element
element + element
:hover
:last-child
:first-child
!important (not recommended)


What seletors win out in the cascade depends on:
-Specificity
-Importance
-Source Order
```

## Element Joiners

`element1 {` - applies values to element
`element1, element2 {` - applies values to element1 and element2
`element1 element2 {` - applies values to element2 that are also element1
`element1 > element2 {` - applies values to element2 that have a parent of element1
`element1 + element2 {` - applies values to element2 that comes right after element1

## Images

`float` is a good way to position images within text, but should only be used with images.

After floating, if you have other content you don't want next to the image, define another property under the float, for `clear: both;`

## px vs em vs rem

px is a measure of pixels. em is a multiplier of the containing element. rem is similar but for the root element (html usually for websites)

## Misc Links

http://paletton.com/

https://css-tricks.com/almanac/

https://css-tricks.com/

https://unsplash.com/

[W3C CSS Selector Reference](https://www.w3schools.com/cssref/css_selectors.asp)

[More about Cascade and Inheritance](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

[Specificity Calculator](https://specificity.keegan.st/)

[CSS Bento Game](https://css-diner.netlify.app/)

[Google Fonts](https://fonts.google.com/)

[px, em rem, %, VW, and VH](https://elementor.com/help/whats-the-difference-between-px-em-rem-vw-and-vh/)

[CSS Quiz](https://www.w3schools.com/css/css_quiz.asp)

[CSS Exercises](https://www.w3schools.com/css/exercise.asp)