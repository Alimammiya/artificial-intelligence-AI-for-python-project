## String in C Programming

In this tutorial, we will study what is a [string in c programming](https://usemynotes.com/what-is-a-string-in-c-programming/), what was the type of declaring and initializing method of string, and the get() and puts() function with the help of examples. So let’s go start.

## String in C Programming
There is no data type available to create strings in C programming. If we have to create a string, then we have to create a char array, hence the character array in C language is also called a string. And the strings in it terminate with a null character ().

In C language we can declare and initialize with strings two types.

### First:-
In this, we create an array of finite numbers and store one-one character of a string in its all index. It stores the null character () in its last index. It is necessary to do this.
```
char myArray[4] = {‘A’, ‘ L’, ‘I’, ‘M’, ‘A’, ‘M’};
```

### Second:-
In this, we create one undefined char array and assign it one string and Array automatically becomes the same size as the string size. With this method, the null character () is automatically added to the initialization.
```
char myArray[] = “ALIMAM”;
```

### Example:-
```
#include<stdio.h>
int main()
{
  /* Declaring string in array format */
  char myArrayF[5] = {‘A’, ‘ L’, ‘I’, ‘M’, ‘A’, ‘M’};

  /* Declaring string in simple format */
  char myArrayS[] = “ALIMAM”;

  printf(“First Way: %sn”,myArrayF);
  printf(“Second Way: %s”, myArrayS);

return 0;
}
```

### Output
```
First Way: ALIMAM
Second Way: ALIMAM
```

## gets() and puts() Functions

### gets() function:-
The get () function is used to read from the string user at run time. This function is defined for this purpose. In this, we pass the name of the array in which we want to store the string.
```
gets(char_Array_Name);
```
On passing the string, it is stored in the char array. If the array is to be made a string point, the loop will have to be used.

### puts() function provide:-
The puts () function is used to print the Char array as a complete string.
```
puts(char_Array_Name);
```

### Example
```
#include<stdio.h>
#include <stdio.h>
int main()
{
char answer[50];
printf(“Who is the founder of Use My Notes?”);

/* Taking string input at run time using gets() function */
gets(answer);
printf(“\n Answer is : “);

/* Printing string to the screen using puts() function */
puts(answer);

return 0;
}
```
### Output:-
```
Who is the founder of Use My Notes?
Alimam Miya (input)
Answer is: Alimam Miya
```