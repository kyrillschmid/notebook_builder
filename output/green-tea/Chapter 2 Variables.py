# j2 from 'macros.j2' import header
# {{ header("Variables, expressions and statements", "Variables, expressions and statements") }}

# %% [markdown] lang="en" tags=["slide"]
# # Chapter 2: Variables, expressions and statements
# - A key feature of programming languages is the ability to manipulate variables
# - In Python, a variable is a name assigned to a value
# Note: Here, variable is a storage location that contains some data (a value), and a name (an identifier) is assigned to it. You can think of it like a label to a storage box in your computer memory, where you put a value. You can assign values, change values, and retrieve values from these storage locations using the variable's name.


# %% [markdown] lang="en" tags=["slide"]
# ## 2.1 Assignment Statements
# - Assignment statements create and assign a value to a new variable
# - Example: defining a string variable named 'message', an integer 'n' and a floating-point number 'pi'
# - Variables can be visualized using a state diagram showing the state of each variable i.e., its current value

# %%
# Assigning values to variables
message = "And now for something completely different"
n = 17
pi = 3.1415926535897932

# %% [markdown] lang="en" tags=["slide"]
# - This example illustrates three assignments:
#   - First, a string is assigned to a new variable "message"
#   - Second, an integer "17" is assigned to a variable "n"
#   - Third, the approximate value of π is assigned to the variable "pi"

# %%
# Check the values of the variables
print(f"Message: {message}")
print(f"Value of n: {n}")
print(f"Value of pi: {pi}")

# %% [markdown] lang="en" tags=["slide"]
# ## 2.2  Variable names
# - Variable names should be meaningful to document their use.
# - They can include both letters and numbers, but must not start with a number.
# - While uppercase letters are allowed, using only lower case letters is conventional.
# - Underscore (_) is often used in multi-word variable names (e.g., your_name, airspeed_of_unladen_swallow).
# - If a variable has an illegal name, a syntax error will be returned.

# %%
# This is erroneous code and will throw a SyntaxError when run
# 76trombones = 'big parade'
# more@ = 1000000
# class = 'Advanced Theoretical Zymurgy'

# %% [markdown] lang="en" tags=["slide"]
# - 76trombones is illegal because it begins with a number.
# - more@ is illegal because it contains an illegal character, @.
# - 'class' is illegal because it's one of Python's keywords.
# - Keywords are reserved and recognized by the Python interpreter for program structure; they cannot be used as variable names.

# %%
# Keywords in Python
# False, class, finally, is, return
# None, continue, for, lambda, try
# True, def, from, nonlocal, while
# and, del, global, not, with
# as, elif, if, or, yield
# assert, else, import, pass
# break, except, in, raise

# %% [markdown] lang="en" tags=["slide"]
# - Python 3 has a list of reserved keywords.
# - These reserved words can't be used as variable names, as they are required for their own specific functions within Python's language structure.
# - There's no need to memorize this list; most development environments will highlight them differently to ensure you're aware they're keywords.
# %% [markdown] lang="en" tags=["slide"]
# ## 2.3  Expressions and Statements in Python
# - An expression is a combination of values, variables, and operators.
# - A value or a variable itself can be an expression. They can be evaluated to find their values.
# - Statement is a unit of code that performs an action, like assigning a value to a variable or printing a value.
# - Statements are executed by the interpreter, performing the actions they are intended to do.

# %%
# Evaluating expressions
value = 42
print(value)

n = 17
print(n)

result = n + 25
print(result)

# %%
# Example of statements
n = 17
print(n)
# %% [markdown] lang="en" tags=["slide"]
# ## Script mode in Python
# - Python can be run in two modes: **interactive mode** and **script mode**
#     - In interactive mode, you interact directly with the interpreter - ideal for small snippets.
#     - In script mode, you write your code in a file known as a script (ending in .py) and then execute the script.
# - In script mode, simply writing an expression doesn't provide any visible output. One must use the `print` statement.

# %% [markdown] lang="en" tags=["slide"]
# ## Interactive vs Script Mode
# - There are subtle differences between interactive and script mode.
# - For instance, when using Python as a calculator, execution behaves differently in both modes. Let's see an example.

# %%
# Interactive Mode
miles = 26.2
miles * 1.61

# %% [markdown] lang="en" tags=["slide"]
# - In the interactive mode, the above code will display the result of the expression `miles * 1.61`.
# - However, in script mode, just writing the expression won't output anything.
# - To get a visible output, we need to use the `print` statement.

# %%
# Script Mode
miles = 26.2
print(miles * 1.61)

# %% [markdown] lang="en" tags=["slide"]
# ## Experiment with Interactive and Script Mode
# - To better understand the difference between the two modes, try running the following statements in both interactive and script mode.
# - Observe the difference in their results.

# %%
# Test in Interactive Mode
5
x = 5
x + 1

# %%
# Test in Script Mode
print(5)
x = 5
print(x + 1)
# %% [markdown] lang="en" tags=["slide"]
# ## 2.5  Order of Operations
# - When multiple operators are used, their order of evaluation is guided by Python's predefined rules, reflecting mathematical norms.
# - The order of precedence can be remembered utilizing the acronym PEMDAS:
#   - Parentheses (for grouping expressions)
#   - Exponentiation (power operation)
#   - Multiplication and Division
#   - Addition and Subtraction
# - Operators sharing precedence are evaluated from left to right.

# %% [markdown] lang="en" tags=["slide"]
# ## Order of Operations (cont.)
# - Parentheses have the utmost priority leading to expressions enclosed in them to be evaluated first. For example, `2 * (3-1)` equals 4.
# - Exponentiation has next highest precedence, so `1 + 2**3` yields 9.
# - Multiplication and Division are more prioritized than Addition and Subtraction as `2*3-1` is 5, not 4.
# - Creating complex expressions with unknown operator precedence is enhanced by using parentheses for clarity.

# %%
# Parentheses (highest precedence)
print(2 * (3 - 1))  # output should be 4
print((1 + 1) ** (5 - 2))  # output should be 8
# Exponentiation (next highest precedence)
print(1 + 2**3)  # output should be 9
print(2 * 3**2)  # output should be 18
# Multiplication and Division (higher precedence than Addition and Subtraction)
print(2 * 3 - 1)  # output should be 5
print(6 + 4 / 2)  # output should be 8
# Use of parentheses for clarity in expressions
degree = 30
pi = 3.14
print(degree / 2 * pi)  # without parentheses
print(degree / (2 * pi))  # with parentheses for clarity
# %% [markdown] lang="en" tags=["slide"]
# ## 2.6 String Operations
# - Mathematical operations can't generally be performed on strings.
# - However, `+` and `*` operators are exceptions to this rule.
# - The `+` operator can perform string concatenation by linking strings end-to-end.
# - The `*` operator performs string repetition, where one value is a string and the other has to be an integer.

# %%
# Illegal operations on strings
try:
    "chinese" - "food"
except:
    print("This operation is illegal")

try:
    "eggs" / "easy"
except:
    print("This operation is illegal")

try:
    "third" * "a charm"
except:
    print("This operation is illegal")

# %% [markdown] lang="en" tags=["slide"]
# ## String Concatenation and Repetition
# - For example, string concatenation can be performed as follows:
#    ```
#    first = 'throat'
#    second = 'warbler'
#    first + second
#    ```
# - String repetition can be performed as follows: `'Spam' * 3` outputs `'SpamSpamSpam'`.
# - Just like `4*3` is equivalent to `4+4+4`, `'Spam'*3` is the same as `'Spam'+'Spam'+'Spam'`.
# - However, string concatenation and repetition are different from integer addition and multiplication in significant ways.

# %%
# String concatenation
first = "throat"
second = "warbler"
print(first + second)

# String repetition
print("Spam" * 3)
# %% [markdown] lang="en" tags=["slide"]
# ## 2.7 Comments
# - As programs increase in size and complexity, they become harder to read.
# - Using comments in your code can help clarify its purpose and functionality.
# - Comments, starting with the '#' symbol, are notes in natural language explaining what the program is doing.
# - These are not executed as part of the program.

# %%
# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60

# %% [markdown] lang="en" tags=["slide"]
# ## Comments Continued
# - Comments can be on a line by themselves or they can be at the end of a line.
# - Any text from '#' to the end of the line is ignored by the Python interpreter.
# - It's useful to use comments to document non-obvious parts of the code.

# %%
percentage = (minute * 100) / 60  # percentage of an hour

# %% [markdown] lang="en" tags=["slide"]
# ## Effective Commenting
# - The real value in comments is not for explaining what the code is doing, but why.
# - Avoid using comments for obvious information: `v = 5  # assign 5 to v` is an unnecessary comment.
# - Instead, use them for non-obvious information: `v = 5  # velocity in meters/second.`

# %%
v = 5  # velocity in meters/second.

# %% [markdown] lang="en" tags=["slide"]
# ## Variable Names and Comments
# - Good variable names can reduce the need for comments.
# - Long variable names can make complex expressions hard to read, so there needs to be a balance.
# - Striking a balance between variable name length and use of comments contributes to the readability of your code.
# %% [markdown] lang="en" tags=["slide"]
# ## 2.8 Debugging
# - Three kinds of errors can occur in a program: syntax errors, runtime errors, and semantic errors.
# - Distinguishing between these error types can help in debugging them more efficiently.

# %% [markdown] lang="en" tags=["slide"]
# ## Syntax Errors
# - Syntax refers to the structure of a program and the rules about that structure.
# - If there is a syntax error anywhere in your program, Python will display an error message and quit.
# - With time and experience, syntax errors will reduce and can be identified faster.

# %% [markdown] lang="en" tags=["slide"]
# ## Runtime Errors
# - Runtime errors, also called exceptions, do not appear until after the program has started running.
# - These errors usually indicate something exceptional (and bad) has happened.
# - Runtime errors are rare in simple programs but become more prevalent as programs get complex.

# %% [markdown] lang="en" tags=["slide"]
# ## Semantic Errors
# - Semantic errors are related to meaning.
# - If there is a semantic error in your program, it will run without generating error messages, but it will not do the right thing.
# - Identifying semantic errors can be tricky because it requires you to analyze the output of the program and figure out what it is doing.

# %% [markdown] lang="en" tags=["slide"]
# ## Section 2.9: Glossary
# - Variable: It is a named reference to a value in a program.
# - Assignment: This is a statement that allocates a value to a variable.
# - State Diagram: This graphical illustration indicates a set of variables alongside their corresponding values.
# - Keyword: These are reserved words employed in parsing a program. Python's keywords include `if`, `def`, and `while`. They cannot be used as variable names.

# %% [markdown] lang="en" tags=["slide"]
# - Operand: This refers to the values an operator works on.
# - Expression: This is a combination of variables, operators, and values representing a single result.
# - Evaluate: This involves simplifying an expression by undertaking operations to yield a singular result value.
# - Statement: This represents a command or an action in a code segment. So far, we have encountered assignment and print statements.

# %% [markdown] lang="en" tags=["slide"]
# - Execute: This involves running a statement to perform its represented action.
# - Interactive Mode: This is a method for utilizing Python by typing code directly at the prompt.
# - Script Mode: This is another method of utilizing Python, where the program is read from a script and executed.
# - Script: A script is a saved program in a file.

# %% [markdown] lang="en" tags=["slide"]
# - Order of Operations: These rules determine the sequence in which expressions with multiple operators and operands are evaluated.
# - Concatenate: This process involves connecting two operands sequentially, end-to-end.
# - Comment: Comments are informational content in a program for other programmers or anyone reviewing the source code. These have no impact on program execution.

# %% [markdown] lang="en" tags=["slide"]
# - Syntax Error: This program error prevents it from being parsed and hence interpreted.
# - Exception: This type of error is detected during the runtime of the program.
# - Semantics: This refers to the meaning or intended purpose of a program.
# - Semantic Error: This occurs when a program error causes it to deviate from what the programmer intended it to do.
# %% [markdown] lang="en" tags=["slide"]
# ## 2.10 Exercises
# - Reading documentation and making intentional mistakes can help understanding new Python features better
# - Perform the following Python operations and observe the outcome:
#   - Try to assign a number to a number. For example, try `42 = n`
#   - Assign a single value to multiple variables together, like `x = y = 1`
#   - Implement a Python statement ending with a semi-colon
#   - Implement a Python statement ending with a period
#   - Try to multiply two variables using a whitespace as in math notation, like `x y`

# %% [markdown] lang="en" tags=["slide"]
# ## Practical Exercises
# - Use Python interpreter as a calculator to solve following problems:
#   - Compute the volume of a sphere with radius 5. Formula for volume of sphere: 4/3 πr³
#   - Calculate the total wholesale cost for 60 books given the cover price of a book is $24.95, bookstores get a discount of 40%, shipping costs $3 for the first copy and 75 cents for each additional copy
#   - Assuming you leave home at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile), and 1 mile at easy pace again, work out the time you get home for breakfast

# %% code cells for Exercise 1
# placeholder for participants to try the operations

# %%
# %% code cells for Practical Exercises
# placeholder for participants to solve problems
