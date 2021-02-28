## 5 Useful javascript tricks for beginners

In this post, I will show you 5 awesome javascript tricks which will make your life easier. And will help you to become a better developer. So if you are interested, continue reading.

## Trick-1: Remove duplicates from an Array!

This trick is pretty simple. Suppose I have an array which is containing numbers, strings, and booleans. And in this array, I want to make sure, that there's no duplicate item. So how do you do that?

```
const array = [1, 2, 3, 2, 1, true, true, false, 'Ratul', 1, 5];
const filtered__array = [...new Set(array)];
console.log(filtered__array) // [ 1, 2, 3, true, false, 'Ratul', 5 ]
```
Simple!

## Trick-2: Turn a Decimal Number into an integer.

This one is a pretty straightforward trick. Let me show you.

```
const number = 23.6565
console.log(number | 0);
```
Isn't it so simple!

## Trick-3: Getting the Last Value of an Array!

Suppose you have an array of something. Now if you want to have the last item of the array, how will you do that?

```
const array = [1, 2, 3, 4, 5]
const last_Item = array.slice(-1)
console.log(last_Item)
````

Here we go! Now if you put -2 instead of -1, you will get the last two values of the array and then if you give -3 instead of -2, you will get the value of the last three indexes and so on.
Trick-4: Get a random index value from an array.

Suppose we are doing a lottery program. We have an array which is containing the names of the participants. Now we want only one user randomly from the array to decide a winner.

````
const participants = ['Ratul', 'George', 'july', 'Padrik', 'G']
const winner = participants[Math.floor(Math.random() * participants.length)]
console.log(winner) // july was the winner 😊
````

## Trick-5: Detect the most lengthy word in an array

Create an array and add some different strings. Now print the most lengthy string of this array.

```
const array = ['Apple', 'Pine-apple', 'Banana', 'Jack-fruit']

let most_lengthy_string = ''
array.forEach((item) => {
  if (item.length > most_lengthy_string.length) {
    most_lengthy_string = item
  }
})
console.log(most_lengthy_string)
```

Simple! So let me explain to you what's going on here. Firstly we have an array which is containing some strings. And After that, I have created a variable which is containing an empty string. And now, to detect the most lengthy string in this array, I need to take a look at all of the array items So I have looped through the array. And if the array's item length is greater than the length of our "most_lengthy_string" we are reassigning the value of the variable and after all, I am just printing out the variable. That's all!

### Conclusion

Thanks for reading this article. Hope you enjoyed that. And make sure you follow me to receive all the informational posts just like that. :)

Originally posted on [ratuloss](https://dev.to/ratuloss/5-useful-javascript-tricks-4kp8) 

------
## learn for free
- [Java programming course for free](https://usemynotes.com/java-programming/) 
- [Python for Beginners Course](https://usemynotes.com/python/) 

---- 
Personally, I love Coffee. 
<a href="https://www.buymeacoffee.com/alimammiya" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>