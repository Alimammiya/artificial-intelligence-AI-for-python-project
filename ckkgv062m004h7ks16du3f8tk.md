## Variables in Java Programming

In this tutorial, we will study what is <a href="https://usemynotes.com/variables-and-constants-in-java/">variables in java</a> and what's are the type of variables in java programming. So let's go into the deep model. 

<h2>What is variable</h2>

A variable is a storage area where we store the data and the information. A variable is a holder that holds the value while the java program is executed. Variable also declare with a data type. When we declare a variable name the first letter of the variable should not be a digit. And the variable name should not be a keyword.

String name;
int number;

Here string is a data type and name is a variable of this data type.
<h2>Types of variable:-</h2>

<h3>Local Variable</h3>

A local variable always declares inside the body of the method and function. A local variable can be a static variable. The local variable should be initialized before accessing them.

Class Test
{
  public void sum()
  {
   int a, b=30, c=20; // declaring local variable a, b, c
   a = b + c;
   System.out.println(“Sum=”+a);
   }
  public static void main(String[] args)
 {
  Test obj= new Test();    // creating object
  Obj.sum();    // calling object
 }
}

<b>Output</b>
Sum = 50
<h3>Instance Variable</h3>
A variable that is declared inside a class but outside the body, method, constructor or block, is called an instance variable. Instance variable need not be initialized before using them as they are automatically initialized to their default values.

class Test
{
  int a, b=20, c=10;
  public void add()
  {
   a = b + c;
   System.out.println(“Sum=” +a );
  }
public void sub()
{
  a= b-c;
  System.out.println(“Sub=”+a);
}
 public static void main(String[] args)
 {
   Test obj= new Test();
    obj.add( );
    obj.sub( );
 }
}

<b>Output</b>

Sum =30
Sum=10
<h3>Static Variable</h3>

A variable that is declared with the static keyword, the Static variable is stored in the static memory. A static variable is regular to every one of the occasions (or objects) of the class since it is a class-level variable. you can say that only a single copy of the static variable is created and shared among all the instances of the class. Memory designation for such factors possibly happens once when the class is loaded in the memory.

<h3>Static variable Syntax</h3>

static keyword followed by data type and variable name

static data_type variable_name;

<h3>Static variable example in Java</h3>

class VariableDemo
{
  static int count=0;
  public void increment()
  {
    count++;
  }
public static void main(String args[])
 {
  VariableDemo obj1=new VariableDemo();
  VariableDemo obj2=new VariableDemo();
  obj1.increment();
  obj2.increment();
  ystem.out.println("Obj1: count is="+obj1.count);
  System.out.println("Obj2: count is="+obj2.count);
 }
}

<b>Output</b>

Obj1: count is=2
Obj2: count is=2
As should be obvious in the above model that both the items are having a similar duplicate of static variable that is the reason, they shown a similar estimation of check.