# %% [markdown] lang="en" tags=["slide"]
#
# ## Mini-Workshop: Basics of Programming

# %% [markdown] lang="en" tags=["subslide"]
#
# Let's start with understanding what a program is and delve into some core concepts through practice.

# %% [markdown] lang="en" tags=["subslide"]
#
# ### What is a program?

# %% [markdown] lang="en" tags=["subslide"]
#
# A program is a sequence of instructions that specifies how to perform a computation. This could involve various activities like mathematical operations, data processing, conditional execution, and repetition among others. In this activity, we will get a taste of these concepts.

# %% [markdown] lang="en" tags=["subslide"]
# ### Basic Operations
#
# Write a function `perform_operations()` that takes in two numbers and prints their sum, difference, and product.
#


# %%
def perform_operations(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
    print(f"The difference between {a} and {b} is {a - b}")
    print(f"The product of {a} and {b} is {a * b}")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `perform_operations()` with the numbers 5 and 2.

# %%
perform_operations(5, 2)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Conditional Execution
#
# Write a function `compare_numbers(a, b)` that prints which number is larger or if they are equal.


# %%
def compare_numbers(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are equal")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `compare_numbers(a, b)` with the pairs (3, 5), (10, 7), and (4, 4).

# %%
compare_numbers(3, 5)
compare_numbers(10, 7)
compare_numbers(4, 4)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Repetition
#
# Write a function `print_numbers(n)` that prints all numbers from 1 to `n`.


# %%
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `print_numbers(n)` with `n` as 5.

# %%
print_numbers(5)
