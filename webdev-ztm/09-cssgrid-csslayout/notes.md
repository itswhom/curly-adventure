# CSS Grid + CSS Layout

## CSS Grid vs Flexbox vs Bootstrap

CSS Grid can be used with Flexbox to achieve great results.

Flexbox is really good for one-dimensional layouts, while CSS Grids are really good for two-dimensional layouts, like galleries. It is more important to know these than Bootstrap these days, since it is newer and more integrated within CSS3 itself.

## CSS Grid 3

### Containers

On the container, use `display: grid;` to set it up as a grid. Then, use `grid-template-columns: {values};` to set up the columns. In {values}, we can use the following:

 * 300px 300px - two columns, 300px each
 * 25% 25% 25% 25% - four columns, a percentage of the window (does not account for gaps)
 * 1fr - divides the window into one fraction (accounts for gaps)
 * 1fr 1fr - divides the window into two equal fractions
 * 1fr 1fr 2fr - three columns, first two columns are half the size of third

`gap: 20px;` will put a margin between grid items.

`grid-template-rows: {values};` defines the row layout/sizing.

 * 1fr 2fr - First row is the size of one fraction, second row is twice that size. The row sizing will repeat.

In the {values} area, you can use `repeat(3, 1fr);` to create 3 items of 1fr size each. This will not move items to a newline if the window shrinks past content minwidth. Instead, you can use `repeat(auto-fill, 300px);` to include as many columns as will fit in the window width, putting overflow content to the next line. To stretch content to the window size and stay fully responsive, use `repeat(auto-fill, minmax(200px, 1fr));`.

In the {values} area, you can use `auto;` in place of 1fr to scale the size to fit the content.

`justify-items` default is `stretch`, but other values change how items are aligned in the window.

### Items

Individual items within a container can be styled to have different grid properties.

``` css
.item {
    grid-column-start: 1;
    grid-column-end: 3;
}
```

This will make the item twice as wide, since it starts at column 1 and ends at column 3. If you make it end at 4, it will be three times as wide as a single item. Shorthand for this is:
``` css
.item {
    grid-column: 1/3;
}
```
In CSS Grid, you can go from first column to the end by using -1:
``` css
.item {
    grid-column: 1/-1;
}
```
We don't always know what columns our item will rest against, so a good way of keeping things modular is to use span. This can also be done for rows:
``` css
.item {
    grid-column: span 2;
    grid-row: 1/3;
}
```
Other properties that could be helpful are justify and align. These can push items to the start, end of the window:
``` css
.item {
    justify-self: start;
    align-self: end;
}
```

## Misc Links

[Grid Gap -> Gap](https://developer.mozilla.org/en-US/docs/Web/CSS/gap)

[CSS Grid - Auto Fill vs Auto Fit](https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit)

[CSS Grid Cheatsheet](http://grid.malven.co/)

[CSS Grid Garden](http://cssgridgarden.com/)

[Another CSS Cheatsheet](https://web.dev/learn/css/)

