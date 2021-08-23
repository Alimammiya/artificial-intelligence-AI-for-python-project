## 4 Important Differences Between Regular And Arrow Functions

Regular and arrow functions are often used interchangeably. Yet, they are not the same. There are some important differences between these two. This tutorial will tell you about four of these differences. This will help you recognize when to use regular functions and when to use arrow functions.

## Forms of functions

In modern JavaScript, there are two ways to write functions. You can use either [regular functions] or you can use [arrow functions]. If you decide to use regular functions, you can choose from two types of syntax. The first one is [function declaration]. The second one is [function expression].

```JavaScript
// Function declaration example:
function calculateCircleArea(radius) {
  return MathMath.PI * (radius ** 2)
}

// Function expression example:
const calculateCircleArea = function(radius) {
  return MathMath.PI * (radius ** 2)
}
```

If you decide to use arrow function, things get easier. For arrow functions, there is only one type of syntax you can use, function expression.

```JavaScript
// Arrow function example:
const calculateCircleArea = (radius) => {
  return MathMath.PI * (radius ** 2)
}
```

If you compare the syntax of a regular function (expression) and arrow function, you find two differences: `function` keyword and `=>` (fat arrow). A more interesting, and important, question is, what are the differences beyond the syntax?

## The _this_

The first important difference between regular and arrow function is the `this` keyword. In case of regular functions, the `this` is very dynamic. It can behave in four different ways depending on the situation.

### Global scope (with regular functions)

When you invoke a regular function in a global scope, the value of `this` will be global object `window`. If you invoke the function a strict mode, the value of `this` will be `undefined`.

```JavaScript
// Create regular function in a global scope:
function logThis() {
  console.log(this)
}

// Call logThis():
logThis()
// Output:
// {
//   window: Window,
//   self: Window,
//   ...
// }


// With strict mode:
// Turn on strict mode:
'use strict'

// Create regular function in a global scope:
function logThis() {
  console.log(this)
}

// Call logThis():
logThis()
// Output:
// undefined
```

### Object methods (with regular functions)

If you use a regular function to define an object method and invoke it, `this` will be the parent object. It will be the object inside which you defined the method.

```JavaScript
// Create a simple object:
const user = {
  name: 'user',
  active: true,
  // Create object method:
  getParentObj () {
    // Return this:
    return this
  }
}

// Call the "getParentObj()" method on "user" object:
user.getParentObj()
// Output:
// {
//   name: 'user',
//   active: true,
//   getParentObj: ƒ getParentObj()
// }
```

### Constructors (with regular functions)

When you use a regular function to create [function constructor], the `this` will be individual instance you create with that constructor.

```JavaScript
// Create a function construct or that accepts one parameter:
function MyFunctionConstructor(name) {
  // Use parameter to create prop:
  this.name = name

  // Log this:
  console.log(this)
}

// Create the first instance of "MyFunctionConstructor":
const myFunctionInstanceOne = new MyFunctionConstructor('Charlie')
// Output:
// MyFunctionConstructor {
//   name: 'Charlie',
//   __proto__: { constructor: ƒ MyFunctionConstructor() }
// }

// Create the first instance of "MyFunctionConstructor":
const myFunctionInstanceTwo = new MyFunctionConstructor('Jenny')
// Output:
// MyFunctionConstructor {
//   name: 'Jenny',
//   __proto__: { constructor: ƒ MyFunctionConstructor() }
// }
```

### The _call()_ and _apply()_ (with regular functions)

Lastly, you can also invoke function indirectly using [apply()] and [call()] methods. These two methods allow you to change the value of `this` of a function and invoke it using that new `this`. This means that `this` can be anything you want.

```JavaScript
// Create object for new "this":
const newThis = {
  planet: 'Earth'
}

// Create a regular function:
function logThis() {
  console.log(this)
}

// Invoke "logThis()" with default this:
logThis()
// Output:
// {
//   window: Window,
//   self: Window
//   ...
// }

// Invoke "logThis()" with "call()" method
// and "newThis" object:
logThis.call(newThis)
// Output:
// { planet: 'Earth' }

// Invoke "logThis()" with "apply()" method
// and "newThis" object:
logThis.apply(newThis)
// Output:
// { planet: 'Earth' }
```

### The _this_ and arrow functions

When it comes to `this`, arrow function is much simpler and always behaves in the same way. The value of `this` is always the value from the parent, or outer, function. This is because arrow function doesn't have its own `this`. It "gets" its `this` lexically, from its lexical scope, outer scope.

If you try to change `this` of an arrow function with `call()` or `apply()`, arrow function will ignore it. It will still get its `this` from its lexical scope.

```JavaScript
// Global scope example:
// Create arrow function in a global scope:
const logThis = () => console.log(this)

// Invoke "logThis()":
logThis()
// Output:
// {
//   window: Window,
//   self: Window
//   ...
// }


// Object method example:
// Create a simple object:
const shape = {
  name: 'square',
  width: 15,
  height: 15,
  // Create object method:
  getParentObj: () => {
    // Return this:
    return this
  }
}

// Invoke "getParentObj()" on "shape" object:
shape.getParentObj()
// Output:
// {
//   window: Window,
//   self: Window
//   ...
// }


// "call()" and "apply()" methods example:
const newThis = {
  name: 'Alexander Joseph Luthor',
  alias: 'Lex Luthor',
  type: 'Egotistical Mastermind'
}

const logThis = () => console.log(this)

// Invoke "logThis()" with "call()" method:
logThis.call(newThis)
// Output:
// {
//   window: Window,
//   self: Window
//   ...
// }


// Invoke "logThis()" with "apply()" method:
logThis.apply(newThis)
// Output:
// {
//   window: Window,
//   self: Window
//   ...
// }
```

Getting `this` lexically also means that you don't have to bind object and class methods when you use arrow functions. This is something you would have to do with regular function if the `this` changes.

```JavaScript
// Regular function example:
// Create "Person" class:
class Person {
  // Add some properties:
  constructor(name, age) {
    this.name = name
    this.age = age
  }

  // Add class method:
  getName() {
    console.log(this.name)
  }
}

// Create instance of "Person":
const jack = new Person('Jack', 44)

// Log the name:
jack.getName()
// Output:
// 'Jack'

// Log the name with different this:
setTimeout(jack.getName, 1000)
// Output:
// ''

// Bind this manually:
setTimeout(jack.getName.bind(jack), 1000)
// Output:
// 'Jack'


// Arrow function example:
class Person {
  constructor(name, age) {
    this.name = name
    this.age = age
  }

  getName = () => {
    console.log(this.name)
  }
}

// Create instance of "Person":
const jack = new Person('Jack', 44)

// Log the name:
jack.getName()
// Output:
// 'Jack'

// Log the name with timeout:
setTimeout(jack.getName, 1000)
// Output:
// 'Jack'
```

## Implicit _return_

When you create a regular function, it will implicitly return `undefined`. You can change this by adding `return` statement with some expression. If you add some expression, but omit the `return` statement, regular function will return `undefined`.

```JavaScript
// Create an empty regular function:
function FnReturningNothing() {}

// Invoke "FnReturningNothing()":
FnReturningNothing()
// Output:
// undefined

// Create a regular function without return statement:
function fnWithoutStatement() {
  const randomNumber = Math.floor(Math.random() * 100)
}

// Invoke "fnWithoutStatement()":
fnWithoutStatement()
// Output:
// undefined

// Create a regular function with return statement:
function fnWithStatement() {
  const randomNumber = Math.floor(Math.random() * 100)

  return randomNumber
}

// Invoke "fnWithStatement()":
fnWithStatement()
// Output:
// 7
```

You can use the `return` statement to return some expression also from arrow functions. However, there is also a shortcut, and feature of arrow functions, to do this. If you omit the function's body curly braces, and function contains one expression, the arrow function will return that expression implicitly.

```JavaScript
// Create arrow function with implicit return:
const returnRandomNumber = () => Math.floor(Math.random() * 10)
// Note: it implicitly returns expression
// that follows after the "=>" (fat arrow).

// Invoke the "returnRandomNumber()":
returnRandomNumber()
// Output:
// 0


// The same as:
const returnRandomNumber = () => {
  // Return random number explicitly:
  return Math.floor(Math.random() * 10)
}

// Invoke the "returnRandomNumber()":
returnRandomNumber()
// Output:
// 7
```

## The _arguments_ object

When you create a regular function, JavaScript also creates a special object called `arguments`. This array-like object is accessible only inside the function. It containing the list of arguments with which you invoked the function. This applies even if the function at hand doesn't accept any parameters.

```JavaScript
// Create a regular function without parameters:
function logArguments() {
  // Log "argument" object:
  console.log(arguments)
}

// Invoke the "logArguments()":
logArguments()
// Output:
// {
//   length: 0,
//   callee: ƒ logArguments(),
//   __proto__: { ... }
// }


// Create a regular function with one parameter:
function logArguments(hobby) {
  // Log "argument" object:
  console.log(arguments)
}

// Invoke the "logArguments()":
logArguments('reading')
// Output:
// {
//   '0': 'reading',
//   length: 1,
//   callee: ƒ logArguments(),
//   __proto__: { ... }
// }


// Create a regular function with two parameters:
function logArguments(fistName, lastName) {
  // Log "argument" object:
  console.log(arguments)
}

// Invoke the "logArguments()":
logArguments('Jack', 'Jones')
// Output:
// {
//   '0': 'Jack',
//   '1': 'Jones',
//   length: 2,
//   callee: ƒ logArguments(),
//   __proto__: { ... }
// }


// Create a regular function with two parameters:
function logArguments(fistName, lastName) {
  // Log "argument" object:
  console.log(arguments)
}

// Invoke the "logArguments()" and pass more arguments:
logArguments('Jack', 'Tobias', 'Jones', 'Junior')
// Output:
// {
//   '0': 'Jack',
//   '1': 'Tobias',
//   '2': 'Jones',
//   '3': 'Junior',
//   length: 4,
//   callee: ƒ logArguments(),
//   __proto__: { ... }
// }
```

Arrow functions don't have their own `arguments` object. If you define arrow function inside a regular function, it will inherit the `arguments` object from the parent function. If you define arrow function in a global scope, and try to access `arguments` object, JavaScript will throw a `ReferenceError`.

```JavaScript
// Create arrow function in a global scope:
const logArguments = () => {
  // Try to log "argument" object:
  console.log(arguments)
}

// Invoke the "logArguments()":
logArguments()
// Output:
// ReferenceError: arguments is not defined


// Try adding parameters:
const logArguments = (a, b) => {
  // Try to log "argument" object:
  console.log(arguments)
}

// Invoke the "logArguments()" with some arguments:
logArguments('One', 'Two')
// Output:
// ReferenceError: arguments is not defined


// Create arrow function inside a regular function:
function parentFunction() {
  const logArguments = () => {
    // Try to log "argument" object:
    console.log(arguments)
  }

  // Invoke "logArguments()":
  logArguments()
}

// Invoke the "logArguments()":
parentFunction('One', 'Two')
// Output:
// {
//   '0': 'One',
//   '1': 'Two',
//   length: 2,
//   callee: ƒ parentFunction(),
//   __proto__: { ... }
// }
```

## Function Constructors

One way to use regular functions is to create constructor functions. Think about function constructor as blueprints for creating objects. Function constructor is still a regular function. However, there are some differences. First, you start its name with a capital letter.

When you want to use it, you call it with `new` keyword. This keyword comes before the constructor name and parentheses. Inside the constructor, you can use `this` to create and assign properties. These properties will be created for every instance you create with that constructor function.

```JavaScript
// Create function constructor "Human":
function Human(name, age) {
  // Create and assign new properties:
  this.name = name
  this.age = age

  // Add constructor method:
  this.sayHello = () => `Hi, my name is ${this.name}.`
}

// Create new instance of "Human":
const joe = new Human('Joel', 33)

// Check if "joe" is instance of "Human":
console.log(joe instanceof Human)
// Output:
// true

// Call the "sayHello()" method on "joe" instance:
joe.sayHello()
// Output:
// 'Hi, my name is Joel.'
```

Constructors with arrow functions? This doesn't work, literally. Arrow function doesn't have its own this. `this` is one thing you will encounter often in constructor functions. For this reason, and maybe some other as well, you can't use arrow function to create constructors. If you try it, JavaScript will throw `TypeError`.

```JavaScript
// Try to create function constructor with arrow function:
const Human = (name, age) => {
  this.name = name
  this.age = age
}

// Try to create new instance of "Human":
const jess = new Human('Jessica', 28)
// Output:
// TypeError: Human is not a constructor
```

## Conclusion: 4 main differences between regular and arrow functions

When it comes to arrow and regular functions, the differences go beyond the syntax. I hope that the four main differences we discussed helped you understand how arrow and regular functions differ from each other and when is it better to use one and when the other.

[regular functions]: https://blog.alexdevero.com/javascript-functions-pt1/
[arrow functions]: https://blog.alexdevero.com/javascript-arrow-functions/
[function declaration]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function
[function expression]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function
[function constructor]: https://blog.alexdevero.com/javascript-constructor-functions/
[apply()]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply
[call()]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call
