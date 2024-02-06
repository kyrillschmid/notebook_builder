# j2 from 'macros.j2' import header
# {{ header("Functions", "Functions") }}

# %% [markdown] lang="en" tags=["slide"]
# # Chapter 3: Functions
# - In programming, a function is a named sequence of statements that performs a specific computation.
# - When defining a function, we specify its name and the sequence of statements it should execute.
# - Once a function is defined, we can "call" or use it later in the program by referring to its name.

# Here is a code cell:

# %%
# Function definition
def greet():
    print("Hello, World!")

# Calling the function
greet()

# %% [markdown] lang="en" tags=["slide"]
# ## Function Calls
# - Function calls in Python involve a name and a parenthetical expression, the argument of the function
# - Functions "take" an argument and "return" a result or return value
# - Some built-in functions in Python convert values from one type to another, like `int()`, `float()`, and `str()`

# %% [markdown] lang="en" tags=["slide"]
# - The built-in function `int()` takes any value and converts it to an integer:
# - However, it does not round off floating point numbers. It truncates the fraction part

# %%
print(type(42))
print(int('32'))
try:
  print(int('Hello'))
except ValueError:
  print("ValueError: invalid literal for int(): Hello")

# %%
print(int(3.99999))
print(int(-2.3))

# %% [markdown] lang="en" tags=["slide"]
# - The `float()` function, on the other hand, converts integers and strings to floating-point numbers
# - The `str()` function is used to convert its argument to a string 

# %%
print(float(32))
print(float('3.14159'))

# %%
print(str(32))
print(str(3.14159))

# %% [markdown] lang="en" tags=["slide"]
# ## 3.2 Math Functions in Python
# - Python provides a `math` module with many customary mathematical functions.
# - A module is a file that consists of a collection of related functions. 
# - Before using the functions from a module, it is required to import the module using an import statement.
# - When importing a module, a module object is created. The module object contains the functions and variables defined in the module.

# %%
# importing the math module
import math

# %%
# displaying the module object
math

# %% [markdown] lang="en" tags=["slide"]
# - Functions in the modules are accessed by specifying the name of the module and the function, separated by a dot. This is known as dot notation.
# - For instance, the `math.log10` function can be used to compute a signal-to-noise ratio in decibels.
# - The `math.sin` function calculates the sine of a number given in radians.

# %%
# using functions from the math module
signal_power = 10
noise_power = 2
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

# %% [markdown] lang="en" tags=["slide"]
# - To convert degrees to radians, values are divided by 180 and multiplied by π, which can be accessed via `math.pi`.
# - The `math.sqrt(x)` function returns the square root of x. We can use it to check the result of trigonometric calculations. 

# %%
# converting degrees to radians and finding sin of the radian value
degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)

# %%
# using math.sqrt function to check the previous result
math.sqrt(2) / 2.0
# %% [markdown] lang="en" tags=["slide"]
# ## 3.3 Composition
# - Programming languages allow the combination of small building blocks - a feature known as composition
# - Function arguments can be constructed from any kind of expression, including arithmetic operations
# - Expressions can also include function calls

# %% [markdown] lang="en" tags=["slide"]
# - You can put an arbitrary expression anywhere you can put a value, with an exception for the left side of an assignment statement
# - The left side of an assignment statement should always be a variable name
# - Placing any other expression on the left side results in a syntax error

# %%
import math
x = math.sin(degrees / 360.0 * 2 * math.pi)

# %%
x = math.exp(math.log(x+1))

# %%
minutes = hours * 60     # This is correct

# %%
hours * 60 = minutes     # This results in a SyntaxError
# This line causes SyntaxError: can't assign to operator

# %% [markdown] lang="en" tags=["slide"]
# ## 3.4 Adding new functions
# - Python allows us to define new functions.
# - A function definition gives the name of the function and the sequence of statements that run when the function is called.
# - The `def` keyword is used for function definition.
# - The function name should comply with the rules of variable names: consisting of letters, numbers, underscores, but mustn't start with a number.
# - The function name should not be a Python keyword, and should be distinct from any variable names.
# - Empty parentheses after the name indicate that the function doesn't take any arguments.

# %% [markdown] lang="en" tags=["slide"]
# - The first line of the function definition is the header, followed by the body.
# - The header should end with a colon, and the body should be indented by four spaces, as per convention.
# - The body can contain any number of statements.
# - A function's end is marked by an empty line.
# - Once a function is defined, a function object is created, which has a type 'function'.
# - Function can be called in the same way as built-in functions.

# %% 
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# %%
print(print_lyrics)
type(print_lyrics)

# %% [markdown] lang="en" tags=["slide"]
# - One can also define functions within other functions.
# - As an example, the function `repeat_lyrics` has been written to repeat the song lyrics by calling the `print_lyrics` function.

# %%
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# %%
repeat_lyrics()

# %% [markdown] lang="en" tags=["slide"]
# ## 3.5 Definitions and Uses
# - Program containing two function definitions: `print_lyrics` and `repeat_lyrics`
# - Function definitions executed just like other statements, creating function objects
# - Statements inside function don't run until function is called
# - No output generated from function definition

# %% [markdown] lang="en" tags=["slide"]
# - Functions must be created before they can be run
# - Function definition must be executed before function call
# - Exercise: move function call before definitions, observe error
# - Try moving `print_lyrics` definition after `repeat_lyrics` definition, observe results

# %%
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()
    
# %% [markdown] lang="en" tags=["slide"]
# - The above box contains an example with function definition and calls in correct order
# - Experiment by moving the `repeat_lyrics()` call and `print_lyrics` definition around to see what happens

# %%
# repeat_lyrics()   # Uncomment to move this call before function definitions

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
# repeat_lyrics()  # Uncomment to move the function call after definitions

# %%
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()   # Uncomment to move the print_lyrics function below repeat_lyric function

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# repeat_lyrics()  # Uncomment to call the repeat_lyrics function after all definitions are in place
    
# %% [markdown] lang="en" tags=["slide"]
# ## 3.6 Flow of Execution
# - Understanding the order of statement execution - the flow of execution - is crucial to ensure a function is defined before its use
# - Execution commencement always starts from the first statement of the program and run one at a time, top to bottom
# - Function definitions do not alter the main program flow; their internal statements run only when the function is called

# %% [markdown] lang="en" tags=["slide"]
# ## Flow of Execution (contd.)
# - When a function is called, the execution flow takes a detour: it jumps to the function body, executes its contents, and then resumes where it left off
# - This can complicate the flow, especially when one function calls another, leading to nested execution flow deviations
# - Regardless of complexity, Python tracks execution location accurately, always returning where it left off once a function completes

# %% [markdown] lang="en" tags=["slide"]
# ## Flow of Execution (contd.)
# - When the program reaches its end, it terminates
# - Therefore, reading a program does not always follow top to bottom order; sometimes, understanding the flow of execution leads to easier program comprehension# %% [markdown] lang="en" tags=["slide"]
# ## 3.7 Parameters and Arguments
# - Functions can require arguments such as math.sin where a number is passed as an argument.
# - Some functions take more than one arguments, for example math.pow which takes two arguments- the base and the exponent.
# - Inside the function, arguments are assigned to variables, these are known as parameters.
# - Functions can take any kind of expression as an argument, these will be evaluated before the function call.

# %% [markdown] lang="en" tags=["slide"]
# ## Defining a Function with Parameters
# - Below is an example of a function definition that takes an argument:
# - This function assigns the input argument to a parameter named 'bruce'.
# - When this function is called, it prints the value of the parameter twice.
# - This function works with any value that can be printed.

# %%
def print_twice(bruce):
    print(bruce)
    print(bruce)

# %% [markdown] lang="en" tags=["slide"]
# ## Calling a Function with Arguments
# - We can call the function print_twice with a string, number or even a math function as an argument.
# - The expressions passed as arguments will be evaluated only once before the function call.
# - Below are some examples of calling print_twice function with different arguments.

# %%
print_twice('Spam')

# %%
print_twice(42)

# %%
import math
print_twice(math.pi)

# %% [markdown] lang="en" tags=["slide"]
# ## Expressions and Variables as Arguments
# - We can use any kind of expression as an argument for print_twice function.
# - The argument is evaluated before the function is called.
# - We can also use a variable as an argument.
# - The name of the variable passed as argument does not have to match with the name of parameter.

# %%
print_twice('Spam '*4)

# %%
print_twice(math.cos(math.pi))

# %%
michael = 'Eric, the half a bee.'
print_twice(michael)

# %% [markdown] lang="en" tags=["slide"]
# ## 3.8 Variables and parameters are local
# - Variables created inside a function are local, which means they only exist inside the function.
# - For example, in the following function, the variable `cat` is local to the function and is destroyed once the function terminates.
# - If we try to print it outside the function, we get an exception.
# - The same applies for parameters as well. Outside the function, they are not defined.

# %%
#Defining the function
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

# %%
#Using the function
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

# %%
#Trying to print the local variable outside the function
print(cat)
#This will return the NameError: name 'cat' is not defined as 'cat' is a local variable.

# %%
#Parameters are also local.
#For example, in the function 'print_twice', there is no parameter called 'bruce' defined.
#If we try to use 'bruce' somewhere outside the function, we will also get a NameError.Let's transform the given HTML content into a series of Jupyter notebook cells.

# %% [markdown] lang="en" tags=["slide"]
# ## 3.9 Stack Diagrams
# - Stack diagrams are a useful tool to understand which variables can be used in a given context.
# - Besides representing variable values, a stack diagram also shows to which function a variable belongs.
# - Functions are depicted as frames, or boxes containing the function's name, parameters and variables.
# - The sequence of function calls is portrayed by arranging frames in a stack manner.

# %% [markdown] lang="en" tags=["slide"]
# - As an example, if 'print_twice' function was called by 'cat_twice', and 'cat_twice' by '__main__', this sequence will be visually represented in the stack diagram.
# - Variables created outside all functions belong to the '__main__' function.
# - In function calls, each parameter refers to the same value as its corresponding argument.


# %% [markdown] lang="en" tags=["slide"]
# - Python aids error resolution by printing the name of the problematic function, and the names of the functions that called it.
# - The traceback, a list of functions shown when an error occurs, includes details about the error's location and the functions' execution state.
# - The order of functions printed in a traceback corresponds to the order of frames in a stack diagram.

# %%
# example of the error in python which will generate a traceback
def print_twice(cat):
    print(cat)

def cat_twice(line1, line2):
    cat = line1 + line2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)
print_twice() # This will generate an error since we didn't pass any argument to the function

# %% [markdown] lang="en" tags=["slide"]
# ## Fruitful Functions and Void Functions
# - Functions which return results are referred to as 'fruitful functions'
# - Functions which perform an action without returning a value are named 'void functions'
# - When a fruitful function is called, the returned result is usually used in subsequent code
# - If a fruitful function is called without storing the return value, it will be lost

# %%
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

# %% [markdown] lang="en" tags=["slide"]
# ## Using Functions in Interactive Mode
# - In interactive mode, Python will display the results of function calls
# - If a fruitful function is called by itself in a script, the result is not stored or displayed
# - Void functions may have some effect, such as displaying something, but don't return a value
# - If a result of void function is assigned to a variable, the special value `None` is obtained  

# %%
math.sqrt(5)

# %%
result = print_twice('Bing')
print(result)

# %% [markdown] lang="en" tags=["slide"]
# ## None Value in Python
# - The value `None` is not the same as the string 'None'
# - It is a special value having its own type in Python, denoted as `<class 'NoneType'>`
# - Most functions you've written so far are void, but in the upcoming chapters, we will start writing fruitful functions

# %%
type(None)

# %% [markdown] lang="en" tags=["slide"]
# ## 3.11 Why Functions?
# - Functions compartmentalize a program, enhancing its readability and debuggability.
# - Functions enable elimination of repetitive code, leading to more compact and efficient programs.
# - Instead of debugging a lengthy code, breaking it into functions allows debugging in parts.
# - Well-crafted functions can be recycled across multiple programs.

# %% [markdown] lang="en" tags=["slide"]
# ## Benefits of Functions
# - They offer the convenience of grouping statements under a unified name.
# - Code change or adjustments need to be performed only once within the function.
# - Functions simplify long complex codes into manageable parts, aiding efficient debugging.
# - Reusable functions pave the way for efficient coding, particularly for repetitive tasks.# %% [markdown] lang="en" tags=["slide"]
# ## Debugging
# - Debugging, while challenging, is an integral part of programming and a critical skill to develop.
# - Much like detective work or experimental science, debugging involves inferring causes from results and formulating hypotheses to test and draw conclusions.
# - This iterative process necessitates patience and precision, but ultimately leads to more effective and efficient programs.

# %% [markdown] lang="en" tags=["slide"]
# - Programming and debugging are often seen as concurrent processes. Programmers typically start with a working base and iteratively refine it, addressing bugs along the way.
# - For instance, Linux, an OS consisting of millions of lines of code, had humble beginnings as a rudimentary program developed by Linus Torvalds, gradually evolving into its current form through constant debugging and improvements.
# - Hence, the key to an efficient program lies not just in strong foundational coding abilities, but also proficient debugging skills.# %% [markdown] lang="en" tags=["slide"]
# ## Glossary of Python Functions
# - Function: A named sequence of statements that performs an operation, with optional arguments and return results
# - Function definition: A statement to create a function with a specific name, parameters, and contained statements
# - Function object: A value created by a function definition, with the function's name being a reference to the function object

# %% [markdown] lang="en" tags=["slide"]
# ## More Terms Related to Python Functions
# - Header: The inaugural line of a function definition 
# - Body: The sequence of statements contained within a function definition
# - Parameter: An internal name within a function referring to the value passed as an argument

# %% [markdown] lang="en" tags=["slide"]
# ## Working with Python Functions
# - Function call: A statement that triggers a function
# - Argument: The value given to a function during its call, assigned to the corresponding parameter
# - Local variable: A variable defined and usable only within its function

# %% [markdown] lang="en" tags=["slide"]
# ## Return Values and Types of Functions
# - Return value: The function's result; when a function call is used as an expression, this is its value
# - Fruitful function: A function that provides a value
# - Void function: Yields `None`

# %% [markdown] lang="en" tags=["slide"]
# ## Python Modules and Import Statements
# - `None`: A distinct value that void functions return
# - Module: A file comprising of related functions and other definitions
# - Import statement: A statement that reads a module file and generates a module object

# %% [markdown] lang="en" tags=["slide"]
# ## Module Objects and Dot Notation in Python
# - Module object: A value made by an `import` statement, providing access to the values defined in a module
# - Dot notation: Syntax for calling a function from another module, represented as `module_name.function_name`

# %% [markdown] lang="en" tags=["slide"]
# ## Advanced Concepts
# - Composition: Using an expression as a part of a larger expression, or a statement as a part of a larger statement
# - Flow of execution: The order of statement execution
# - Stack diagram: A graphical representation of functions stack including their variables and referenced values

# %% [markdown] lang="en" tags=["slide"]
# ## Execution Tracing and Error Handling
# - Frame: A box in a stack diagram that represents a function call, containing the function's local variables and parameters
# - Traceback: A list of executing functions, printed when an exception occurs# %% [markdown] lang="en" tags=["slide"]
# ## Exercises
# - In this section, you will solve some exercises to test your understanding of functions in Python.
# - Some of these exercises will need additional built-in Python functions like `len` which returns the length of a string.
# - You are tasked to call functions multiple times, pass function objects as arguments, and modify or build upon given function templates.

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 1
# - Write a function named `right_justify` that takes a string `s` as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
# - Hint: Utilize string concatenation and repetition.
# - The Python built-in function `len` returns the length of a string, so `len('monty')` will return 5.

# %%
# Code for Exercise 1

def right_justify(s):
    print(70*' ' + s)

right_justify('monty')

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 2
# - A function object is a value you can assign to a variable or pass as an argument.
# - Here, the `do_twice` function takes a function object as an argument and calls it twice.
# - Now we use `do_twice` to call a function named `print_spam` twice.
# - Next, we will modify `do_twice` to take two arguments: a function object and a value. It should call the function twice, passing the value as an argument.

# %%
# Code for Exercise 2 - part 1

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

# %%
# Code for Exercise 2 - part 2

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print_twice, 'spam')

# %% [markdown] lang="en" tags=["slide"]
# ## Continued Exercise 2 & Exercise 3
# - Define a function `do_four` that takes a function object and a value as arguments.
# - It should call the given function four times, passing the value as a parameter. The function should ideally contain only two statements.
# - In the third exercise, write a function that draws a grid.
# - Hint: To print more than one value on a line, a comma-separated sequence of values can be used.
# - The default behavior of `print` advancing to the next line can be overridden to put a space at the end.

# %%
# Code for Exercise 2 - part 3
def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)
    
# Call the function
do_four(print_twice, 'spam')

# %%
# Code for Exercise 3X
def draw_grid_row():
    print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

def draw_grid_col():
    print('|', ' '*5, '|', ' '*5, '|')

def draw_grid():
    draw_grid_row()
    draw_grid_col()
    draw_grid_col()
    draw_grid_col()
    draw_grid_col()
    draw_grid_row()
    draw_grid_col()
    draw_grid_col()
    draw_grid_col()
    draw_grid_col()
    draw_grid_row()

draw_grid()