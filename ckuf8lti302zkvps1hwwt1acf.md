## Python Operators

In this module tutorial, we will learn [Python Operators](https://usemynotes.com/python-operators/). It’s a basic idea of Python that's needed for understanding the workflow of a Python program.

## Python Operators

Operators commonly are used to performing operations on both values and variables in Python. These are standard symbols used for the aim of logical and arithmetic operations. In this post, we will look into various types of Python operators.

- Arithmetic operators
- Relational operators
- Logical operators
- Bitwise operators
- Assignment operators
- Membership Operators
 
### Arithmetic operators
These operators are used to performing mathematical functions such as addition, multiplication, division, subtraction and much more.

<table>
<tbody>
<tr>
<td>Operator</td>
<td>Description</td>
<td>Syntax</td>
</tr>
<tr>
<td>+</td>
<td>Addition: It  adds two operands</td>
<td>x + y</td>
</tr>
<tr>
<td>-</td>
<td>Subtraction:  It  subtracts two operands</td>
<td>x - y</td>
</tr>
<tr>
<td>*</td>
<td>Multiplication: It  multiplies two operands</td>
<td>x * y</td>
</tr>
<tr>
<td>/</td>
<td>Division (float): It  divides the first operand by the second</td>
<td>x / y</td>
</tr>
<tr>
<td>//</td>
<td>Division (floor): It  divides the first operand by the second</td>
<td>x // y</td>
</tr>
<tr>
<td>%</td>
<td>Modulus: It returns the remainder when the first operand is divided by the second</td>
<td>x % y</td>
</tr>
<tr>
<td>**</td>
<td>Power: It  Returns first raised to power second</td>
<td>x ** y</td>
</tr>
</tbody>
</table>

```
# Examples of Arithmetic Operator 
a = 90
b = 40  
# Addition of numbers 
add = a + b 
# Subtraction of numbers 
sub = a - b 
# Multiplication of number 
mul = a * b   
# Division(float) of number 
div1 = a / b 
# Division(floor) of number 
div2 = a // b  
# Modulo of both number 
mod = a % b 
# Power
p = a ** b
# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod)
print(p)

Output:
130
50
3600
2.25
2
1
1.4780E + 78
```

### Relational Operators: 
A relational operator compares the values. It either returns True or False based on the conditions.

<table>
<tbody>
<tr>
<td>Operator</td>
<td>Description</td>
<td>Syntax</td>
</tr>
<tr>
<td>> </td>
<td>Greater than: It  gives True if the left operand is greater than the right</td>
<td>x > y</td>
</tr>
<tr>
<td>< </td>
<td>Less than: It  gives True if the left operand is less than the right</td>
<td>x < y</td>
</tr>
<tr>
<td>==</td>
<td>Equal to: It  gives True if both operands are equal</td>
<td>x == y</td>
</tr>
<tr>
<td>!=</td>
<td>Not equal to: It  gives True if operands are not equal</td>
<td>x != y</td>
</tr>
<tr>
<td>>=</td>
<td>Greater than or equal to :  It  gives True if the left operand is greater than or equal to the right</td>
<td>x >= y</td>
</tr>
<tr>
<td><=</td>
<td>Less than or equal to :  It  gives  True if the left operand is less than or equal to the right</td>
<td>x <= y</td>
</tr>
</tbody>
</table>

```
# Examples of Relational Operators
a = 1
b = 3
# a > b is False
print(a > b)
# a < b is True
print(a < b)
# a == b is False
print(a == b)
# a != b is True
print(a != b)
# a >= b is False
print(a >= b)
# a <= b is True
print(a <= b)

Output:
False
True
False
True
False
True
```
### Logical operators:
Logical operators perform Logical AND, Logical OR and Logical NOT operations.

<table>
<tbody>
<tr>
<td>Operator</td>
<td>Description</td>
<td>Syntax</td>
</tr>
<tr>
<td>And</td>
<td>Logical AND: It  gives True if both the operands are true</td>
<td>x and y</td>
</tr>
<tr>
<td>Or</td>
<td>Logical OR: It  gives True if either of the operands is true</td>
<td>x or y</td>
</tr>
<tr>
<td>Not</td>
<td>Logical NOT: It  gives True if the operand is false</td>
<td>not x</td>
</tr>
</tbody>
</table>

```
# Examples of Logical Operator
a = True
b = False  
# Print a and b is False
print(a and b)
# Print a or b is True
print(a or b)
# Print, not a is False
print(not a)

Output:
False
True
False
```

### Bitwise operators: 
Bitwise operators act on bits and perform bit by bit operations.

<table>
<tbody>
<tr>
<td>Operator</td>
<td>Description</td>
<td>Syntax</td>
</tr>
<tr>
<td>&</td>
<td>Bitwise AND</td>
<td>x & y</td>
</tr>
<tr>
<td>|</td>
<td>Bitwise OR</td>
<td>x | y</td>
</tr>
<tr>
<td>~</td>
<td>Bitwise NOT</td>
<td>~x</td>
</tr>
<tr>
<td>^</td>
<td>Bitwise XOR</td>
<td>x ^ y</td>
</tr>
<tr>
<td>>> </td>
<td>Bitwise right shift</td>
<td>x>></td>
</tr>
<tr>
<td><<  </td>
<td>Bitwise left shift</td>
<td>x<<</td>
</tr>
</tbody>
</table>

```
# Examples of Bitwise operators
a = 10
b = 4
# Print bitwise AND operation  
print(a & b)
# Print bitwise OR operation
print(a | b)
# Print bitwise NOT operation 
print(~a)
# print bitwise XOR operation 
print(a ^ b)
# print bitwise right shift operation 
print(a >> 2)
# print bitwise left shift operation 
print(a << 2)

Output:
0
14
-11
14
2
40
```

### Assignment operators:
Assignment operators are used to assigning values to the variables.
<table>
<tbody>
<tr>
<td>Operator</td>
<td>Description</td>
<td>Syntax</td>
</tr>
<tr>
<td>=</td>
<td>Assign the value of the right side of expression to the left side operand</td>
<td>x = y + z</td>
</tr>
<tr>
<td>+=</td>
<td>Add AND: Add right-side operand with left side operand and then assign to left operand</td>
<td>a+=b  a=a+b</td>
</tr>
<tr>
<td>-=</td>
<td>Subtract AND: Subtract right operand from left operand and then assign to left operand</td>
<td>a-=b  a=a-b</td>
</tr>
<tr>
<td>*=</td>
<td>Multiply AND: Multiply right operand with left operand and then assign to left operand</td>
<td>a*=b  a=a*b</td>
</tr>
<tr>
<td>/=</td>
<td>Divide AND: Divide left operand with right operand and then assign to left operand</td>
<td>a/=b  a=a/b</td>
</tr>
<tr>
<td>%=</td>
<td>Modulus AND: Takes modulus using left and right operands and assign the result to left operand</td>
<td>a%=b  a=a%b</td>
</tr>
<tr>
<td>//=</td>
<td>Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand</td>
<td>a//=b  a=a//b</td>
</tr>
<tr>
<td>**=</td>
<td>Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand</td>
<td>a**=b  a=a**b</td>
</tr>
<tr>
<td>&=</td>
<td>Performs Bitwise AND on operands and assign value to left operand</td>
<td>a&=b  a=a&b</td>
</tr>
<tr>
<td>|=</td>
<td>Performs Bitwise OR on operands and assign value to left operand</td>
<td>a|=b   a=a|b</td>
</tr>
<tr>
<td>^=</td>
<td>Performs Bitwise XOR on operands and assign value to left operand</td>
<td>a^=b  a=a^b</td>
</tr>
<tr>
<td>>>=</td>
<td>Performs Bitwise right shift on operands and assign value to left operand</td>
<td>a>>=b   a=a>>b</td>
</tr>
<tr>
<td><<=</td>
<td>Performs Bitwise left shift on operands and assign value to left operand</td>
<td>a <<= b   a= a << b</td>
</tr>
</tbody>
</table>

#### Learn full tutorial-
[Python Operators](https://usemynotes.com/python-operators/)

I hope this module can be useful for you to understand Operators in Python. You should try to use all the Operators and functionality to get a better understanding. Stay in touch with us to find out more modules that are taught like this. Keep rehearsing it!
