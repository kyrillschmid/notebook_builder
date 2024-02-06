# %% [markdown] lang="en" tags=["slide"]
#
# ## Mini-Workshop: The first program

# %% [markdown] lang="de" tags=["slide"]
# ## Mini-Workshop: Das erste Programm

# %% [markdown] lang="en" tags=["subslide"]
#
# The tradition in learning a new programming language is to start with a simple program that prints "Hello, World!" to the screen. This task helps you become familiar with the basic syntax of the language for printing text to the console.

# %% [markdown] lang="de" tags=["subslide"]
# Die Tradition beim Erlernen einer neuen Programmiersprache ist es, mit einem einfachen Programm zu beginnen, das "Hallo Welt!" auf den Bildschirm druckt. Diese Aufgabe hilft Ihnen, mit der grundlegenden Syntax der Sprache für die Ausgabe von Text in der Konsole vertraut zu werden.

# %% [markdown]
# Write a function called `hello_world()` that prints "Hello, World!" to the screen.


# %%
def hello_world():
    print("Hello, World!")


# %% [markdown] tags=["subslide"]
#
# Now, call the function `hello_world()` to print "Hello, World!".

# %%
hello_world()

# %% [markdown] tags=["subslide"]
#
# ### Examining the Hello, World! program
#
# - The quotation marks define a string that is passed as an argument to the `print()` function.
# - The `print()` function displays the string on the screen.
#
# Let’s enhance our function. Modify `hello_world()` so that it takes a parameter `name` and prints "Hello, `name`!" where `name` is the value of the parameter. Provide a default value of "World" for `name`.


# %%
def hello_world(name="World"):
    print(f"Hello, {name}!")


# %% [markdown] tags=["subslide"]
#
# Test the enhanced `hello_world()` function by:
#
# 1. Calling it without arguments.
# 2. Calling it with your name as the argument.

# %%
hello_world()
hello_world("Alice")

# %% [markdown] tags=["subslide"]
#
# **Congratulations!** You’ve successfully created and modified your first Python program. This exercise demonstrated the basic structure of a Python program and introduced you to the `print()` function and string manipulation. As you continue learning Python, you'll build upon these foundational concepts to create more complex and powerful programs.
