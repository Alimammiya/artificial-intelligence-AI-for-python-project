## 5 CSS Bad Coding Habits

A lot of time I check HTML/CSS and I got a collection of mistakes. And I'd like to share my collection of CSS bad habits that I saw in the majority of cases.

##Defining properties for all elements and then reset one of them
I face how people set some property and then reset it. That leads me to confuse because I like shortly CSS. And I want to show my vision in the following example.

There is an issue when you should set margins between elements. How people do. At first, they set to all elements and then reset from the first or last element. So they'll get 2 at-rules.

But there are selectors such as the nth-child/nth-of-type selectors, the :not() pseudo-class, or the next-sibling combinator (known as +) that help to write same in 1 at-rule.

This lifehack helps me to save the compact size of my CSS. So I hope you'll apply it in your work.

**don't do this**
```css
.item {
  margin-right: 1rem;
}

.item:last-child {
  margin-right: 0;
}
```
**You can use this instead**
```css
.item:not(:last-child) {
  margin-right: 1rem;
}
/*or*/
.item:nth-child(n+2) {
  margin-left: 1rem;
}
/*or*/
.item + .item {
  margin-left: 1rem;
}
```
##Defining display: block to absolutely positioned or fixed positioned elements
The popular mistake that I often meet is you add display: block to elements with position: absolute or position: fixed. You shouldn't do that because browser sets display: block itself for elements with position: absolute or position: fixed. 

That can't be changed. Besides, the inline or inline-block value will be changed to block, inline-flex -> flex, inline-grid -> grid, and inline-table -> table for the same reason.

**don't do this**
```css
.button::before {
  content: "";
  display: block;
  position: absolute;
}
/*or*/
.button::before {
  content: "";
  display: block;
  position: fixed;
}
```
**You can use this instead**
```css
.button::before {
  content: "";
  position: absolute;
}
/*or*/
.button::before {
  content: "";
  position: fixed;
}
```
##Using the transform: translate(-50%, -50%) approach for centering
For a long time, there is the approach of centering elements using the transform property. I'm sure you wrote transform: translate(-50%, -50%) at least once.

In this approach we have to use the set of 5 properties. I'd like to share the approach that'll allow reducing the code to the two properties.

You probably heard auto margins is one of the main benefits of flexbox. That's happened because it's works predictable. We don't need to know the element's width and height so that it's centered.

We just write margin: auto, if there is free space a browser will display by the center. If no, anyway, a browser will display it accurately.

So that's my favorite way that will help in 100% of cases.

**don't do this**
```css
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```
**You can use this instead**
```css
.parent {
  display: flex;
}

.child {
  margin: auto;
}
```
##Defining width: 100% to block-level elements
There is a popular practice of using flexbox to create a multi-column grid that transforms to a single column. I think using flexbox for a multi-column grid is ok but not for creating a single-column. 

In this case grid's items stretch out for on parent width using width: 100%. But we forget grid's items are block-level elements that stretch that way by default. 

So we don't need to use the width: 100%. Just use flexbox only when you need to create a multi-column grid.

**don't do this**
```html
<div class="parent">
  <div class="child">1</div>
  <div class="child">2</div>
  <div class="child">3</div>
  <div class="child">4</div>
</div>
```

```css
.parent {
  display: flex;
  flex-wrap: wrap;
}

.child {
  width: 100%;
}

@media (min-width: 1024px) {
  
  .child {
    width: 25%;
  }
}
```
**You can use this instead**
```html
<div class="parent">
  <div class="child">1</div>
  <div class="child">2</div>
  <div class="child">3</div>
  <div class="child">4</div>
</div>
```
```css
@media (min-width: 1024px) {

  .parent {
    display: flex;
    flex-wrap: wrap;
  }
  
  .child {
    width: 25%;
  }
}
```
##Defining display: block to flex-items
There is an important feature when we use flexbox. When you write display: flex for the element all its child elements (flex items) are blockified. 

What does it mean? All flex items that are set the display property with the inline, inline-block, inline-flex, inline-grid, or inline-table values will be changed. The inline and inline-block will changed to block, inline-flex -> flex, inline-grid -> grid and inline-table -> table. 

So don't use the inline-* values and your code will be saved clear.

**don't do this**
```css
.parent {
  display: flex;
}

.child {
  display: block;
}
```
**You can use this instead**
```css
.parent {
  display: flex;
}
```
Originaly posted on - [melnik909](https://dev.to/melnik909/5-css-bad-coding-habits-1he3)