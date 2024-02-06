# j2 from 'macros.j2' import header
# {{ header("Interface Design", "Interface Design") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Chapter 4 Case study: interface design
- This chapter presents a case study that demonstrates a process for designing functions that work together.
- It introduces the turtle module, which allows you to create images using turtle graphics.
- The turtle module is included in most Python installations, but might not be available on PythonAnywhere.
- If you have already installed Python on your computer, you should be able to run the examples.
- Code examples from this chapter are available from https://thinkpython.com/code/polygon.py.
# %% [markdown] lang="en" tags=["slide"]
# ## The turtle module
- The `turtle` module allows for the creation and manipulation of turtle objects, which are represented by a small arrow in a window
- To check whether the `turtle` module is installed, open the Python interpreter and type:
    - `import turtle`
    - `bob = turtle.Turtle()`
- This should create a new window with a small arrow that represents the turtle. Close the window.

# %% [markdown] lang="en" tags=["slide"]
# ## Using the turtle module
- Create a file named `mypolygon.py` and type in the following code:
    ```
    import turtle
    bob = turtle.Turtle()
    print(bob)
    turtle.mainloop()
    ```
- When you run this program, it creates a `Turtle` object (represented by the small arrow in a window)
- A `Turtle` object can be moved around the window using various methods, such as `fd` to move forward, `bk` to move backward, `lt` for left turn, and `rt` for right turn
- Each `Turtle` can have its pen either up or down, which determines whether it leaves a trail as it moves

# %% [markdown] lang="en" tags=["slide"]
# ## Drawing with the turtle
- To draw a right angle, add the following lines after creating `bob` and before calling `mainloop`:
    ```
    bob.fd(100)
    bob.lt(90)
    bob.fd(100)
    ```
- This causes the turtle to move east, then north, leaving a trail behind
- Try modifying the program to draw a square before moving on to the next section
# %% [markdown] lang="en" tags=["slide"]
# ## Simple repetition
- You might have written this code to draw a square: 
    - bob.fd(100)
    - bob.lt(90)
    - bob.fd(100)
    - bob.lt(90)
    - bob.fd(100)
    - bob.lt(90)
    - bob.fd(100)
# %% [markdown] lang="en" tags=["slide"]
# ## Simple repetition
- We can use a for statement to do the same thing more concisely:
    - for i in range(4):
        - print('Hello!')
- The output of this loop will be:
    - Hello!
    - Hello!
    - Hello!
    - Hello!
- The for statement has a header that ends with a colon and an indented body. The body can contain any number of statements. A for statement is also called a loop because the flow of execution runs through the body and then loops back to the top. In this case, it runs the body four times.
# %% [markdown] lang="en" tags=["slide"]
# ## Simple repetition
- Here is a for statement that draws a square:
    - for i in range(4):
        - bob.fd(100)
        - bob.lt(90)
- This version is a little different from the previous square-drawing code because it makes another turn after drawing the last side of the square. The extra turn takes more time, but it simplifies the code if we do the same thing every time through the loop. This version also has the effect of leaving the turtle back in the starting position, facing in the starting direction.
# %% [markdown] lang="en" tags=["slide"]
# ## 4.3  Exercises
- The exercises below are meant to be fun and interactive
  - Write and run a function that draws a square using the `turtle` module
  - Add another parameter to the function to modify the length of the sides
  - Make a copy of the square function to create a function that draws a polygon with n sides
  - Write a function that draws an approximate circle using a polygon with an appropriate length and number of sides
  - Generalize the circle function to be able to draw a fraction of a circle by specifying an angle parameter
# %% [markdown] lang="en" tags=["slide"]
# ## Encapsulation
# - Encapsulation is the process of wrapping a piece of code up in a function
# - The benefit of encapsulation includes attaching a name to the code
#   - This serves as a kind of documentation
# - Another advantage is that it makes the code more concise and reusable
# - In the provided exercise, the square-drawing code is encapsulated in a function definition
#   - The function is then called, passing the turtle as a parameter

# %% 
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)

# %% 
alice = turtle.Turtle()
square(alice)
# %% [markdown] lang="en" tags=["slide"]
# ## Generalization
- Adding a parameter to a function is called generalization because it makes the function more general
- In the previous version, the square is always the same size; in this version, it can be any size

# %% 
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
square(bob, 100)

# %% 
# The next step is also a generalization
- Instead of drawing squares, polygon draws regular polygons with any number of sides

# %% 
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 7, 70)

# %% 
# If you are using Python 2, the value of `angle` might be off because of integer division
- A simple solution is to compute `angle = 360.0 / n`

# %% 
# When a function has more than a few numeric arguments, it is often a good idea to include the names of the parameters in the argument list:
- These are called keyword arguments because they include the parameter names as “keywords”
# %% [markdown] lang="en" tags=["slide"]
# ## 4.6  Interface design
- The development section discusses improving the previous solution by incorporating a function `circle` that takes a radius `r` as a parameter
- The first line calculates the circumference of the circle using the formula `2 * math.pi * r`, and hence, `math` is imported
- The function `polygon` is employed here to draw a 50-sided polygon approximating the circle with radius `r`

# %% [markdown] lang="en" tags=["slide"]
# - The limitation with the previous solution is that the number of line segments (`n`) is a constant
- The drawback is that for large circles, the line segments are too long, and for small circles, drawing very small segments leads to waste of time
- A general solution is proposed here to improve the previous function design

# %% [markdown] lang="en" tags=["slide"]
# - The development section discusses adding the number of line segments `n` as a parameter to the function
- The `interface` of a function is summarized here, focusing on the parameters, the functionality, and the return value
- It is emphasized that an interface should be "clean" and allow the caller to perform the desired operation without being burdened with unnecessary details
# %% [markdown] lang="en" tags=["slide"]
# ## Refactoring
- The process of rearranging a program to improve interfaces and facilitate code re-use is called refactoring
- When re-using code, it is important to consider the interface of the original code and how it can be generalized or specialized
- Generalizing or specializing code can often result in the creation of new functions with clearer and more specific interfaces

# %% [markdown] lang="en" tags=["slide"]
# - The function `arc` cannot re-use `polygon` or `circle` to draw an arc
- The function `arc` could be refactored to use a new function `polyline` which is more general and takes an angle as a third argument

# %% [markdown] lang="en" tags=["slide"]
# - The `polyline` function is created to be more general and can be used in `arc` and `polygon` to draw the desired shape
- The `polygon` and `arc` functions are then refactored to use the `polyline` function
- The `circle` function is then refactored to use the `arc` function
- The process of code reorganization and refactoring has improved the interfaces and facilitated code re-use
# %% [markdown] lang="en" tags=["slide"]
# ## A Development Plan
- A development plan is a process for writing programs
- The process used in this case study is "encapsulation and generalization"
- The steps of this process are:
  - Start by writing a small program with no function definitions
  - Once the program is working, identify a coherent piece and encapsulate it in a function
  - Generalize the function by adding appropriate parameters
  - Repeat the above steps until a set of working functions is obtained
- Copy and paste working code to avoid retyping and re-debugging
- Look for opportunities to improve the program by refactoring
- This process can be useful if you don't know ahead of time how to divide the program into functions and lets you design as you go along
# %% [markdown] lang="en" tags=["slide"]
# ## Docstring
- A docstring is a string at the beginning of a function that explains the interface
- It is a triple-quoted string allowing it to span more than one line
- Contains essential information someone would need to use this function
- Explains the function's behavior and the effect of each parameter on it
- Important part of interface design
- A well-designed interface should be simple to explain
# %% [markdown] lang="en" tags=["slide"]
# ## Debugging
- An interface is like a contract between a function and a caller
- Preconditions are the responsibility of the caller
- Violating a (properly documented!) precondition is a bug in the caller, not the function
- If preconditions are satisfied and postconditions are not, the bug is in the function
# %% [markdown] lang="en" tags=["slide"]
# ## Glossary
- method: A function that is associated with an object and called using dot notation
- loop: A part of a program that can run repeatedly
- encapsulation: The process of transforming a sequence of statements into a function definition
- generalization: The process of replacing something unnecessarily specific (like a number) with something appropriately general (like a variable or parameter)
# %% [markdown] lang="en" tags=["slide"]
# ## 4.12 Exercises
- Draw a stack diagram when executing the `circle` function
- A way to reduce the error when drawing an `arc` using linear approximation
- Write functions to draw flowers as in Figure 4.1. Solution: [flower.py](https://thinkpython.com/code/flower.py)
- Write functions to draw shapes as in Figure 4.2. Solution: [pie.py](https://thinkpython.com/code/pie.py)
- Design an alphabet using a minimal number of basic elements and write functions to draw the letters. Solution: [letters.py](https://thinkpython.com/code/letters.py)
- Write a program to draw an Archimedian spiral (or other kinds). Solution: [spiral.py](https://thinkpython.com/code/spiral.py)
