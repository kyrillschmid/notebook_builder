# j2 from 'macros.j2' import header
# {{ header("Fruitful Functions", "Fruitful Functions") }}

# j2 from 'macros.j2' import header
# {{ header("Fruitful Functions", "Fruitful Functions") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Fruitful functions
# - Python functions, such as the math functions, often produce return values
# - The functions we have written so far are void and do not have a return value
# - This chapter focuses on writing fruitful functions that have a return value
# - Fruitful functions are those that perform a task and return a value, rather than just performing a task or action without returning a value
# %% [markdown] lang="en" tags=["slide"]
# ## Fruitful functions
# - Python functions, such as the math functions, often produce return values
# - The functions we have written so far are void and do not have a return value
# - This chapter focuses on writing fruitful functions that have a return value
# - Fruitful functions are those that perform a task and return a value, rather than just performing a task or action without returning a value

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions
# In this mini-workshop, we will work with fruit-themed functions that return values. We will also explore the concept of fruitful functions and practice creating and using them.

# %% [markdown] lang="en" tags=["subslide"]
#
# Define a function called `add_fruits` that takes two parameters `fruit1` and `fruit2` and returns a string containing both fruits separated by a space.
# For example, if `add_fruits("apple", "banana")` is called, the function should return "apple banana".

# %%
def add_fruits(fruit1, fruit2):
    return fruit1 + " " + fruit2

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `add_fruits` function to create a variable `fruit_salad` containing the result of adding "apple" and "banana".

# %%
fruit_salad = add_fruits("apple", "banana")
fruit_salad

# %% [markdown] lang="en" tags=["subslide"]
#
# Define a function called `fruit_count` that takes a list of fruits as a parameter and returns the number of fruits in the list.

# %%
def fruit_count(fruit_list):
    return len(fruit_list)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `fruit_count` function to find the number of fruits in the list ["apple", "banana", "orange", "kiwi"].

# %%
fruits = ["apple", "banana", "orange", "kiwi"]
fruit_count(fruits)
# %% [markdown] lang="en" tags=["slide"]
# ## 6.1  Return values
- Calling a function generates a return value, usually assigned to a variable or used in an expression
- Functions written so far have been void with no return value (or return value of None)
- Now, we are going to write fruitful functions

# %% [markdown] lang="en" tags=["slide"]
# ## Return Statement
- `return` statement includes an expression which is used as a return value
- Functions can be concise without temporary variables 
- Multiple return statements can be used, one in each branch of a conditional

# %% [markdown] lang="en" tags=["slide"]
# ## Example of fruitful function
- Example function `area(radius)` returns the area of a circle with the given radius
- Using a temporary variable 'a' to store the area value
  ```python
  def area(radius):
      a = math.pi * radius**2
      return a
  ```
- Alternatively, the temporary variable can be omitted
  ```python
  def area(radius):
      return math.pi * radius**2
  ```

# %% [markdown] lang="en" tags=["slide"]
# ## Return Statement in Conditional
- Having multiple return statements, one in each branch of a conditional 
- As soon as a return statement runs, the function terminates without executing any subsequent statements

# %% [markdown] lang="en" tags=["slide"]
# ## Dead Code and Handling of x = 0
- Code appearing after a return statement, or any other place the flow of execution can never reach, is called dead code
- It is important to ensure that every possible path through the program hits a return statement
- Example function to get the absolute value of x, but it is incorrect as it does not handle case of x being 0

# %% [markdown] lang="en" tags=["slide"]
# ## Handling of x = 0
- If the flow of execution gets to the end of a function, the return value is `None`
- The function to get the absolute value is incorrect as it does not handle case of x being 0

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise
- Exercise to write a `compare` function that takes two values x and y and returns 1 if x > y, 0 if x == y, and -1 if x < y.
# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions
#
# In this mini-workshop, we will practice writing fruitful functions and understanding how return values work in Python.

# %% [markdown] lang="en" tags=["slide"]
# ## Return Statement
#
# A `return` statement is used to include an expression as a return value in a function. This allows functions to generate a return value that can be assigned to a variable or used in an expression. When a `return` statement is encountered, the function terminates and the return value is passed back to the caller.

# %% [markdown] lang="en" tags=["slide"]
# ## Example of fruitful function
#
# Let's consider an example function `double_value` that takes an input parameter `x` and returns double of that value. We can define this function as follows:
#
# ```python
# def double_value(x):
#     return 2*x
# ```

# %% [markdown] lang="en" tags=["subslide"]
#
# Now, let's create a function `triple_value` that takes an input parameter `y` and returns triple of that value. Try implementing this function below:

# %% lang="en"
def triple_value(y):
    return 3*y

# Let's verify our function by calling it with a test input.
triple_value(4)

# %% [markdown] lang="en" tags=["slide"]
# ## Return Statement in Conditional
#
# In fruitful functions, multiple return statements can be used, each within different branches of a conditional statement. As soon as a return statement is executed, the function terminates without executing any subsequent statements.

# %% [markdown] lang="en" tags=["subslide"]
#
# Let's create a function `get_sign` that takes an input value `num` and returns a string indicating whether the input is positive, negative, or zero. Implement this function using conditional statements and return statements.

# %% lang="en"
def get_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Let's test our function with different inputs.
print(get_sign(5))  # Output: Positive
print(get_sign(-3))  # Output: Negative
print(get_sign(0))   # Output: Zero

# %% [markdown] lang="en" tags=["slide"]
# ## Handling Edge Cases
#
# It is important to handle edge cases in fruitful functions to ensure that every possible path through the program hits a return statement. Let's consider an example function `absolute_value` that returns the absolute value of an input number. We need to ensure that the function correctly handles the case of input being 0.

# %% [markdown] lang="en" tags=["subslide"]
#
# Implement the `absolute_value` function below, and make sure to handle the case when the input is 0.

# %% lang="en"
def absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x
    else:
        return 0

# Let's test our function with different inputs including 0.
print(absolute_value(5))   # Output: 5
print(absolute_value(-3))  # Output: 3
print(absolute_value(0))   # Output: 0

# %% [markdown] lang="en" tags=["subslide"]
#
# It's important to ensure that the `absolute_value` function handles the case of input being 0, as evidenced by the test case above.

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise
#
# Now it's time for you to write your own fruitful function! 
#
# Write a function called `compare` that takes two values `x` and `y` as input, and returns:
# - 1 if `x` is greater than `y`
# - 0 if `x` is equal to `y`
# - -1 if `x` is less than `y`
# %% [markdown] lang="en" tags=["slide"]
# ## Incremental development
- As you write larger functions, you might find yourself spending more time debugging
- Incremental development is an approach to avoid long debugging sessions by adding and testing only a small amount of code at a time

# %% [markdown] lang="en" tags=["slide"]
# - As an example, consider the task of finding the distance between two points given by the coordinates (x1,y1) and (x2,y2)
- The distance can be calculated using the Pythagorean theorem: $distance=\sqrt{(x2-x1)^2+(y2-y1)^2}$

# %% [markdown] lang="en" tags=["slide"]
# - The first step in incremental development is to consider what a function to calculate distance should look like in Python
- Determine the inputs (parameters) and the output (return value)
- Create an initial version of the function as a syntactically correct outline

# %% [markdown] lang="en" tags=["slide"]
# - Test the initial version of the function with sample arguments to confirm it is syntactically correct and runs without errors
- Use sample arguments that you can verify the correct result for to ensure the function runs correctly

# %% [markdown] lang="en" tags=["slide"]
# - Once confirmed that the initial version runs syntactically correct, start adding code to the body of the function
- Incrementally add small chunks of code at a time to build and test the function
- Use temporary variables and print statements to debug and verify the calculations within the function
# %% [markdown] lang="en" tags=["slide"]
# ## Fruitful Functions: Workshop

# %% [markdown] lang="en" tags=["slide"]
# - In this workshop, we will explore the concept of fruitful functions in Python
# - We will learn about incremental development and how to create and test functions step by step

# %% [markdown] lang="en" tags=["slide"]
# - Let's start by understanding the concept of incremental development in the context of creating fruitful functions

# %% [markdown] lang="en" tags=["subslide"]
# ## Incremental Development
# - As you write larger functions, you might find yourself spending more time debugging
# - Incremental development is an approach to avoid long debugging sessions by adding and testing only a small amount of code at a time

# %% [markdown] lang="en" tags=["subslide"]
# - As an example, consider the task of creating a function to calculate the surface area of a sphere
# - The surface area of a sphere can be calculated using the formula: $4 * \pi * r^2$, where r is the radius of the sphere

# %% [markdown] lang="en" tags=["subslide"]
# - The first step in incremental development is to consider what the function to calculate the surface area should look like in Python
# - Determine the inputs (parameters) and the output (return value)
# - Create an initial version of the function as a syntactically correct outline

# %% [markdown] lang="en" tags=["subslide"]
# - Test the initial version of the function with sample arguments to confirm it is syntactically correct and runs without errors
# - Use sample arguments that you can verify the correct result for to ensure the function runs correctly

# %% [markdown] lang="en" tags=["subslide"]
# - Once confirmed that the initial version runs syntactically correct, start adding code to the body of the function
# - Incrementally add small chunks of code at a time to build and test the function
# - Use temporary variables and print statements to debug and verify the calculations within the function

# %% [markdown] lang="en" tags=["subslide"]
# Now, let's move on to the exercises to practice incremental development and fruitful functions

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 1: Calculate Cube Volume

# %% [markdown] lang="en" tags=["subslide"]
# - Define a function called `calculate_cube_volume` that takes a single parameter `side_length` (float or int)
# - The function should return the volume of a cube with the given side length

# %% [markdown] lang="en" tags=["subslide"]
# - Follow the incremental development approach to build and test the function
# - Use print statements and sample input values to verify the correctness of the function

# %% [markdown] lang="en" tags=["subslide"]
# - Once you have defined the function, test it with different side lengths (e.g., 5, 7.5, 10) to ensure it produces the correct volume

# %% [markdown] lang="en" tags=["subslide"]
# - Finally, call the function with a side length of 4.2 and print the result to verify the correctness

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 2: Calculate Circle Area

# %% [markdown] lang="en" tags=["subslide"]
# - Define a function called `calculate_circle_area` that takes a single parameter `radius` (float or int)
# - The function should return the area of a circle with the given radius
# - Use the value of `pi` from the `math` module to perform the calculation

# %% [markdown] lang="en" tags=["subslide"]
# - Follow the incremental development approach to build and test the function
# - Use print statements and sample input values to verify the correctness of the function

# %% [markdown] lang="en" tags=["subslide"]
# - Once you have defined the function, test it with different radii (e.g., 3, 6.5, 9) to ensure it produces the correct area

# %% [markdown] lang="en" tags=["subslide"]
# - Finally, call the function with a radius of 5.2 and print the result to verify the correctness

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 3: Calculate Discounted Price

# %% [markdown] lang="en" tags=["subslide"]
# - Define a function called `calculate_discounted_price` that takes two parameters: `original_price` (float) and `discount_percentage` (float)
# - The function should return the discounted price after applying the percentage discount

# %% [markdown] lang="en" tags=["subslide"]
# - Follow the incremental development approach to build and test the function
# - Use print statements and sample input values to verify the correctness of the function

# %% [markdown] lang="en" tags=["subslide"]
# - Once you have defined the function, test it with different original prices and discount percentages to ensure it produces the correct discounted price

# %% [markdown] lang="en" tags=["subslide"]
# - Finally, call the function with an original price of 100 and a discount percentage of 20% and print the result to verify the correctness

# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - In this workshop, we explored the concept of fruitful functions and incremental development
# - We practiced creating and testing functions step by step, using print statements and sample input values to verify correctness
# - This approach helps in avoiding long debugging sessions and leads to the development of reliable and accurate functions in Python
# %% [markdown] lang="en" tags=["slide"]
# ## 6.3  Composition
- One function can be called from within another
- Example: writing a function to compute the area of a circle based on the center and a point on the perimeter
- Encapsulate distance calculation and area calculation in a function
- Composing the function calls to make the code more concise
-----Start Workshop-----
# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions
#
# In this workshop, we will work with fruitful functions and explore different ways to use them.

# %% [markdown] lang="en" tags=["subslide"]
#
# Write a Python function called `square` that takes a number as input and returns the square of that number.

# %% lang="en"
def square(num):
    return num * num

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `square` function to calculate the square of 7.

# %% lang="en"
square(7)

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function called `multiply` that takes two numbers as input and returns their product.

# %% lang="en"
def multiply(num1, num2):
    return num1 * num2

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `multiply` function to calculate the product of 10 and 3.

# %% lang="en"
multiply(10, 3)

# %% [markdown] lang="en" tags=["subslide"]
#
# Write a function called `is_even` that takes a number as input and returns `True` if the number is even, and `False` otherwise.

# %% lang="en"
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `is_even` function to check if 10 is even.

# %% lang="en"
is_even(10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `is_even` function to check if 7 is even.

# %% lang="en"
is_even(7)
-----End Workshop-----
# %% [markdown] lang="en" tags=["slide"]
# ## Boolean Functions
- Functions can return booleans, which is often convenient for encapsulating complicated tests inside functions
- The result of the comparison operator `==` is a boolean, so we can return it directly
- Boolean functions are often used in conditional statements

# %% [markdown] lang="en" tags=["slide"]
# - The function `is_divisible(x, y)` returns either `True` or `False` to indicate whether `x` is divisible by `y`
- The extra comparison in conditional statements such as `if is_divisible(x, y) == True` is unnecessary
- An exercise is to write a function `is_between(x, y, z)` that returns `True` if `x ≤ y ≤ z` or `False` otherwise 

# %% [markdown] lang="en" tags=["slide"]
# - The functions can be used to ask yes/no questions by naming them accordingly
- As an example, the function `is_divisible(x, y)` returns either `True` or `False` to indicate whether `x` is divisible by `y`
# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions (Part 1)
# Let's learn about boolean functions and how to use the return values from them!
# 
# - We will start by using the `is_divisible(x, y)` function that returns `True` if `x` is divisible by `y` and `False` otherwise. 
# - Then, we will create our own boolean function `is_between(x, y, z)` that returns `True` if `x ≤ y ≤ z` or `False` otherwise.

# %% [markdown] lang="en" tags=["subslide"]
#
# The function `is_divisible(x, y)` returns either `True` or `False` to indicate whether `x` is divisible by `y`.

# %% [markdown] lang="en" tags=["subslide"]
#
# Define a function called `is_divisible` that takes two parameters `x` and `y`, and returns `True` if `x` is divisible by `y`, and `False` otherwise.
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

# %% [markdown] lang="en" tags=["subslide"]
#
# Now, test the function with some values to verify that it is working correctly.
is_divisible(10, 2)  # Expected output: True

# %% [markdown] lang="en" tags=["subslide"]
#
# An exercise is to write a function `is_between(x, y, z)` that returns `True` if `x ≤ y ≤ z` or `False` otherwise.
# 
# Define a function called `is_between` that takes three parameters `x`, `y`, and `z`, and returns `True` if `x ≤ y ≤ z`, and `False` otherwise.
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

# %% [markdown] lang="en" tags=["subslide"]
#
# Now, test the function with some values to verify that it is working correctly. 
is_between(5, 10, 15)  # Expected output: True

# %% [markdown] lang="en" tags=["subslide"]
#
# You can use the functions to ask yes/no questions by naming them accordingly. 
# 
# For example, the function `is_divisible(x, y)` returns either `True` or `False` to indicate whether `x` is divisible by `y`.

# %%
# Let's test the is_divisible and is_between functions with some additional values
is_divisible(20, 7)  # Expected output: False

# %% [markdown] lang="en" tags=["subslide"]
#
# Feel free to play around with the functions and try different input values to see how they work!

# %% [markdown] lang="en" tags=["subslide"]
# 
# Good job completing the workshop! Now you have a better understanding of boolean functions and how to use the return values from them. Keep practicing to solidify your understanding.

# %% [markdown] lang="en" tags=["slide"]
# ## More Recursion
# - Python is a complete programming language, which means that anything that can be computed can be expressed in this language
# - In fact, any program ever written could be rewritten using only the language features learned so far
# - Validation is from the Turing Thesis, initially accomplished by Alan Turing
# - For an accurate discussion of the Turing Thesis, Michael Sipser's book "Introduction to the Theory of Computation" is recommended
# - A recursive definition is similar to a circular definition i.e. it contains a reference to the thing being defined

# %% [markdown] lang="en" tags=["slide"]
# ## Factorial Function
# - The definition of the factorial function is !n = n(n-1)!
# - A recursive definition allows us to write a Python program to evaluate it
# - The first step involves deciding what the parameters should be

# %% [markdown] lang="en" tags=["slide"]
# ## Python Program to Calculate Factorial Function
# - If the argument happens to be 0, return 1
# - Otherwise, make a recursive call to find the factorial of n-1 and then multiply it by n
Here is the workshop for the topic "Fruitful Functions":

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Fruitful Functions
#
# - Define a function called `square` that takes a single argument `x` and returns the square of `x`.
# - Define a function called `add` that takes two arguments `a` and `b` and returns the sum of `a` and `b`.

# %% lang="en"
def square(x):
    return x ** 2

# %% lang="en"
def add(a, b):
    return a + b

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `square` function to calculate the squares of the numbers 1, 2, and 3.

# %% lang="en"
square(1), square(2), square(3)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `add` function to calculate the sum of the numbers 4 and 5.

# %% lang="en"
add(4, 5)

# %% [markdown] lang="en" tags=["subslide"]
#
# Define a function called `is_even` that takes a single argument `n` and returns `True` if `n` is even, and `False` otherwise.

# %% lang="en"
def is_even(n):
    return n % 2 == 0

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `is_even` function to check if the numbers 6, 7, and 8 are even.

# %% lang="en"
is_even(6), is_even(7), is_even(8)
# %% [markdown] lang="en" tags=["slide"]
# ## 6.6 Leap of faith
- Reading programs by following the flow of execution can quickly become overwhelming 
- An alternative approach is the "leap of faith", where when you come to a function call, you assume that the function works correctly and returns the right result 
- This is similar to using built-in functions where you don't examine the bodies of the functions, you just assume that they work 
- The same is true for your own functions once you have convinced yourself that they are correct; you can use the function without examining the body again 
- When dealing with recursive programs, instead of following the flow of execution, you should assume that the recursive call works and then ask if you can compute the result based on that assumption 
- It might be strange to assume that the function works correctly while you're still writing it, but that's why it's called a leap of faith
-----Start Workshop-----
# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions (Part 1)
#
# - Define a function called `addition` that takes two parameters `a` and `b` and returns their sum.
# - Define a function called `subtraction` that takes two parameters `a` and `b` and returns their difference.

# %% lang="python"
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `addition` function to calculate the sum of 10 and 20.

# %% lang="python"
addition(10, 20)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `subtraction` function to calculate the difference between 30 and 15.

# %% lang="python"
subtraction(30, 15)

# %% [markdown] lang="en" tags=["subslide"]
#
# Define a function called `multiplication` that takes two parameters `a` and `b` and returns their product.
# Define a function called `division` that takes two parameters `a` and `b` and returns the result of dividing `a` by `b`.

# %% lang="python"
def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `multiplication` function to calculate the product of 8 and 5.

# %% lang="python"
multiplication(8, 5)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `division` function to calculate the result of dividing 50 by 10.

# %% lang="python"
division(50, 10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Define a function called `power` that takes two parameters `base` and `exponent` and returns the result of raising `base` to the power of `exponent`.

# %% lang="python"
def power(base, exponent):
    return base ** exponent

# %% [markdown] lang="en" tags=["subslide"]
#
# Use the `power` function to calculate 2 raised to the power of 5.

# %% lang="python"
power(2, 5)
-----End Workshop-----
# %% [markdown] lang="en" tags=["slide"]
# ## One more example
# - Another common example of a recursively defined mathematical function is the fibonacci sequence
# - The fibonacci sequence has the following recursive definition: 
#   - fibonacci(0) = 0
#   - fibonacci(1) = 1
#   - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# - Translating the definition into Python, it looks like this:

# %% [markdown] lang="en" tags=["slide"]
# ## One more example
# - Translated into Python, it looks like this:
# - def fibonacci(n):
#     - if n == 0:
#         - return 0
#     - elif n == 1:
#         - return 1
#     - else:
#         - return fibonacci(n-1) + fibonacci(n-2)

# %% [markdown] lang="en" tags=["slide"]
# ## One more example
# - If you try to follow the flow of execution for the fibonacci sequence for even a fairly small value of n, it can be challenging
# - According to the leap of faith, if you assume that the two recursive calls work correctly, then it is clear that you get the right result by adding them together.
# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions (Part 1)
# 
# - Define a function called `calculate_circle_area` that takes a parameter `radius` and returns the area of a circle with that radius.
# - Use the formula for the area of a circle: $A = \pi r^2$.

# %% lang="en"
import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# %% [markdown] lang="en" tags=["subslide"]
#
# Write a function called `calculate_triangle_area` that takes two parameters `base` and `height` and returns the area of a triangle with that base and height.
# Use the formula for the area of a triangle: $A = \frac{1}{2} \times base \times height$.

# %%
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function called `calculate_rectangle_area` that takes two parameters `length` and `width` and returns the area of a rectangle with that length and width.
# Use the formula for the area of a rectangle: $A = length \times width$.

# %%
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function called `calculate_square_area` that takes a parameter `side` and returns the area of a square with that side length.
# Use the formula for the area of a square: $A = side^2$.

# %%
def calculate_square_area(side):
    area = side ** 2
    return area
# %% [markdown] lang="en" tags=["slide"]
# ## Checking types
- When calling a function with a non-integer input, it can lead to infinite recursion
- To handle this, we can use the `isinstance` function to verify the type of the argument and ensure it is positive
- The `factorial` function can be modified to check for:
    - Non-integer input
    - Negative integers
- Upon encountering these cases, the function prints an error message and returns `None`
- The program demonstrates the use of "guardians" to protect the code from values that might cause errors

# %% [markdown] lang="en" tags=["slide"]
# ## Checking types (Code)
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
# %% [markdown] lang="en" tags=["subslide"]
# ## Mini-workshop: Fruitful Functions
# In this mini workshop, we will work with fruitful functions and learn how to handle different input types and conditions in our functions.

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 1
# Define a function called `calculate_circle_area` that takes a single argument `r` (radius) and calculates the area of a circle. The function should check if the input `r` is a positive number, and if not, it should print an error message and return `None`. Use the value of π as 3.14159.

# %% lang="en"
import math

def calculate_circle_area(r):
    if not isinstance(r, (int, float)) or r <= 0:
        print('Radius should be a positive number.')
        return None
    else:
        return math.pi * (r ** 2)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 2
# Define a function called `calculate_triangle_area` that takes two arguments `base` and `height` and calculates the area of a triangle. The function should check if the inputs `base` and `height` are positive numbers, and if not, it should print an error message and return `None`.

# %% lang="en"
def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or base <= 0 or not isinstance(height, (int, float)) or height <= 0:
        print('Base and height should be positive numbers.')
        return None
    else:
        return 0.5 * base * height

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 3
# Define a function called `calculate_cylinder_volume` that takes two arguments `r` (radius) and `h` (height) and calculates the volume of a cylinder. The function should check if the inputs `r` and `h` are positive numbers, and if not, it should print an error message and return `None`.

# %% lang="en"
def calculate_cylinder_volume(r, h):
    if not isinstance(r, (int, float)) or r <= 0 or not isinstance(h, (int, float)) or h <= 0:
        print('Radius and height should be positive numbers.')
        return None
    else:
        return math.pi * (r ** 2) * h

# %% [markdown] lang="en" tags=["subslide"]
# ## Key Takeaways

# - Fruitful functions can return a value and perform a specific task.
# - We can use type checking and condition handling to ensure that our functions receive the correct input.
# - Handling different scenarios and providing meaningful error messages can make our functions more robust and user-friendly.

# We have successfully created fruitful functions for calculating the area of a circle, area of a triangle, and volume of a cylinder.

# Now it's time to practice and apply these concepts and create more fruitful functions for various scenarios!
# %% [markdown] lang="en" tags=["slide"]
# ## Debugging
- Breaking a large program into smaller functions creates natural checkpoints for debugging
- Three possibilities to consider if a function is not working:
  - Something wrong with the arguments the function is getting; a precondition is violated
  - Something wrong with the function; a postcondition is violated
  - Something wrong with the return value or the way it is being used
- To rule out the first possibility, you can add a print statement at the beginning of the function and display the values of the parameters or write code that checks the preconditions explicitly

# %% [markdown] lang="en" tags=["slide"]
# ## Debugging (cont.)
- If the parameters look good, add a print statement before each return statement and display the return value
- Consider calling the function with values that make it easy to check the result
- If the function seems to be working, look at the function call to make sure the return value is being used correctly (or used at all!)
- Adding print statements at the beginning and end of a function can help make the flow of execution more visible
# %% [markdown] lang="en" tags=["slide"]
# ## Fruitful Functions
- A fruitful function is a function that returns a value
- The return statement is used to send a value back from the function to the part of the program that called the function
- The expression after the return statement is called the return value

# %% [markdown] lang="en" tags=["slide"]
# ## Fruitful Functions (cont.)
- To create a fruitful function:
  - Define the function using def keyword followed by the function name and parameters
  - Write the code inside the function with necessary computations
  - Use the return statement to return the computed value

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise: Fruitful Functions (Part 1)
#
# - Define a function called `cylinder_volume` that takes two parameters `radius` and `height` and returns the volume of a cylinder using the formula: 
#   `volume = π * radius^2 * height`
# - Use the value `3.14159` for π and return the volume with 2 decimal places.

# %% [markdown] lang="en" tags=["subslide"]
#
# Solution:
#
# ```python
# def cylinder_volume(radius, height):
#     volume = 3.14159 * radius**2 * height
#     return round(volume, 2)
# ```

# %% [markdown] lang="en" tags=["subslide"]
#
# Test your function with a cylinder of radius 5 and height 10.

# %%
def cylinder_volume(radius, height):
    volume = 3.14159 * radius**2 * height
    return round(volume, 2)

cylinder_volume(5, 10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Test your function with a cylinder of radius 2.5 and height 8.

# %%
cylinder_volume(2.5, 8)
# %% [markdown] lang="en" tags=["slide"]
# ## Glossary
- temporary variable: A variable used to store an intermediate value in a complex calculation
- dead code: Part of a program that can never run, often because it appears after a return statement
- incremental development: A program development plan intended to avoid debugging by adding and testing only a small amount of code at a time
- scaffolding: Code that is used during program development but is not part of the final version
# %% [markdown] lang="en" tags=["subslide"]
# 
# ## Mini-workshop: Fruitful Functions
#
# - Define a function called `multiply` that takes two arguments and returns their product.
# - Call the `multiply` function with the arguments 5 and 3. Print the result.

# %% lang="python"
# Define the multiply function
def multiply(x, y):
    return x * y

# Call the multiply function
result = multiply(5, 3)
print(result)

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function called `power` that takes two arguments, a base and an exponent, and returns the result of raising the base to the exponent.
# - Call the `power` function with the arguments 2 and 3, and print the result.

# %% lang="python"
# Define the power function
def power(base, exponent):
    return base ** exponent

# Call the power function
result = power(2, 3)
print(result)

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function called `absolute_value` that takes a number as an argument and returns its absolute value.
# - Call the `absolute_value` function with the argument -5, and print the result.

# %% lang="python"
# Define the absolute_value function
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

# Call the absolute_value function
result = absolute_value(-5)
print(result)

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function called `average` that takes a list of numbers as an argument and returns the average of those numbers.
# - Call the `average` function with the argument `[3, 6, 9]` and print the result.

# %% lang="python"
# Define the average function
def average(nums):
    return sum(nums) / len(nums)

# Call the average function
result = average([3, 6, 9])
print(result)
# %% [markdown] lang="en" tags=["slide"]
# ## 6.11  Exercises
# - **Exercise 1** asks us to draw a stack diagram for the given program and identify what the program prints
# - We're required to create a function `ack` to evaluate the Ackermann function for **Exercise 2**
# - **Exercise 3** expects us to create functions to identify if a word is a palindrome and evaluate a given string
# - **Exercise 4** instructs us to create a function called `is_power` to identify if a number is a power of another number
# - Lastly, **Exercise 5** require us to develop a function to identify the greatest common divisor of two numbers.
# %% [markdown] lang="en" tags=["slide"]
# ## 6.11  Exercises
# - **Exercise 1** asks us to draw a stack diagram for the given program and identify what the program prints
# - We're required to create a function `ack` to evaluate the Ackermann function for **Exercise 2**
# - **Exercise 3** expects us to create functions to identify if a word is a palindrome and evaluate a given string
# - **Exercise 4** instructs us to create a function called `is_power` to identify if a number is a power of another number
# - Lastly, **Exercise 5** require us to develop a function to identify the greatest common divisor of two numbers.

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Fruitful Functions
#
# In this workshop, we'll focus on creating fruitful functions that return values after performing computations. Let's start by defining some basic functions and then move on to the exercises.

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function `add_numbers` that takes two numbers as input and returns the sum of the two numbers.

# %%
def add_numbers(num1, num2):
    return num1 + num2

add_numbers(5, 3)

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function `multiply_numbers` that takes two numbers as input and returns the product of the two numbers.

# %%
def multiply_numbers(num1, num2):
    return num1 * num2

multiply_numbers(5, 3)

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a function `calculate_power` that takes a base and an exponent as input and returns the result of the base raised to the exponent.

# %%
def calculate_power(base, exponent):
    return base ** exponent

calculate_power(2, 3)

# %% [markdown] lang="en" tags=["subslide"]
#
# Now that we've covered some basic fruitful functions, let's move on to the exercises to apply what we've learned.

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Exercise 1
#
# For this exercise, draw a stack diagram for the given program and identify what the program prints.

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Exercise 2
#
# For this exercise, we're required to create a function `ack` to evaluate the Ackermann function. The Ackermann function is defined for non-negative integers `m` and `n` as follows:
# - If `m = 0`, the result is `n + 1`.
# - If `m > 0` and `n = 0`, the result is `ack(m-1, 1)`.
# - If `m > 0` and `n > 0`, the result is `ack(m-1, ack(m, n-1))`.

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Exercise 3
#
# For this exercise, create a function called `is_palindrome` that takes a string as input and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Exercise 4
#
# For this exercise, create a function called `is_power` that takes two integers, `a` and `b`, as input and returns `True` if `a` is a power of `b`. A number `a` is a power of `b` if it is divisible by `b` and `a/b` is also a power of `b`.

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Exercise 5
#
# For this exercise, develop a function called `gcd` that takes two positive integers as input and returns their greatest common divisor. The greatest common divisor (GCD) of two integers is the largest positive integer that divides each of the integers without a remainder. Use the Euclidean algorithm to implement the function.

# %% [markdown] lang="en" tags=["subslide"]
#
# Great work on learning about fruitful functions and solving exercises! Keep practicing and applying these concepts to build your expertise in Python programming.
