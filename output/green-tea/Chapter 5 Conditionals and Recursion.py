# j2 from 'macros.j2' import header
# {{ header("Conditionals and recursion", "Conditionals and recursion") }}

# %% [markdown] lang="en" tags=["slide"]
# # Chapter 5  Conditionals and recursion
# - The core focus in this chapter will be on the `if` statement.
# - This program control structure allows for conditional execution of code depending on the state of the program.
# - Before diving in, we'll introduce two important operators: floor division and modulus.

# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to Floor Division and Modulus Operators
# - Python has special operators to perform different types of operations.
# - Two such operators are:
#   - Floor Division (`//`): This operator returns the largest possible integer after division.
#   - Modulus (`%`): This operator returns the remainder of the division.

# %%
# Example of Floor Division
print("Floor Division Example: ")
print(10 // 3) # Will output 3

# %%
# Example of Modulus
print("Modulus Operator Example: ")
print(10 % 3)  # Will output 1

# %% [markdown] lang="en" tags=["slide"]
# ## 5.1  Floor Division and Modulus
# - The floor division operator, '//', divides two numbers and rounds down to an integer.
# - Following example illustrates how you can calculate integer hours from movie run time in minutes using floor division. 

# %%
# Traditional division returns a floating-point number
minutes = 105
minutes / 60

# %% [markdown] lang="en" tags=["slide"]
# - For scenarios where we need results in integer form, like hours from minutes, we can use floor division. It returns the integer by rounding down.

# %%
# Floor division returns the integer number of hours, rounding down
minutes = 105
hours = minutes // 60
hours

# %% [markdown] lang="en" tags=["slide"]
# - To get the remaining minutes after calculating hours, you can subtract the hours in minutes from total minutes.
# - An alternative is to use the modulus operator which returns the remainder after division. 

# %%
# Getting the remainder with subtraction
remainder = minutes - hours * 60
remainder

# %%
# Getting the remainder using modulus operator
remainder = minutes % 60
remainder

# %% [markdown] lang="en" tags=["slide"]
# - The modulus operator is more handy than it seems. For example, it can be used to check if a number is divisible by another number or to extract the right-most digit(s) from a number.
# - However, take note that in Python 2, the standard division operator performs floor division if both operands are integers and floating-point division if any operand is a float.
# %% [markdown] lang="en" tags=["slide"]
# ## 5.2 Boolean Expressions
# - Boolean expressions are expressions that can be either true or false.
# - In Python, we use relational operators to create boolean expressions.
# - Examples of relational operators are `==`, `!=`, `>`, `<`, `>=`, and `<=`.
# - `==` is for comparison, while `=` is for assignment.

# %% 
# Comparing two operands using ==
print(5 == 5)  # This will return True
print(5 == 6)  # This will return False

# %% [markdown] lang="en" tags=["slide"]
# ## Data Types in Boolean Expressions
# - `True` and `False` are special values belonging to the `bool` type in Python.
# - It's crucial to remember that they are not strings.

# %% 
# Checking the type of True and False
print(type(True))   # This will return <class 'bool'>
print(type(False))  # This will return <class 'bool'>

# %% [markdown] lang="en" tags=["slide"]
# ## Relational Operators in Python
# - Other examples of relational operators include `!=` for inequality, `>` for greater than, `<` for less than, `>=` for greater than or equal to, and `<=` for less than or equal to.
# - Unlike mathematical symbols, Python uses unique symbols for its relational operators. For instance, '=' is for assignment, while '==' is for equality checking.
# - Note that Python syntax does not support the use of `=<` or `=>`.

# %% 
# Demonstrating the use of other relational operators
x = 10
y = 20
print(x != y)  # This will return True, because x is not equal to y
print(x > y)   # This will return False, because x is not greater than y
print(x < y)   # This will return True, because x is less than y
print(x >= y)  # This will return False, because x is not greater than or equal to y
print(x <= y)  # This will return True, because x is less than or equal to y
# %% [markdown] lang="en" tags=["slide"]
# ## 5.3  Logical operators
# - Python has three logical operators: `and`, `or`, and `not`. 
# - The operator `and` results in `True` only if both the statements are true. For example, `x > 0 and x < 10`.
# - The `or` operator results in `True` if either or both of the conditions is true, e.g. `n%2 == 0 or n%3 == 0`.
# - The `not` operator negates a boolean expression. For example `not (x > y)` is true if `x > y` is false.
# - In Python, any nonzero number is interpreted as `True`. But there are caveats with this flexibility so it's advised to use it cautiously.

# %% 
42 and True
# %% [markdown] lang="en" tags=["slide"]
# ## 5.4 Conditional Execution
# - Writing useful programs encompasses our ability to check conditions and alter program behavior accordingly. This is achieved through conditional statements.
# - In Python, the simplest form of a conditional statement is the `if` statement.
# - The `if` statement evaluates a boolean expression (called a condition), if the condition returns `True`, the indented code block under the `if` statement is executed.
# - Conditional statements similar to function definitions consist of a header followed by an indented body. 

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding `if` Statement
# - An if statement can have multiple lines of code in its body, however, at least one line is necessary.
# - There are instances where we may need a placeholder for our `if` statement body. This placeholder may be to reserve space for future code that hasn't been written. In such cases, the `pass` statement is utilized which does nothing.

# %%
# Example of if statement
x = 10
if x > 0:
    print('x is positive')

# %%
# Example of if statement with pass keyword
x = -10
if x < 0:
    pass          # TODO: need to handle negative values!
# %% [markdown] lang="en" tags=["slide"]
# ## 5.5 Alternative execution
# - In Python, a variation of `if` statement is "alternative execution", where two outcomes are possible and the condition determines which one is executed.
# - This form of flow control follows the following syntax i.e., 
# - An `else` clause is added to the `if` statement, and the block of code under `else` gets executed when the condition in the `if` statement is not satisfied.
# - This leads to two branches in the flow of execution, as exactly one of the alternatives (or outcomes) will execute based on the condition.

# %% 
# Example of alternative execution
x = 7
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

# Alternative will execute based on whether x is even or odd. If x is an even number, 'x is even' is printed. Else, 'x is odd' is printed. 
# The output will be 'x is odd'.

# %% [markdown] lang="en" tags=["slide"]
# ## 5.6 Chained Conditionals
# - Chained conditionals come into play when there are more than two possibilities,
#   hence needing more than two branches for decision-making.
# - In chained conditionals, "elif" is used as an abbreviation of "else if".
# - Only one branch in the chain will run, even though there are no limits on the number of "elif" statements.
# - If an "else" clause exists, it must be at the end, but it's not mandatory to have one.

# %% 
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

# %% [markdown] lang="en" tags=["slide"]
# - Each condition in the chain is checked in order. If the first condition proves false,
#   the next one is checked and this pattern is followed until a true condition is found.
# - Once a true condition is discovered, the corresponding branch runs and the
#   statement ends. If there is more than one true condition, only the first one executes.

# %%
if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()
# %% [markdown] lang="en" tags=["slide"]
# ## 5.7 Nested Conditionals
# - Conditionals can be nested within another.
# - For example, we can write an if-else statement inside another if-else statement.
# - The outer conditional could have many branches and each branch may contain its own `if` statement.
# - Every branch could be a simple or conditional statement.
# - Though the indentation makes the structure apparent, nested conditionals often become hard to read.
# - It is suggested to avoid them when it's not necessary.
# - Use of logical operators like "and", "or" etc. can help simplify the nested conditional statements.
# - Python also provides a concise way to express a condition with a chain of conditions for a single variable.

# %% 
# Example of a nested conditional
x,y = 10, 20
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# %% [markdown] lang="en" tags=["slide"]
# - For instance, we can rewrite a nested `if` condition to test the range of a number using the `and` operator. 
# - This simplifies the code for better readability.

# %%
# Nested 'if' statement
x = 5
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

# Using 'and' operator to simplify the nested 'if' statement
x = 5
if 0 < x and x < 10:
    print('x is a positive single-digit number.')

# %% [markdown] lang="en" tags=["slide"]
# - Python provides a more concise way to write chained conditions involving the same variable.
# - This is especially useful when checking for a number within a specific range.

# %% 
# More concise way to express the condition
x = 5
if 0 < x < 10:
    print('x is a positive single-digit number.')
# %% [markdown] lang="en" tags=["slide"]
# ## 5.8 Recursion
# - Functions can call other functions or even themselves. This is known as recursion.
# - A recursive function can be very powerful, allowing for complex operations to be written succinctly.

# %% [markdown] lang="en" tags=["slide"]
# - Let's consider a function named 'countdown'. This function takes an input `n`, and if `n` is less than or equal to 0, it prints 'Blastoff!'.
# - If `n` is greater than 0, it first prints `n` and then calls itself with an argument `n-1`.
# - The function continues to call itself, decrementing `n` by 1 each time, until `n` is less than or equal to 0. 

# %%
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
# %% [markdown] lang="en" tags=["slide"]
# - If we call the countdown function with an argument of 3, it will print the values 3, 2, 1, followed by 'Blastoff!'.
# - The recursive calls return in the reverse order they were called, resuming control back to the main program.

# %%
countdown(3)

# %% [markdown] lang="en" tags=["slide"]
# - Recursion is a function calling itself to solve a smaller instance of the problem.
# - Another example of recursion is the function 'print_n', which prints a given string `s` `n` times. 
# - This function checks if `n` is less than or equal to 0. If it is, the function ends. If `n` is greater than 0, it prints the string `s` and calls itself with `n-1`.

# %%
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
        
# %% [markdown] lang="en" tags=["slide"]
# - This process allows the function to print the string `s` `n` times.
# - While a `for` loop might be simpler for this specific example, recursion can be invaluable for more complex tasks. It's a powerful tool in your programming arsenal.
# - Recursion can solve problems that are difficult to solve using iteration. The key to understanding recursion is to realize that a function can be in multiple stages of execution at the same time.
# %% [markdown] lang="en" tags=["slide"]
# ## Stack Diagrams for Recursive Functions
# - Stack diagrams can help interpret the state of a program during a function call, including recursive functions.
# - Every time a function gets called, Python creates a frame to contain the function’s local variables and parameters.
# - For a recursive function, there might be more than one frame on the stack at the same time. 

# %% [markdown] lang="en" tags=["slide"]
# ## Stack Diagrams for Recursive Functions (continued)
# - Stack diagrams visually represent recursion: the top of the stack is the frame for the `__main__` function, while the other frames represent recursive calls.
# - Each recursive call frame has its own local variables and parameters.
# - The bottom of the stack, where recursion ends, is called the "base case". 

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise: Stack Diagrams for Recursive Functions
# - Draw a stack diagram for a function `print_n` called with `s = 'Hello'` and `n=2`.
# - Write a function `do_n` that takes a function object and a number `n` as arguments, and that calls the given function `n` times.

# %% [markdown] lang="en"] # Put this in a markdown cell to state the objective of the following code cell
# Let's start with the definition of the function `print_n` which prints a string 's' n number of times.

# %% 
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Hello', 2)

# %%
# Now let's proceed to create the function `do_n` which takes a function and a number 'n' as arguments and calls the given function 'n' times.

def do_n(func, n):
    if n <= 0:
        return
    func()
    do_n(func, n-1)

# Now we can test our function
do_n(lambda: print('Repeated Function Call'), 3)
# %% [markdown] lang="en" tags=["slide"]
# ## 5.10 Infinite recursion
# - What is infinite recursion?
#   - If a recursion never reaches a base case, it goes on making recursive calls infinitely - this is infinite recursion.
#   - It's generally an unfavorable scenario when programming.
# - There's usually a limit to the recursion depth; when surpassed, Python reports an error message. 

# %% [markdown] lang="en" tags=["slide"]
# - Here's an example of a program with an infinite recursion:

# %%
def recurse():
    recurse()

# %% [markdown] lang="en" tags=["slide"]
# - When the maximum recursion depth is reached, Python reports an error message like this:

# %%
'''
  File "<stdin>", line 2, in recurse
  File "<stdin>", line 2, in recurse
  File "<stdin>", line 2, in recurse
                  .   
                  .
                  .
  File "<stdin>", line 2, in recurse
RuntimeError: Maximum recursion depth exceeded
'''

# %% [markdown] lang="en" tags=["slide"]
# - When an error occurs due to infinite recursion, there are 1000 recurse frames on the stack.
# - If you encounter an infinite recursion by accident:
#   - Review your function to ensure that there is a base case that does not make a recursion.
#   - Ensure you are guaranteed to reach the base case.
# %% [markdown] lang="en" tags=["slide"]
# ## 5.11 Keyboard input
# - Python's built-in `input` function allows for user input during program execution. 
# - When `input` is called, the program waits for the user to type something and resumes execution when the user hits "Return" or "Enter". 
# - The input provided by the user is returned as a string. 
# - In Python 2, this function is called as `raw_input`.

# %%
text = input()
print(text)

# %% [markdown] lang="en" tags=["slide"]
# - For better interaction with the user, it's a good idea to print a prompt before getting input, which can be passed as an argument to `input`.
# - The sequence '\n' at the end of the prompt represents a newline, which is a special character that causes a line break. 
# - If needed, the return value of `input` can be converted to integer using the `int` function.

# %%
name = input('What...is your name?\n')
print(name)

# %%
prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
print(int(speed))

# %% [markdown] lang="en" tags=["slide"]
# - Be careful while converting user input to integer as any non-numeric input will raise an error. 
# - In the future, we will discuss how to handle such errors. 

# %%
speed = input(prompt)
print(int(speed))  # This will raise an error if the input is not a string of digits.
# %% [markdown] lang="en" tags=["slide"]
# ## 5.12 Debugging
# - Error messages contain helpful information to identify problems in codes, including kind of error and its location
# - Usually, syntax errors are easy to find. However, errors involving whitespaces (tabs and spaces) can be challenging to trace since they are invisible, and we often ignore them
# - Error messages basically point to the code line where an issue occurred, not necessarily the location of actual errors. Errors could have happened earlier but only got detected later

# %% [markdown] lang="en" tags=["slide"]
# # Debugging continued...
# - The above explanation is also true for runtime errors
# - Let's look at an example related to computation of a signal-to-noise ratio in decibels (SNRdb= 10 log10(Psignal/Pnoise))
# - Errors may appear on a different line that what the error message indicates
# - Debugging requires meticulous checking. Though read error messages carefully, but don't assume every detail they provide is correct

# %%
>>> x = 5
>>> y = 6
#Above code will raise an IndentationError: unexpected indent error, because the second line is indented by one space. 

# %%
# Now let's see an example code for computation of a signal-to-noise ratio in decibels
import math
signal_power = 9
noise_power = 10
ratio = signal_power // noise_power

# %%
# Continue from previous cell
decibels = 10 * math.log10(ratio)
print(decibels)
#The above code will raise a ValueError: math domain error, because line 4 uses floor division instead of floating-point division which leads to ratio being 0 and log10 can't take 0 as an argument. You should fix such errors by closely inspecting all lines of your code, not just the line mentioned in the error message.
# %% [markdown] lang="en" tags=["slide"]
# ## 5.13 Glossary
## Floor Division
- An operator, denoted //, that divides two numbers and rounds down (toward negative infinity) to an integer.

## Modulus Operator
- An operator, denoted with a percent sign (%), that works on integers and returns the remainder when one number is divided by another.

# %% [markdown] lang="en" tags=["slide"]
## Boolean Expression
- An expression whose value is either True or False.

## Relational Operator
- One of the operators that compares its operands, i.e., ==, !=, >, <, >=, and <=.

## Logical Operator
- One of the operators that combines boolean expressions like: 'and', 'or', and 'not'.

# %% [markdown] lang="en" tags=["slide"]
## Conditional Statement
- A statement that controls the flow of execution depending on some condition.

## Condition
- The boolean expression in a conditional statement that determines which branch runs.

## Compound Statement
- A statement that consists of a header and a body. The header ends with a colon (:). The body is indented relative to the header.

# %% [markdown] lang="en" tags=["slide"]
## Branch 
- One of the alternative sequences of statements in a conditional statement.

## Chained Conditional
- A conditional statement with a series of alternative branches.

## Nested Conditional
- A conditional statement that appears in one of the branches of another conditional statement.

# %% [markdown] lang="en" tags=["slide"]
## Return Statement
- A statement that causes a function to end immediately and return to the caller.

## Recursion
- The process of calling the function that is currently executing.

## Base Case
- A conditional branch in a recursive function that does not make a recursive call.

# %% [markdown] lang="en" tags=["slide"]
## Infinite Recursion
- A recursion that doesn’t have a base case, or never reaches it. This causes a runtime error eventually.
# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 1 : Time Calculation and Conversion
# - Python's `time` module includes a function `time` that returns the current Greenwich Mean Time in the epoch.
# - The epoch is a reference point in time, which on UNIX systems corresponds to 1 January 1970.
# - The aim of this exercise is to write a script that reads the current time and converts it into a time of day (in hours, minutes, and seconds) and calculates the number of days since the epoch.

# %%
import time 
print(time.time())
# Output: 1437746094.5735958

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 2: Checking Fermat's Last Theorem
# - Fermat's Last Theorem states that there are no three positive integers (a, b, c) such that a^n + b^n = c^n for any values of n greater than 2.
# - The exercise entails writing a function `check_fermat` that takes four parameters (a, b, c, and n) and checks if Fermat's theorem holds.
# - If n is greater than 2 and a^n + b^n = c^n, then the program should print, "Holy smokes, Fermat was wrong!". Otherwise, it should print, "No, that doesn’t work."
# - Another function should be created to prompt the user to input values for a, b, c, and n (converting them to integers), and then use `check_fermat` to test whether they violate Fermat’s theorem.

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 3: Triangle Formation
# - Three sticks can be arranged to form a triangle unless one of the sticks is longer than the sum of the other two. 
# - If one stick is longer, it's not possible to arrange them into a triangle while if their sum equals one of the sticks, they form a degenerate triangle.
# - The task is to write a function `is_triangle` which accepts three integers (representing the stick lengths) and prints "Yes" if a triangle can be formed or "No" if it can't.
# - Additionally, write another function to prompt the user to input three stick lengths, convert them to integers, and more importantly, use `is_triangle` to verify if the lengths provided can form a triangle.

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 4: Understanding Recursion
# - Understand the output of the following recursive program and what would happen if it was invoked like this: `recurse(-1, 0)?`.
# - Diagram the state of the program when it's being executed.
# - Write a docstring that comprehensively explains everything someone would need to know to use this function.

# %%
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 5: Analysis and function understanding
# - Interpret the function below (& see the examples in Chapter 4) before executing it to verify if the interpretation was correct.

# %%
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 6: Drawing a Koch Curve
# - A Koch curve is a fractal, and to draw a Koch curve with length x, the following steps are used:
#   1. Draw a Koch curve with length x/3.
#   2. Turn left 60 degrees.
#   3. Draw a Koch curve with length x/3.
#   4. Turn right 120 degrees.
#   5. Draw a Koch curve with length x/3.
#   6. Turn left 60 degrees.
#   7. Draw a Koch curve with length x/3.
# - However, if x is less than 3, a straight line with length x should be drawn.
# - Write a function `koch` that takes a turtle and a length as parameters and uses the turtle to draw a Koch curve with the given length.
# - Write a function `snowflake` that draws three Koch curves to make the outline of a snowflake.
# - The Koch curve can be generalized in multiple ways. Consider implementing a favorite one as provided in the Wikipedia link.
