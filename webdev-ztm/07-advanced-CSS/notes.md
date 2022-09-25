# Advanced CSS

## Critical Render Path

 * Browser requests html file
 * Browser notices it needs a css file, requests that
 * Browser notices it needs a font, requests that

Browser could start rendering other areas, but not text because it's waiting for font files. Sometimes it has the font but is waiting for the text.

Want to make sure your CSS is not too large, so it loads quicker.

## Flexbox

Flexbox is a popular layout tool in CSS. To enable it, use `display: flex;` on the container, and set the appropriate attributes to get the results you're looking for.

## CSS3

When using new features of the latest CSS, it's important to make sure what you build is supported in all browsers your viewers use.

If a feature has not been fully implemented, you may still be able to use it, but with a browser-specific prefix. Example `-moz-box-shadow: 4px 4px 5px #888;`

## Responsive

Responsive UI is a design that dynamically changes to account for different sizes of viewer window. It should look good in any size window.

## Misc Links

[CSS Minify](https://www.cleancss.com/css-minify/)

[CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

[Flexbox Froggy](http://flexboxfroggy.com/)

[Flexbox Cheatsheet](https://darekkay.com/dev/flexbox-cheatsheet.html)

[CSS Browser Support Reference](https://www.w3schools.com/cssref/css3_browsersupport.asp)

[Can I Use?](https://caniuse.com/)

[ShouldIPrefix.com](http://shouldiprefix.com/)

[CSS Autoprefixer Tool](https://autoprefixer.github.io/)

[CSS Transitions and Transforms for Beginners](https://robots.thoughtbot.com/transitions-and-transforms)

[Practice CSS](https://learn.freecodecamp.org/responsive-web-design/basic-css)