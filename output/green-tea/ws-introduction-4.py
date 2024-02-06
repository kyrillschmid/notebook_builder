# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Intro to Arithmetic Operators

# %% [markdown] lang="en" tags=["subslide"]
#
# Python provides various arithmetic operators such as `+`, `-`, `*`, `/`, and `**`. Let's use these operators to perform some basic arithmetic operations.

# %% [markdown] lang="en"
# Write a function `perform_operations(a, b)` that takes two numbers `a` and `b` as arguments and returns a tuple. The tuple should contain the result of: addition (`a + b`), subtraction (`a - b`), multiplication (`a * b`), division (`a / b`), and exponentiation (`a ** b`).


# %%
def perform_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    exponentiation = a**b
    return addition, subtraction, multiplication, division, exponentiation


# %% [markdown] lang="en" tags=["subslide"]
#
# Assert that `perform_operations(6, 2)` returns the correct results for the operations: addition => 8, subtraction => 4, multiplication => 12, division => 3.0, and exponentiation => 36.

# %%
assert perform_operations(6, 2) == (8, 4, 12, 3.0, 36)

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `print_operations(a, b)` that
#
# - takes two numbers `a` and `b`,
# - performs the same arithmetic operations as `perform_operations`, and
# - prints the results in a user-friendly way.
#
# Ensure you clearly label each operation in the output.


# %%
def print_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    exponentiation = a**b
    print(f"Addition: {a} + {b} = {addition}")
    print(f"Subtraction: {a} - {b} = {subtraction}")
    print(f"Multiplication: {a} * {b} = {multiplication}")
    print(f"Division: {a} / {b} = {division}")
    print(f"Exponentiation: {a} ** {b} = {exponentiation}")


# %% [markdown] lang="en" tags=["subslide"]
# Test the `print_operations(a, b)` function with the values 6 and 2.

# %%
print_operations(6, 2)
