## Build your own Covid 19 tracker using C

Welcome guys, in this module we are going to talk about [How to build your own Covid 19 tracker using the C](https://usemynotes.com/build-your-own-covid-19-tracker-using-c/). I understand, you all must be wondering how we can build this using the C language. So, let’s start reading this module, and build the same using C.

## Build your own Covid 19 tracker using C

Covid-19 tracker is the way to track whether the person or user is infected from the covid-19 virus or not based on certain symptoms.

Some of the common symptoms of covid-19 are:

- Fever
- Headache
- Body Pain
- Diarrhea
- Cough and Cold
- Breathing Issues
- Loss of Taste and Smell

And suffering from any disease prior like diabetes, Hypertension, Blood Pressure, etc.
Based on these symptoms the covid-19 tracker will give the result and advice to the user or patient. Let’s see the step-to-step wise implementation of the [C language](https://usemynotes.com/c-programming/) model and then the complete code.

## Step 1: Importing the Header Files

This is the very first step, in which we have to import the necessary header files to write the program.

```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// string.h for using various string functions such as strcmp(), strcpy(), etc.
// stdlib.h for memory management in the program.
```

## Step 2: Creating Global variables

Global variables are the variables that can be accessed anywhere throughout the program. So, these are the list of variables that are declared globally in the program.

```
char n[10], feverDetails[10], coughDetails[10], BodyDetails[10], diaDetails[10], breathingDetails[10], tasteDetails[10], disease[10] ;
```
## Step 3: Creating the function to detect the covid.

The aim of this function is to detect the covid based on certain parameters that have been entered by the user.

```
int detectCovid(){
    if (strcmp(disease,"yes") == 0){
        printf("Please do stay at home with more precautions\n");
    }
    else if (strcmp(feverDetails,"yes") == 0 || strcmp(coughDetails,"yes") == 0 || strcmp(BodyDetails,"yes") == 0 || strcmp(diaDetails,"yes") == 0 || strcmp(breathingDetails,"yes") == 0 || strcmp(tasteDetails,"yes") == 0){
        printf("You are not safe, get yourself tested and take proper precautions\n");
    }
    else {
        printf("You are safe\n");
    }
}
```

## Step 4: Creating int main() function, the main part of the code.

In the main part of the program, the compiler starts executing from diarrhea inside the main function and keeps on executing until the main function’s last line.

```
int main(){
    char a[20];
    printf("Welcome to covid-19 tracker");
    printf("\nDo you have any symptoms?\n1) Cough\n2) Cold\n3) Body Ache\n4) fever\n5) Diarrhea\n6) Breathing Issues\n7) Sore throat]\n8) Loss of taste and smell\n9) Any disease like Diabetes, Blood Pressure, Hypertension, etc");
    printf("\nPress yes if you have any of these: ");
 
    scanf("%s",n);
    // strcmp(a,b) used to compare two strings a and b.
    if(strcmp(n , "yes") == 0){
        printf("Do you have a fever? Enter yes or no\n");
        scanf("%s ", feverDetails);
        // strcpy(a,b) used to copy the string b to string a
        strcpy(a, "fever");
    }
    if(strcmp(a , "fever") == 0){
        printf("Do you have a cough and cold? Enter yes or no\n");
        scanf("%s ”, coughDetails);
        strcpy(a, "cough");
    }
    if(strcmp(a , "cough") == 0){
        printf("Do you have Body Ache? Enter yes or no\n");
        scanf("%s ", BodyDetails);
        strcpy(a, "body");
    }
    if(strcmp(a , "body") == 0){
        printf("Are you suffering from Diarrhea? Enter yes or no\n");
        scanf("%s ", diaDetails);
        strcpy(a, "Diarrhea");
    }
    if(strcmp(a , "Diarrhea") == 0){
        printf("Do you have Breathing Issues? Enter yes or no\n");
        scanf("%s ", breathingDetails);
        strcpy(a, "Breathing");
    }
    if(strcmp(a , "Breathing") == 0){
        printf("Are you getting taste and smell? Enter yes or no\n");
        scanf("%s ", tasteDetails);
        strcpy(a, "taste");
    }
    if(strcmp(a, "taste") == 0){
        printf("Are you suffering from any disease already? Enter yes or no\n");
        scanf("%s ", disease);
        strcpy(a, "disease");
    }
    if(strcmp(a , "disease") == 0){
        detectCovid();
    }
    else{
        printf("Thanks for using !!\n");
    }
    return 0;
}
```

### Final Output

```
Welcome to covid-19 tracker
Do you have any symptoms?
1) Cough
2) Cold
3) Body Ache
4) fever
5) Diarrhea
6) Breathing Issues
7) Sore throat
8) Loss of taste and smell
9) Any disease like Diabetes, Blood Pressure, Hypertension,
Press yes if you have any of these: yes
Do you have a fever? Enter yes or no
no
Do you have a cough and cold? Enter yes or no
no
Do you have Body Ache? Enter yes or no
yes
Are you suffering from diarrhea? Enter yes or no
no
Do you have Breathing Issues? Enter yes or no
no
Are you getting taste and smell? Enter yes or no
Yes
Are you suffering from any disease already? Enter yes or no
no
You are not safe, get yourself tested and take proper precautions
```

I hope you all find this amazing and exciting. You all must also be amazed that this program has been constructed using the C language. So, congratulations to all of you for constructing or building your own Covid-19 tracker. For such amazing articles, stay connected with us, until then Keep reading, and Happy Coding.