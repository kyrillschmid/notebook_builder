# %% [markdown] lang="en" tags=["slide"]
#
# # Mini-Workshop: Introduction to Programming

# %% [markdown] lang="en"
#
# The goal of this mini-workshop is to introduce you to the idea of thinking like a computer scientist, which involves understanding how to approach problem solving in a systematic and logical manner. We'll start with a basic exercise that gives you a taste of programming and problem-solving.

# %% [markdown] lang="en" tags=["slide"]
#
# Write a function `greet(name)` that prints a greeting to the screen. The function should take a string `name` as an argument and print the message `"Hello, {name}! Welcome to the world of Python!"`.


# %%
def greet(name):
    print(f"Hello, {name}! Welcome to the world of Python!")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test the function `greet(name)` with your name and observe the output.

# %%
greet("Alice")

# %% [markdown] lang="en" tags=["subslide"]
#
# Problem solving involves breaking down a problem into smaller, more manageable parts and then solving each part. Let's practice this by writing a function `is_positive(number)` that:
#
# - Returns `True` if `number` is positive.
# - Otherwise, returns `False`.


# %%
def is_positive(number):
    return number > 0


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions to test the `is_positive()` function to ensure it returns correct results for -1, 0, and 5.

# %%
assert not is_positive(-1)
assert not is_positive(0)
assert is_positive(5)

# %% [markdown] lang="en" tags=["subslide"]
#
# By writing these small functions and testing them, you are practicing the problem-solving approach of breaking problems down and verifying solutions at each step.
#
# Next, write a function `describe_number(number)` that:
#
# - Prints "`number` is positive." if the number is positive.
# - Prints "`number` is zero." if the number is 0.
# - Prints "`number` is negative." if the number is negative.
#
# Use the `is_positive()` function as part of your solution.


# %%
def describe_number(number):
    if is_positive(number):
        print(f"{number} is positive.")
    elif number == 0:
        print(f"{number} is zero.")
    else:
        print(f"{number} is negative.")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `describe_number(number)` with the values -5, 0, and 10.

# %%
describe_number(-5)
describe_number(0)
describe_number(10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Congratulations! You've taken your first steps into the world of programming by learning to think like a computer scientist and practicing problem-solving. Remember, the key is to break down problems into smaller parts, solve each part, and then combine the solutions. Continue practicing these skills, and you'll become more proficient over time.
