## How to write my first Java Program

n this tutorial, we will start by writing our <a href="https://usemynotes.com/a-simple-java-program/">A simple Java program</a>. It will cover the very basic structure of a program and also the rules that are followed to write a successful Java program. We will be using a console/terminal to compile our program, run and display the output of our program.

Let’s write our first simple Java program that prints “Hello world !” message in the console. At first, open your favorite text editor. Some of the freely available text editors are Notepad++, Atom, and Visual Studio Code which you can use for this tutorial.

<h2>Create a new hello.text file & type the following program.</h2>

class FirstProgram{
public static void main(String args[]){
System.out.println("Hello World !");
}}

<b>The above program is composed of two components:</b>
<table>
<ul>
<li>The class block</li>
<li>The main function</li>
</ul>
</table>
<table>
<ul>
<li>The class block is kind of a wrapper block that contains all the code of a class.</li>
A class basically contains all code that relates to each other. For now, our class is named as FirstProgram.
<li>The class block has a main() function that is the starting point of the program. (Ignore other keywords as they will be covered later)</li>
<li>The statement System.out.println(“Hello World !”); prints the actual message in the console. Feel free to change the message between double-quotations to anything you want to print in the console.</li>
</ul>
</table>

Save the following program in your preferred directory and name it FirstProgram.java

Once saved, open cmd prompt and go to the directory where you have saved the program

Type the following line and press Enter: javac FirstProgram.java

The above line will use the java compiler to compile the Java program. It will fail to compile if there is an error in the program. If there are 0 errors, then it will generate FirstProgram.class file in the same directory.

After a successful compilation of the program, Type the following line and press Enter. java FirstProgram

This actually executes the Java program and print the output on the next line.

Congratulations! you have successfully written and executed your first Java program.
<h2>Note:</h2>
<table>
<ol>
<li>We have named our class as the first program, you can name it anything you want. Make sure you give it a valid name as per the name rules.</li>
<li>By convention, a class name starts with a capital case and subsequent internal words are started with capital letters too. Example: CalculatorProgram, MyJavaProgram, HelloWorldProgram, etc.</li>
<li>We cannot use a special character in the class name such as !,*,^,%, etc. Only underscore (_) is allowed.</li>
<li>The first character of a class name should always be an underscore or an alphabet. The class name should not start with a number or other special characters.</li>
<li>For this tutorial, we have saved the file with the name FirstProgram.java which is exactly the same as the class name which makes it easy to remember for compiling and executing.</li>
<li>When we compile the program with the javac command, it generates compiled .class files for that program.</li>
<li>For example, if you have a file MyProgram.java which has a class with the name Calculator, then you will compile the program as javac MyProgram.java</li>
<li>To execute the program, you will type: java Calculator</li>
<li>The words public, static, void, class are keywords that should be in small-casing.</li>
<li>The words String and System are pre-defined classes.</li>
</ol>
</table>