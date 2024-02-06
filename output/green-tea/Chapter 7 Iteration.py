# j2 from 'macros.j2' import header
# {{ header("Iteration", "Iteration") }}

# %% [markdown] lang="en" tags=["slide"]
# # Chapter 7: Iteration
# - Iteration allows running a block of statements multiple times
# - Previously explored iteration types include recursion (Section 5.8) and `for` loops (Section 4.2)
# - This chapter introduces iteration via `while` loops
# - Additionally, we'll discuss more about variable assignment

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Iteration
# - Iteration is a core concept in programming that enables repetitive execution of code blocks
# - Recursion is a form of iteration where a function calls itself
# - `for` loops iterate over elements of a sequence or iterable
# - `while` loops continue executing as long as a condition remains true

# %% [markdown] lang="en" tags=["slide"]
# ## Variable Assignment Revisited
# - Variable assignment is crucial in controlling the flow of iteration
# - Proper management of variable values is essential for accurate and efficient iterations
# - In the context of loops, variable assignment often involves initializing counters or accumulators before the loop starts
# - Updating variable values appropriately within the loop body is key to avoiding infinite loops or incorrect results

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop 1: Iteration Exploration
#
# In this workshop, we will delve into the use of `while` loops for iteration in Python. We will also reinforce our understanding of iteration with variable assignment, crucial for managing loop execution and updates efficiently.
#
# ### Task 1: Counting Up
# - Initialize a variable `counter` with the value `0`.
# - Use a `while` loop to increment `counter` by `1` until it reaches `10`.
# - Print the value of `counter` after the loop ends to confirm it's `10`.

# %% lang="en"
counter = 0
while counter < 10:
    counter += 1
print(counter)  # Should print 10

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Collecting Squares
#
# - Create an empty list named `squares`.
# - Using a `while` loop, populate this list with the squares of the numbers from `1` to `5`.
# - Ensure you use a variable to track the current number inside your loop.
# - After the loop, print `squares` to ensure it contains `[1, 4, 9, 16, 25]`.

# %% lang="en"
squares = []
number = 1
while number <= 5:
    squares.append(number**2)
    number += 1
print(squares)  # Should print [1, 4, 9, 16, 25]

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: Using `while` for Input Validation
#
# - Write a `while` loop that continually prompts the user to enter their age.
# - The loop should only break if the user enters a valid age (integer from `0` to `120`).
# - After the loop ends, print a message saying `"Age entered: <age>."` with `<age>` replaced by the user's input.
# - **Hint:** Use `input()` to prompt for user input and `int()` to convert the input string to an integer. Be aware of exceptions that can occur with `int()` and handle them gracefully.

# %% lang="en"
while True:
    user_input = input("Please enter your age (0-120): ")
    try:
        age = int(user_input)
        if 0 <= age <= 120:
            break
    except ValueError:
        pass  # Ignore invalid integer inputs
print(f"Age entered: {age}.")

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Challenge Task: Fibonacci Sequence
#
# - The Fibonacci sequence is a sequence of numbers where the next number is found by adding up the two numbers before it.
# - Starting with `0` and `1`, the sequence goes `0, 1, 1, 2, 3, 5, 8, ...`
# - Using a `while` loop, generate the first `10` Fibonacci numbers and store them in a list named `fibonacci`.
# - Print `fibonacci` after the loop to ensure it contains the correct sequence.

# %% lang="en"
fibonacci = [0, 1]
while len(fibonacci) < 10:
    # Append the sum of the last two elements in the sequence
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)  # Should print the first 10 Fibonacci numbers

# %% [markdown] lang="en" tags=["slide"]
# ## 7.1 Reassignment
# - Variables can be assigned multiple times; later assignments change the variable's reference
# - Initial display of `x` shows value of 5, subsequent display shows value of 7
# - Python's equal sign (`=`) means assignment, not mathematical equality
# - Reassignment can make variables temporarily equal, but they may not remain that way

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Python Assignment
# - Assignment is not a symmetric relationship like mathematical equality
#   - `a = 7` is valid, whereas `7 = a` is not
# - Assignment creates a temporary equality, not a permanent one
#   - Example: assigning `b = a` makes them equal until `a` changes
# - Use reassignment cautiously to avoid code confusion and debugging issues

# %%
x = 5
x

# %%
x = 7
x

# %%
a = 5
b = a  # a and b are now equal
a = 3  # a and b are no longer equal
b

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop 2: Iteration
#
# ### Introduction to Iteration with For Loops

# %% [markdown] lang="en" tags=["slide"]
# - Iteration allows you to run a block of code repeatedly with some parameters updated each time through the loop.
# - A `for` loop in Python iterates over the items of any sequence (a list, a tuple, a dictionary, a set, or a string), in the order that they appear in the sequence.
# - Let's experiment with some basic `for` loops in Python.

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Simple For Loop
#
# Use a `for` loop to print each character in the string `"Python"`.

# %% lang="en"
for character in "Python":
    print(character)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Iterating Over a List
#
# Create a list called `fruits` with the elements `"apple"`, `"banana"`, and `"cherry"`.
# Then use a `for` loop to print each element of the list.

# %% lang="en"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Using `range()` Function
#
# The `range()` function returns a sequence of numbers and is commonly used in `for` loops.
#
# Use a `for` loop and the `range()` function to print numbers from 1 to 5.

# %% lang="en"
for number in range(1, 6):
    print(number)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Nested For Loops
#
# Using nested `for` loops, print a 3x3 grid of asterisks (`*`).
# Your output should look like this:
#
# ```
# * * *
# * * *
# * * *
# ```

# %% lang="en"
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # to move to the next line after each row

# %% [markdown] lang="en" tags=["subslide"]
#
# ### For Loop With Else
#
# A `for` loop can have an optional `else` block which is executed when the loop is exhausted.
# Print numbers from 1 to 3 using a `for` loop and add an `else` statement to print `"Done!"` when the loop is finished.

# %% lang="en"
for number in range(1, 4):
    print(number)
else:
    print("Done!")

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise: Creating a Dictionary from Lists
#
# Given two lists: `keys = ["One", "Two", "Three"]` and `values = [1, 2, 3]`, use a `for` loop to create a dictionary that maps each key to its corresponding value. Print the created dictionary.

# %% lang="en"
keys = ["One", "Two", "Three"]
values = [1, 2, 3]
mapped_dict = {}
for i in range(len(keys)):
    mapped_dict[keys[i]] = values[i]

print(mapped_dict)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Summary
# - In this workshop, we explored the basics of iteration in Python using `for` loops. We practiced iterating over strings, lists, and using functions like `range()` to generate sequences of numbers.
# - We also looked at nested loops, `for` loops with `else`, and an exercise on creating dictionaries from lists using loops.


# %% [markdown] lang="en" tags=["slide"]
# ## 7.2  Updating Variables
# - Variable updates involve reassignment where the new value relies on its previous value.
# - Example of increment: `x = x + 1`. This pattern adds one to the current value of `x`.
# - Attempting to update a non-initialized variable results in an error: `NameError: name 'x' is not defined`.
# - Initialization before updating is crucial: `x = 0` followed by `x = x + 1`.
# - Increment (`x = x + 1`) and decrement (`x = x - 1`) are common update operations.

# %%
x = 0

# %%
x = x + 1

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop 3: Iteration
#
# Iteration refers to the process of executing a block of statements repeatedly for a set number of times or until a certain condition is met. Python provides several iteration mechanisms, such as `for` loops and `while` loops. In this workshop, we will explore some practical applications of iteration.
#
# - Start by creating a variable `counter` initialized to 0.
# - Use a while loop to increment `counter` until it is equal to 5. Print the value of `counter` in each iteration.

# %% lang="en"
counter = 0
while counter < 5:
    counter = counter + 1
    print(counter)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use a `for` loop to iterate over a list of numbers from 1 to 5, and print the square of each number. Hint: Use `range` to generate the list of numbers.

# %% lang="en"
for number in range(1, 6):  # Remember, `range` stops before the second number
    print(number**2)

# %% [markdown] lang="en" tags=["subslide"]
#
# Given a list `numbers = [2, 4, 6, 8, 10]`, use a `for` loop to iterate over it and print each number multiplied by 10.

# %% lang="en"
numbers = [2, 4, 6, 8, 10]
for number in numbers:
    print(number * 10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Use a `for` loop to create a list of the first 10 square numbers (i.e., the square of numbers from 1 to 10). Print the list at the end. Hint: Start with an empty list and use the `.append()` method to add each square number to the list.

# %% lang="en"
square_numbers = []
for number in range(1, 11):
    square_numbers.append(number**2)
square_numbers

# %% [markdown] lang="en" tags=["slide"]
# ## The while statement
# - Computers excel at automating repetitive tasks, a concept known as iteration in programming.
# - Python offers `while` and `for` statements to facilitate iteration.
# - The `while` statement is used to repeat a task while a condition is true.
# - We'll explore how to use `while` with examples, including how to avoid infinite loops.

# %% [markdown] lang="en" tags=["slide"]
# ## Countdown Example with `while`
# - A `while` loop can make the countdown process straightforward.
# - The structure of a `while` loop allows for repetitive tasks based on a condition.
# - It keeps executing its block of code as long as the condition remains true.
# - Let's look at a countdown example using a `while` loop:


# %%
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print("Blastoff!")


# Example usage
countdown(5)

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding `while` Loops
# - The flow of a `while` loop includes checking a condition and executing the loop body if the condition is true.
# - If the condition becomes false, the loop terminates and execution continues with the next statement.
# - To prevent infinite loops, ensure that the loop condition will eventually become false.
# - Infinite loops are a common error, akin to an endless shampoo bottle instruction: "Lather, rinse, repeat."

# %% [markdown] lang="en" tags=["slide"]
# ## Example: Sequence Generation with `while`
# - Let's explore a more complex example, where a sequence of numbers is generated until a certain condition is met.
# - This example illustrates how to deal with even and odd numbers differently in a loop.
# - The loop condition is designed to continue until a specific value is reached.
# - Understanding the termination condition for this loop can be challenging.


# %%
def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else:  # n is odd
            n = n * 3 + 1


# Example usage
sequence(3)

# %% [markdown] lang="en" tags=["slide"]
# ## Loop Termination and the Collatz Conjecture
# - Determining whether certain loops terminate can sometimes be straightforward and, at other times, extremely complex.
# - The sequence example introduces the Collatz conjecture, an unsolved mathematical problem.
# - For some loops, proving termination depends on the input values and the loop's behavior.
# - The Collatz conjecture poses a challenging question: does the sequence loop terminate for all positive integers?

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise: Iteration instead of Recursion
# - As a practical exercise, try rewriting the `print_n` function (from previous sections) using iteration instead of recursion.
# - This exercise helps in understanding the practical differences between iterative and recursive approaches.
# - Experimenting with rewriting recursive functions as iterative ones can deepen your understanding of loop mechanics.
# - Below is a template to get started. Replace it with your iterative solution.


# %%
def print_n(n):
    # Your code here: rewrite using iteration instead of recursion
    pass


# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: While Loops
#
# Iteration is a core concept in programming, allowing repetitive execution of code blocks based on a condition. In this workshop, we'll explore the `while` loop in Python, which is a fundamental way to implement iteration.

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 1: Simple Countdown
# - Implement a function named `simple_countdown` that takes an integer `n` and prints numbers from `n` down to `1`. After printing `1`, it should print `Go!`.
# - Use a `while` loop to implement this function.
# - Ensure that your function prints each number on a new line.


# %% lang="en"
def simple_countdown(n):
    # Your code here
    while n > 0:
        print(n)
        n -= 1
    print("Go!")


# Example usage
simple_countdown(3)


# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Oddities and Evenness
# - Implement a function named `odd_even_countdown` that takes an integer `n`.
# - If `n` is odd, it counts down only the odd numbers till 1. If `n` is even, it counts down only the even numbers till 2.
# - Use a `while` loop to implement this functionality.
# - Hint: The termination condition of the loop changes based on whether `n` is even or odd.


# %% lang="en"
def odd_even_countdown(n):
    # Your code here
    while n > 0:
        print(n)
        n -= 2 if n % 2 == 0 else 1


# Example usage
odd_even_countdown(5)  # It should print: 5, 3, 1
odd_even_countdown(6)  # It should print: 6, 4, 2

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: Accumulating Sum
# - Implement a function named `accumulating_sum` that uses a `while` loop to add numbers from 1 to `n`, inclusive.
# - The function should return the total sum after adding numbers from 1 to `n`.
# - This task helps understand how loops can be used for cumulative operations.


# %% lang="en"
def accumulating_sum(n):
    # Your code here
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


# Example usage
print(accumulating_sum(10))  # Should print 55 as the result

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 4: The Power of While
# - Challenge: Implement a function named `power_of_while` that takes two integers, `base` and `exponent`.
# - The function calculates `base` to the power of `exponent` using a `while` loop (i.e., `base` ** `exponent`), without using the `**` operator or `pow()` function.
# - Return the calculated value.
# - This task will help you understand how to implement mathematical operations using loops.


# %% lang="en"
def power_of_while(base, exponent):
    # Your code here
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result


# Example usage
print(power_of_while(2, 3))  # Should print 8 as the result

# %% [markdown] lang="en" tags=["slide"]
# ## 7.4  break
# - The `break` statement is used to exit a loop prematurely
# - This is useful when you need to stop the loop based on a condition that is checked within the loop's body, rather than at the start

# %% [markdown] lang="en" tags=["slide"]
# ## Example: User Input Loop
# - When you want to keep taking input from the user until a specific input is received
# - The loop's condition is set to `True` to ensure it keeps running indefinitely
# - The `break` statement is then used to exit the loop based on the user's input

# %%
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)

print("Done!")

# %% [markdown] lang="en" tags=["slide"]
# ## Sample Run
# - In a sample run, the program keeps asking for input
# - If the user types "done", the program exits the loop and prints "Done!"
# - This illustrates the dynamic control you have within loops using the `break` statement

# %%
# Sample Input
"> not done"
"not done"
"> done"
"Done!"

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: While Loops and Break
#
# The goals of this workshop are:
# 1. To understand and apply the `while` loop for repeated actions.
# 2. To utilize the `break` statement to exit a loop based on a dynamic condition.
# 3. To practice iterative processing of user input.
#
# Let's get started with iteration in Python!

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 1: Infinite Echo
#
# - Write a program that continuously asks the user for input and prints what the user typed.
# - The program should break the loop and stop if the user types `"quit"`.
#
# Example of expected functionality:
# ```
# > Hello
# Hello
# > How are you?
# How are you?
# > quit
# ```

# %% lang="en"
while True:
    user_input = input("> ")
    if user_input == "quit":
        break
    print(user_input)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Counting Numbers
#
# - Using a `while` loop, write a program that counts from 1 to 10 and prints each number to the console.
# - The loop should stop once it reaches 10.

# %% lang="en"
count = 1
while count <= 10:
    print(count)
    count += 1

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: User-Controlled Countdown
#
# - Ask the user to input a number.
# - Using a `while` loop, perform a countdown from that number to 1 on the console, and then print `"Liftoff!"`.
#
# Example of expected functionality:
# ```
# Enter a number to countdown from: 5
# 5
# 4
# 3
# 2
# 1
# Liftoff!
# ```

# %% lang="en"
number = int(input("Enter a number to countdown from: "))
while number > 0:
    print(number)
    number -= 1
print("Liftoff!")

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 4: Simple Interest Calculator
#
# - Prompt the user for:
#   - The principal amount (`P`)
#   - The annual interest rate (`r`) as a percentage (e.g., 5 for 5%)
#   - The time period in years (`t`)
# - Calculate the simple interest using the formula `SI = (P * r * t) / 100`
# - Print the calculated simple interest to the console rounded to two decimal places.
#
# Example of expected functionality:
# ```
# Enter the principal amount: 1000
# Enter the annual interest rate (%): 5
# Enter the time period in years: 2
# The simple interest is: 100.0
# ```

# %% lang="en"
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_period = float(input("Enter the time period in years: "))
simple_interest = (principal * interest_rate * time_period) / 100
print(f"The simple interest is: {simple_interest:.2f}")

# %% [markdown] lang="en" tags=["slide"]
# ## 7.5 Square Roots
# - Loops are vital for iteratively improving numerical results
# - Newton's method is a classic example for computing square roots
# - Starting with an estimate, we iteratively refine it to get closer to the actual square root

# %% [markdown] lang="en" tags=["slide"]
# ## Iterative Improvement
# - An initial estimate `x` is progressively improved using `y = (x + a/x) / 2`
# - This process is repeated until the estimate no longer changes significantly

# %% [code]
a = 4
x = 3
y = (x + a / x) / 2
print(y)

# %% [code]
x = y
y = (x + a / x) / 2
print(y)

# %% [code]
x = y
y = (x + a / x) / 2
print(y)

# %% [code]
x = y
y = (x + a / x) / 2
print(y)

# %% [markdown] lang="en" tags=["slide"]
# ## Checking for Convergence
# - Directly comparing floating-point numbers is risky due to precision issues
# - Instead, we check if the absolute difference is smaller than a tiny value `epsilon`
# - This approach guides us to stop the iteration once the estimate is precise enough

# %% [code]
epsilon = 0.0000001
while True:
    print(x)
    y = (x + a / x) / 2
    if abs(y - x) < epsilon:
        break
    x = y

# %% [markdown] lang="en" tags=["subslide"]
# ## Mini-Workshop
#
# Iteration in Python allows you to execute a block of code repeatedly. Loops, such as `while` and `for`, are commonly used for iterating over sequences or repeating code until a condition changes. In this workshop, you will practice writing different types of loops.

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 1: Counting with Loops
#
# Use a `for` loop to count from 1 to 10, printing out each number on a new line.

# %% lang="en"
for i in range(1, 11):
    print(i)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 2: Summing Numbers
#
# Write a loop that sums all numbers from 1 to 100. Print the result.

# %% lang="en"
total = 0
for i in range(1, 101):
    total += i
print(total)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 3: Finding the Square Root
#
# - Let's manually compute the square root of a number using iteration (Newton's method shown in the examples).
# - Start with an initial guess `x` for the square root of `a = 25`, then iteratively improve the guess using the formula `y = (x + a / x) / 2`.
# - Repeat this process until the absolute difference between `y` and `x` is less than `epsilon = 0.000001`. Print each guess.

# %% lang="en"
a = 25
x = 3
epsilon = 0.000001
while True:
    y = (x + a / x) / 2
    if abs(y - x) < epsilon:
        break
    x = y
    print(x)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 4: Iterating Over Lists
#
# Given the list `items = ["apple", "banana", "cherry"]`, write a loop that iterates over the list and prints each item.

# %% lang="en"
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# %% [markdown] lang="en" tags=["subslide"]
# Congratulations on completing this mini-workshop on iteration!
# - Through these exercises, you've practiced using `for` and `while` loops for counting, summing numbers, computing square roots using an iterative method, and iterating over list items.

# %% [markdown] lang="en" tags=["slide"]
# ## 7.6 Algorithms
# - Newton's method illustrates what an algorithm is: a mechanical process for solving a certain category of problems, such as computing square roots.
# - Algorithms contrast with memorized solutions, embodying general solutions to problems rather than specific answers.
# - Examples include techniques for addition with carrying, subtraction with borrowing, and long division—all of which are algorithms.
# - A hallmark of algorithms is their mechanical nature, requiring no intelligence to execute, merely following a set of simple rules.

# %% [markdown] lang="en" tags=["slide"]
# ## Characteristics and Challenges of Algorithms
# - Designing algorithms is intriguing and central to computer science, focusing on formulating a series of steps to solve problems.
# - A key challenge in algorithm design is handling tasks that humans perform intuitively, such as understanding natural language.
# - These natural abilities, effortless for humans, are difficult to translate into algorithmic form.
# - This discrepancy highlights both the complexity of human cognition and the intellectual challenges in computer science.

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Workshop: Iteration
#
# Iteration is a fundamental concept in programming, enabling the execution of a block of code repetitively until a certain condition is met. In Python, iteration can be achieved through loops such as `for` and `while`. This workshop focuses on practical exercises to understand and use iteration in Python effectively.
#
# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 1: Sum of Numbers
#
# - Create a list `numbers` containing the first ten positive integers.
# - Using a `for` loop, calculate the sum of all numbers in the `numbers` list and print the result.

# %% lang="en"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print(sum_of_numbers)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Find the Even Numbers
#
# - Given the list `numbers` from the previous task, use a `for` loop and a conditional statement to find all the even numbers in the list.
# - Append the even numbers to a new list called `even_numbers` and print it.

# %% lang="en"
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: Build a Number Triangle
#
# - Using a `for` loop, print the following pattern:
# ```
# 1
# 22
# 333
# 4444
# 55555
# ```
# - Note: The pattern should be easily adjustable to accommodate more lines.

# %% lang="en"
for i in range(1, 6):
    print(str(i) * i)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 4: Fibonacci Sequence
#
# - The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# - Write a `for` loop to generate the first 10 numbers of the Fibonacci sequence and store them in a list called `fibonacci`.
# - The list should start with `[0, 1, 1, 2, 3, 5, ...]`.

# %% lang="en"
fibonacci = [0, 1]
for i in range(2, 10):
    next_number = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_number)
print(fibonacci)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 5: Using `while` Loops
#
# - Write a `while` loop that starts with `x = 0` and increments `x` by `1` on each iteration, printing the value of `x`.
# - The loop should terminate once `x` reaches `5`.
# - Pay careful attention to avoid creating an infinite loop.

# %% lang="en"
x = 0
while x <= 5:
    print(x)
    x += 1

# %% [markdown] lang="en" tags=["slide"]
# ## 7.7  Debugging
# - Writing larger programs increases debugging time due to more code and potential error spots
# - Debugging by bisection can significantly reduce debugging time
#   - Example: Debugging 100 lines of code by bisection vs. line by line
# - Place check points in the program to narrow down the error location

# %% [markdown] lang="en" tags=["slide"]
# ## Efficient Debugging Strategies
# - Add a print statement near the mid-point of the program to verify intermediate values
# - Incorrect mid-point checks indicate problems in the first half of the program, and vice versa
# - Each check effectively halves the potential error space, streamlining error identification

# %% [markdown] lang="en" tags=["slide"]
# ## Practical Debugging Tips
# - Identifying the "middle of the program" isn't about counting lines but assessing error-prone areas
# - Strategically place checks where errors are likely or verification is simple
# - Aim to choose check points that make it equally probable for errors to be before or after the check

# %% [markdown] lang="en" tags=["slide"]
# ## Example of Debugging by Bisection
# - A practical approach to localize the error in fewer steps
# - Not always about finding the exact midpoint but about smartly dividing the problem space
# - Effective use of print statements or other verifiable actions can greatly aid in narrowing down the bug's location

# %% lang="python" tags=["code"]
# Example of adding a print statement to debug:
# Imagine having a function that is not giving the expected output


# %%
def problematic_function(x):
    # Some complex logic here...
    result = x**2 - 2 * x + 1  # An intended operation
    # More complex logic...
    return result


x_test = 4  # Test value
print("Intermediate check:", problematic_function(x_test))
# This print statement serves as a midpoint check to verify the function's behavior

# %%
# Depending on the output of the print statement, we can deduce if the error
# lies before or after this point in the overall logic of our program.

# %% [markdown] lang="en" tags=["slide"]
# ## Mini-workshop: Iteration Techniques in Python

# %% [markdown] lang="en" tags=["subslide"]
# ### Iterating Over a List
#
# - Given the list `num_list` containing the numbers from 1 to 5, write a `for` loop that prints each number multiplied by 2.

# %% lang="python"
num_list = [1, 2, 3, 4, 5]

# %% lang="python"
# Your code here
for num in num_list:
    print(num * 2)

# %% [markdown] lang="en" tags=["subslide"]
# ### Using Enumerate
#
# - Modify the previous loop to also print the index of each element before multiplying it by 2. Utilize `enumerate` in your solution.

# %% lang="python"
# Your code here
for index, num in enumerate(num_list):
    print(f"Index: {index}, Number: {num*2}")

# %% [markdown] lang="en" tags=["subslide"]
# ### List Comprehension
#
# - Use a list comprehension to create a new list named `squared_list` containing the squares of all numbers in `num_list`.

# %% lang="python"
# Your code here
squared_list = [num**2 for num in num_list]
squared_list

# %% [markdown] lang="en" tags=["subslide"]
# ### Iterating Over a Dictionary
#
# - Given the dictionary `colors_with_codes`, iterate over it to print each color name (key) along with its color code (value).
# - `colors_with_codes` is defined with colors as keys and their hexadecimal codes as values.

# %% lang="python"
colors_with_codes = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# %% lang="python"
# Your code here
for color, code in colors_with_codes.items():
    print(f"{color}: {code}")

# %% [markdown] lang="en" tags=["subslide"]
# ### While Loop with Condition
#
# - Using a while loop, print numbers from 1 to 10. Use a variable to track the current number and increment it in each iteration.

# %% lang="python"
# Your code here
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# %% [markdown] lang="en" tags=["subslide"]
# ### Break Statement
#
# - Modify the previous while loop to stop (using the `break` statement) when the current number reaches 5.

# %% lang="python"
# Your code here
current_number = 1
while True:
    if current_number > 5:
        break
    print(current_number)
    current_number += 1

# %% [markdown] lang="en" tags=["subslide"]
# Congratulations for completing the iteration techniques workshop! You've practiced iterating over lists and dictionaries, using enumerate, list comprehensions, while loops, and controlling loop execution with `break`.

# %% [markdown] lang="en" tags=["slide"]
# ## 7.8 Glossary
# - Reassignment refers to assigning a new value to an existing variable
# - Update is a specific type of assignment where the variable's new value depends on its old value

# %% [markdown] lang="en" tags=["slide"]
# - Initialization involves giving an initial value to a variable intended for future updates
# - Increment and decrement are types of updates that respectively increase or decrease the value of a variable

# %% [markdown] lang="en" tags=["slide"]
# - Iteration denotes the repeated execution of a set of statements, achieved via loops or recursive function calls
# - An infinite loop occurs when a loop's terminating condition is never met, causing endless iteration

# %% [markdown] lang="en" tags=["slide"]
# - The term algorithm refers to a general process for solving a specific category of problems, often involving iteration
# ## Mini-workshop: Iterating Through Seasons
### The Task of Seasons
# - Define a variable `seasons` containing a list of the strings `"Spring"`, `"Summer"`, `"Autumn"`, and `"Winter"`.
# - Using a loop, print each element of the `seasons` list.


seasons = ["Spring", "Summer", "Autumn", "Winter"]

for season in seasons:
    print(season)

# %% [markdown] lang="en" tags=["subslide"]
# - Create a variable `countdown` containing the numbers from 10 down to 1 (inclusive).
# - Using a loop, print each number, followed by the word "Liftoff!" after printing the number 1.

# %% lang="en"
countdown = list(range(10, 0, -1))

for number in countdown:
    print(number)
    if number == 1:
        print("Liftoff!")

### Infinite Wisdom
# - **WARNING:** This is a theoretical task. Do not run the code, as it will create an infinite loop.
# - Write a theoretical loop that would print `"Learning is endless"` indefinitely.
# ```python
# WARNING: DO NOT RUN THIS CODE
# while True:
#    print("Learning is endless")
# ```

# %% [markdown] lang="en" tags=["subslide"]
### Numbers and Their Squares
# - Create a list `numbers` containing the numbers 1 through 5.
# - Using a loop, print each number and its square, formatted like: `Number: 1, Square: 1`.

# %%
numbers = list(range(1, 6))

# %%
for number in numbers:
    print(f"Number: {number}, Square: {number**2}")


# %% [markdown] lang="en" tags=["subslide"]
### Breaking the Loop
# - Write a loop that prints numbers from 1 to 10 but stops (breaks) when it reaches 5.

# %%
for i in range(1, 11):
    if i > 5:
        break
    print(i)


### Continue to Skip
# - Write a loop that prints numbers from 1 to 10 but skips printing the number 5.

# %%
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# %% [markdown] lang="en" tags=["subslide"]
### Challenge: Prime Number Check
# - Define a variable `num` with a positive integer value.
# - Write a loop to check if `num` is a prime number and print `"Prime"` if it is, or `"Not prime"` if it isn't. (Hint: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.)

# %%
num = 11  # Try different numbers
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

# %% [markdown] lang="en" tags=["slide"]
# ## Exercises on Iteration
# - We will cover three exercises that encapsulate the concepts of iteration
# - These exercises range from creating functions, evaluating expressions to approximating mathematical constants
# - The focus will be on developing functions for square root approximation, evaluating expressions, and approximating π
# - We aim to enhance understanding of loops, function encapsulation, and the `eval` function

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 1: Square Root Approximation
# - Develop a function `mysqrt(a)` that estimates the square root of `a`
# - Choose an initial guess for `x` within the function
# - Use the technique from Section 7.5 for approximation
# - Test your function with `test_square_root` to compare against `math.sqrt(a)`
# - Your test should print a table showing `a`, `mysqrt(a)`, `math.sqrt(a)`, and the difference


# %%
def mysqrt(a):
    x = a / 2  # Initial guess for the square root
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


# %%
def test_square_root(start=1, end=10):
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for a in range(start, end + 1):
        mysqrt_a = mysqrt(a)
        math_sqrt_a = math.sqrt(a)
        diff = abs(mysqrt_a - math_sqrt_a)
        print(f"{a:.1f} {mysqrt_a:<13} {math_sqrt_a:<13} {diff}")


# %%
import math

test_square_root()

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 2: Evaluating Expressions with `eval`
# - Create a function `eval_loop` that interactively prompts the user
# - It evaluates user input with `eval` and prints the result
# - The loop ends when the user enters 'done', returning the last evaluated expression
# - This exercise demonstrates the use of `eval` for dynamic expression evaluation


# %%
def eval_loop():
    last_result = None
    while True:
        user_input = input("Enter an expression (or 'done' to exit): ")
        if user_input == "done":
            return last_result
        last_result = eval(user_input)
        print(last_result)


# %%
# Uncomment the following line to test eval_loop, but note that interactive input doesn't work well in Jupyter notebooks directly.
# eval_loop()

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 3: Approximating π with Ramanujan's Formula
# - Implement `estimate_pi` to approximate π using Ramanujan's infinite series
# - Continue adding terms until the last term is less than `1e-15`
# - Compare your approximation with `math.pi`
# - This exercise emphasizes looping for summing a series and the use of conditional loops to achieve precision


# %%
def estimate_pi():
    import math

    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = math.factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term
        if abs(term) < 1e-15:  # Break the loop if the term is less than 1e-15
            break
        k += 1
    return 1 / total


# %%
print(f"Estimated π: {estimate_pi()}")
print(f"math.pi: {math.pi}")

# %% [markdown] lang="en" tags=["slide"]
# Using the template and structure provided in the example, let's create an iteration-focused workshop for a section in a Jupyter notebook.


# %% [markdown] lang="en" tags=["subslide"]
#
# ## Workshop: Iteration (Part 1)
#
# - We will practice the concepts of iteration, which are fundamental to programming in Python.
# - This workshop contains exercises that require you to use loops to solve different problems ranging from numerical computations to processing collections of data.

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise 1: The Power of While Loops
#
# - Write a function named `countdown` that takes an integer `n`.
# - Using a `while` loop, print from `n` down to `1`, followed by `"Liftoff!"`.
# - The function doesn't need to return anything, just print the countdown.


# %% lang="en"
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")


# %% lang="en"
# Uncomment to test your function
# countdown(5)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise 2: Iterating Over Sequences
#
# - Given a list of integers `numbers`, write a function named `sum_odd_numbers` that returns the sum of all odd numbers in the list.
# - Utilize a `for` loop to iterate over the elements in the list.
# - Hint: Remember the modulo operator `%` to check if a number is odd.


# %% lang="en"
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


# %% lang="en"
# Uncomment to test your function with a list of numbers
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_odd_numbers(numbers_list))

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise 3: Fibonacci Sequence
#
# - Write a function called `fibonacci` that takes an integer `n` and prints the first `n` numbers of the Fibonacci sequence.
# - The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it.
# - For example, the first 10 numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
# - Use iteration (loops) in your solution.


# %% lang="en"
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# %% lang="en"
# Uncomment to test your function
# fibonacci(10)

# %% [markdown] lang="en" tags=["subslide"]
#
# - Congratulations on completing the iteration workshop! These exercises aimed to strengthen your understanding of loops in Python, an essential concept for iterative problem-solving in programming.
