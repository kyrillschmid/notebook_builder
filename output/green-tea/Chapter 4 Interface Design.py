# j2 from 'macros.j2' import header
# {{ header("Interface Design", "Interface Design") }}

# %% [markdown] lang="en" tags=["slide"]
# # Chapter 4  Case Study: Interface Design
# - This chapter presents a case study focusing on designing functions that work together.
# - It introduces the `turtle` module, which helps in creating images using turtle graphics.
# - `turtle` module is included in most Python installations, but may not be available if running Python using PythonAnywhere.
# - If Python is already installed on your computer, running the examples should be possible. However, if not done yet, this is a good time for installation.

# %% [markdown] lang="en" tags=["slide"]
# - Instructions are provided on the site [http://tinyurl.com/thinkpython2e](http://tinyurl.com/thinkpython2e) for installation. 
# - Code examples can be accessed from the site: [https://thinkpython.com/code/polygon.py](https://thinkpython.com/code/polygon.py).
# - This chapter involves practical examples and exercises, which require use of the `turtle` module.
# - These applications allow for practice of newly introduced concepts and will foster better understanding. 

# %% [markdown] lang="en" tags=["slide"]
# ## Installation of Turtle Module
# - If you are working on a local Python environment, you might have the Turtle module pre-installed. 
# - However, you can check for same with command: `import turtle`.
# - If module is missing, install it using pip: `pip install PythonTurtle` or with conda if you are using anaconda distribution: `conda install -c conda-forge python-turtle`. 

# %% [markdown] lang="en" tags=["slide"]
# ## Checking for Module and Installation
# - If you have Python installed locally, try importing the Turtle module.
# - If it's not available, you might have to install it.

# %%
# Try importing the Turtle module
try: 
    import turtle
    print("Module 'turtle' is installed.")
except ImportError:
    print("Module 'turtle' is not installed.") 

# %%
# If it is not installed, then you might have to install it. You can use following command for the same,
# !pip install PythonTurtle

# Note: Uncomment the above line to install the module. Also, if you are using Jupyter notebook, you might need to restart the kernel.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.1 The turtle module
# - To check if the turtle module is present, we can try importing it.
# - A Turtle object can be created using the turtle.Turtle() function.
# - This turtle object moves within a dedicated window, and can be controlled through method calls.
# - The turtle.mainloop() function makes the window wait for user interaction.

# %%
# Importing turtle module and creating a Turtle object
import turtle
bob = turtle.Turtle()

# %% [markdown] lang="en" tags=["slide"]
# ## Working with the Turtle Object
# - Printing our Turtle object would display a statement revealing it as a Turtle-type object within the turtle module. 
# - Turtle objects have methods to manipulate their movement such as fd (forward), bk (backward), lt (left turn), and rt (right turn).
# - The "fd" method moves the Turtle forward by a distance specified in pixels.
# - The methods "lt" and "rt" make the Turtle turn to the left or right by the specified number of degrees.
# - The functionality can be extended to drawing geometric shapes like squares.

# %%
# Printing our Turtle object
print(bob)

# Mainloop function
turtle.mainloop()

# %% [markdown] lang="en" tags=["slide"]
# ## Managing the Turtle's Pen
# - The Turtle "holds" a pen which can be either up or down. 
# - If the pen is down, the Turtle leaves a trail as it moves.
# - The methods "pu" and "pd" can be used to lift the pen up or put it down, respectively. 
# - We can use these methods along with the movement methods to make our Turtle draw a right angle.

# %%
# Directing our Turtle object to move and create a right angle.
bob.fd(100)
bob.lt(90)
bob.fd(100)

# %% [markdown] lang="en" tags=["slide"]
# ## Turtle Exercise
# - Try modifying the program to command the Turtle to draw a square.
# - Note: Before proceeding, make sure your program works correctly and the Turtle draws a square.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.2 Simple Repetition
# - A simple sequence of commands can be executed in a more concise way using a `for` statement.
# - The `for` statement has a header ending with a colon and an indented body.
# - The body can contain any number of statements.
# - A `for` statement is also known as a loop as the flow of execution goes through the body and then loops back to the top.

# %% 
bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)

# %% [markdown] lang="en" tags=["slide"]
# - The `for` statement is used to run a block of code a specific number of times.
# - Example: When `for i in range(4):    print('Hello!')` is executed, 'Hello!' is printed 4 times.
# - The resulting output illustrates the operation of the previous `for` loop.
# - After writing a square-drawing program, it can be simplified with a `for` loop.

# %% 
for i in range(4):
    print('Hello!')

# %% 
Hello!
Hello!
Hello!
Hello!

# %% [markdown] lang="en" tags=["slide"]
# - The `for` loop can be used to draw shapes, as shown in the example of drawing a square.
# - At the end of each iteration, add a turn to simplify the loop and to make the result more predictable.
# - While the additional turn does consume more time, it simplifies the loop by ensuring the same actions occur in each iteration.
# - After the final side of the square is drawn, the turtle ends up in the starting position, facing the original direction.

# %%
for i in range(4):
    bob.fd(100)
    bob.lt(90)
# %% [markdown] lang="en" tags=["slide"]
# ## Exercises with 'turtle' module 
# - This exercise involves a series of tasks using 'turtle' module in Python.
# - While performing these tasks, remember the underlying principles behind each step.
# - Exercise solutions are provided ahead. Only check them after trying your best.

# %% [markdown] lang="en" tags=["slide"]
# ## Task 1: Function 'square'
# - Write a function 'square' that takes a parameter 't', which is a turtle. 
# - Use the turtle "t" to draw a square.
# - Call the function using 'bob' as an argument.

# %%
# code for Task 1 goes here

# %% [markdown] lang="en" tags=["slide"]
# ## Task 2: Function 'square' with added parameter
# - Add another parameter to function 'square', named 'length'.
# - Modify the function so that it draws a square of side length 'length'.
# - Run the function again with the added argument.
# - Test your function with different values of 'length'.

# %%
# code for Task 2 goes here

# %% [markdown] lang="en" tags=["slide"]
# ## Task 3: Function 'polygon'
# - Copy function 'square' and rename it to 'polygon'.
# - Add another parameter 'n' and modify the function so it draws an n-sided regular polygon.
# - Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

# %%
# code for Task 3 goes here

# %% [markdown] lang="en" tags=["slide"]
# ## Task 4: Function 'circle'
# - Write a function 'circle' that takes a turtle 't', and radius 'r', as parameters.
# - This function should draw an approximate circle by making suited calls to the 'polygon' function.
# - Test your function with a variety of radius values.
# - Hint: Determine the circumference of the circle and ensure that length * n equals the circumference.

# %%
# code for Task 4 goes here

# %% [markdown] lang="en" tags=["slide"]
# ## Task 5: Function 'arc'
# - Make a more general function of 'circle' called 'arc'.
# - 'Arc' should take an additional parameter 'angle', which determines the fraction of a circle to draw.
# - Angle is in units of degrees, hence, when angle = 360, 'arc' should draw a complete circle.

# %%
# code for Task 5 goes here
# %% [markdown] lang="en" tags=["slide"]
# ## 4.4 Encapsulation
# - Encapsulation involves wrapping a piece of code inside a function.
# - This technique has several advantages, such as giving the code a specific name which serves as documentation.
# - Encapsulated code can be re-used easily by calling the function, which is more concise than copying and pasting the same code block.
# - One exercise example is creating a function for drawing a square and then calling this function.

# %%
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
# %%
square(bob)

# %% [markdown] lang="en" tags=["slide"]
# - The function `square` takes a parameter `t`, which refers to a turtle object, and uses it to draw a square.
# - The inner statements `t.fd(100)` and `t.lt(90)` are indented twice, showing they are inside both the for loop and the function definition.
# - After defining and invoking the function with an argument, the next line of code is flush with the left margin, indicating the end of both the for loop and function definition.
# - The parameter `t` can represent any turtle, not just `bob`. This is demonstrated by creating a second turtle `alice` and passing it as an argument to `square`.

# %%
alice = turtle.Turtle()

# %%
square(alice)
# %% [markdown] lang="en" tags=["slide"]
# ## 4.5 Generalization
# - Generalization involves adding parameters to a function to make it more versatile.
# - For instance, adding a length parameter to the square function allows it to draw squares of any size.
# - The next step, involves expanding the function to draw regular polygons of any number of sides.

# %%
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 100)

# %% [markdown] lang="en" tags=["slide"]
# - The parameterized polygon function can now draw an n-sided polygon, with sides of a specified length.
# - For Python 2 users, make sure to compute the angle as `360.0 / n` to ensure a floating point result.
# - More complex functions with various numeric arguments can be made more readable through the use of keyword arguments.

# %%
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 7, 70)

# %%
polygon(bob, n=7, length=70)
# %% [markdown] lang="en" tags=["slide"]
# ## 4.6  Interface Design
# - To implement the concept of interface design, a function for drawing a circle called `circle` is created.
# - This function takes a radius `r` as a parameter and utilizes the `polygon` function to craft its circle via the approximation of a 50-sided polygon.
# - One potential limitation to this approach is the static use of `n` as the number of segments, which could result in inefficiency with very small or very large circles.
# - This would be improved by allowing `n` to be a user input parameter, helping the user to better control the number of segments based on the size of the circle they are working with.

# %% 
import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

# %% [markdown] lang="en" tags=["slide"]
# - Function interfaces form an integral part of how to interact with the function, providing essential information about the function's parameters, what the function does, and what it returns.
# - A "clean" interface provides the user all the necessary information and control they need while sparing them from unnecessary details.
# - In our `circle` function example, the radius `r` forms part of the interface since it specifies the circle to be drawn. However, `n` is less suitable since it's related to the manner of circle rendering, not its attributes.
# - Hence, instead of letting the user manually define `n`, we come up with a suitable value for `n` based on the circle's circumference.

# %%
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

# %% [markdown] lang="en" tags=["slide"]
# - With the above adapted `circle` function, the number of segments is set as an integer near `circumference/3`.
# - This ensures each segment length is approximately 3 units, striking a good balance between visibility and efficiency.
# - This approach is also adaptive, changing based on the size of the circle.
# - Furthermore, by adding 3 to `n`, we ensure that our polygon will always have at least 3 sides.

# %% [markdown] lang="en" tags=["slide"]
# ## 4.7 Refactoring 
# - Refactoring is the process of rearranging a program to improve interfaces and facilitate code reuse. 
# - It can be useful when we notice similar code in different parts of our program. 
# - In the given scenario, we see that 'arc' and 'polygon' have similar code components, that can be "factored out" into 'polyline'
# - The process requires rewriting parts of the code with the aim of generalization for better reusability.

# %% [markdown] lang="en"] tags=["slide"]
# ## Refactoring `arc` function
# - The function `arc` could not be written by reusing the existing `circle` or `polygon` functions.
# - One of the approaches could be to modify the `polygon` function into `arc`.
# - However, to maintain the appropriate naming, a new generalized function, `polyline` is created for reuse

# %% 
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# %% [markdown] lang="en"] tags=["slide"]
# ## Introduction of `polyline` 
# - The function `polyline` is a more generalized version of the function `polygon`.
# - The `polyline` function takes an additional argument, `angle`, compared to the `polygon` function.

# %% 
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# %% [markdown] lang="en"] tags=["slide"]
# ## Reusing `polyline` in `polygon` and `arc` 
# - Both `polygon` and `arc` functions can be rewritten to use `polyline`
# - This generalization allows for better reusability of the code

# %% 
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

# %% [markdown] lang="en"] tags=["slide"]
# ## Refactoring `circle` to use `arc`
# - The function `circle` can be rewritten to utilise the function `arc`
# - Refactoring in this fashion improves the overall coding standard, making it easier to understand and maintain 

# %% 
def circle(t, r):
    arc(t, r, 360)

# %% [markdown] lang="en"] tags=["slide"]
# ## Learning through Refactoring
# - Refactoring often occurs when you realize ways to optimize or better structure your code as you're writing it. 
# - Sometimes, it indicates that you've learned something new as you're coding. 
# - It is not always possible to plan ahead for every interface at the beginning of a project, the understanding improves as we delve deeper into the coding phase.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.8 A Development Plan
# - A development plan is a systematic approach to writing programs.
# - The methodology used in the current study is "Encapsulation and Generalization".
# - This methodology involves a series of steps to guide the development of your program.

# %% [markdown] lang="en" tags=["slide"]
# ## Encapsulation and Generalization Steps
# - Begin by crafting a simple program with no function definitions.
# - Once the program is operational, identify a coherent segment, encapsulate it as a distinct function, and assign it a name.
# - Generalize the function with relevant parameters.
# - Repeat the previous steps until there's a collection of performing functions.

# %% [markdown] lang="en" tags=["slide"]
# ## Code Refactoring and Improvement
# - To avoid retyping and potential debugging, repurpose working code as much as possible.
# - Constantly look out for opportunities to enhance the program through refactoring.
#   - For instance, if similar code occurs in multiple areas, think about abstracting it into a suitably general function.
# - This process may have some shortcomings but can be helpful if there's initial uncertainty about how to partition the program into distinct functions.
# - This strategy allows for progressive design over time.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.9 Docstrings 
# - A docstring is a triple-quoted string placed at the beginning of a function to explain its interface.
# - The docstring offers a brief explanation of what the function does, its parameters and their effects, and parameter types.
# - Interface design benefits greatly from informative docstrings.
# - A well-written, concise docstring can be an indicator of a well-designed interface.

# %% 
def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# %% [markdown] lang="en" tags=["slide"]
# - The provided code demonstrates a docstring in a function called polyline.
# - Docstrings are typically multiline strings; they can span more than one line.
# - If explaining a function through its docstring becomes challenging, it indicates that the function interface may need improvement.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.10  Debugging
# - An interface can be perceived as a contract between a function and a caller, defining preconditions and postconditions .
#    - Preconditions: Given conditions or parameters that must hold true before a function begins execution.
#    - Postconditions: Expected outcome at the end of the function's execution. These include the function's intended effects and any side effects.
# - Preconditions are the caller's responsibility. If the preconditions are violated and the function fails, the error lies with the caller, not the function.
# - If the preconditions are met, but the postconditions aren't, the error lies in the function.
# - Clearly stating pre- and post-conditions helps in debugging. 

# An example of a function precondition could be that the function `polyline` requires four arguments:
# - `t` has to be a Turtle
# - `n` has to be an integer
# - `length` should be a positive number
# - `angle` has to be a number, which is understood to be in degrees. 

# The postconditions for the function `polyline` might include drawing line segments, moving the Turtle, or making other changes. 

# %% [markdown] lang="en" tags=["slide"]
# - In the following section we will give an example of the function `polyline`.
# - This example is not meant for execution, its purpose is to clarify the concept of preconditions and postconditions.

# %% 
# This is an example and is not meant for execution
def polyline(t, n, length, angle):
    """
    Preconditions:
    - t: has to be a Turtle instance
    - n: an integer value representing the number of line segments
    - length: a positive number denoting length of each segment
    - angle: a number representing the angle (in degrees) of each turn

    Postconditions:
    - Draws n line segments with the given length and angle
    - The final position of Turtle instance t may change
    """
    for _ in range(n):
        t.forward(length)
        t.right(angle) 
# This example does not run as we do not define an instance of Turtle 't'. This is merely to demonstrate the concept of preconditions and postconditions.
# In real use-cases, make sure the precondtions are satisfied before calling a function. If the function doesn't deliver the 
# expected outcomes i.e., postconditions, despite the preconditions being met, the bug lies in the function block itself.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.11 Glossary
# - Method: A function tied to an object, accessible through dot notation.
# - Loop: A block of code set to execute repeatedly in a program.
# - Encapsulation: The task of converting a series of statements into a function definition.
# - Generalization: The practice of replacing specific elements (like a number) with general ones (like a variable or parameter).

# %% [markdown] lang="en" tags=["slide"]
# ## 4.11 Glossary (Continued)
# - Keyword argument: An argument that incorporates the parameter's name as a “keyword”.
# - Interface: Detailed instructions on how to utilize a function, that includes the function's name, arguments, and return value.
# - Refactoring: Tweaking a functioning program to enhance its function interfaces, and other elements. 
# - Development plan: A strategy for writing programs.

# %% [markdown] lang="en" tags=["slide"]
# ## 4.11 Glossary (Continuation)
# - Docstring: A string that is stationed at the beginning of a function definition to document the function’s interface.
# - Precondition: A requirement that must be met by the caller before a function begins execution.
# - Postcondition: A condition that must be met by the function before it concludes.
# %% [markdown] lang="en" tags=["slide"]
# ## Exercises

# - To understand the state of program while executing `circle(bob, radius)`, draw a stack diagram or use print statements in the code.
# - As the version of `arc` from section 4.7 may not be accurate in creating the circle, we try to reduce the error's impact in our solution. Try to read the code to understand. Drawing a diagram might help.

# %%
# Required library and function
# import thinkpython.com/code/polygon.py
# circle(bob, radius)

# %% [markdown] lang="en" tags=["slide"]
# ## Exercises

# - Create a function to draw flowers as in Figure 4.1.
# - Create a function to draw shapes as in Figure 4.2.
# - Try designing an alphabet using basic elements like vertical and horizontal lines and a couple of curves. Each letter should be a function.

# %%
# Exercise 2 Solution 
# URL provided for reference purpose only, It may not work in Jupyter cell
# import thinkpython.com/code/flower.py
# import polygon.py

# %%
# Exercise 3 Solution 
# URL provided for reference purpose only, It may not work in Jupyter cell
# import thinkpython.com/code/pie.py

# %%
# Exercise 4 Solution 
# Follow the pseudocode below,
# create letters in a file namedletters.py
# Test your code using turtle typewriter
# import thinkpython.com/code/typewriter.py

# %% [markdown] lang="en" tags=["slide"]
# ## Exercises
# - Explore about spirals at http://en.wikipedia.org/wiki/Spiral
# - Write a program that can draw an Archimedian spiral or any other kind of spirals

# %%
# Exercise 5 Solution 
# URL provided for reference purpose only, It may not work in Jupyter cell
# import thinkpython.com/code/spiral.py
