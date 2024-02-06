# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Introduction to Debugging

# %% [markdown] lang="en"
#
# Debugging is a crucial skill in programming. It involves identifying and resolving errors or bugs in your code. Let's practice some basic debugging strategies.

# %% [markdown] lang="en"
# Write a simple function `divide_numbers(numerator, denominator)` that divides two numbers and returns the result. But, make an intentional mistake in the function, for example, use multiplication instead of division.


# %%
def divide_numbers(numerator, denominator):
    # Intentional mistake: using multiplication instead of division
    return numerator * denominator


# %% [markdown] lang="en" tags=["subslide"]
#
# Write a test case that checks whether `divide_numbers()` returns the correct result for a division you know the answer to, e.g., 10 divided by 2. Make an assertion that you know will fail because of the intentional mistake.

# %%
# This assertion should fail because of the mistake in divide_numbers
assert divide_numbers(10, 2) == 5, "The division result should be 5."

# %% [markdown] lang="en" tags=["subslide"]
# Once you've seen the assertion fail, fix the bug in the `divide_numbers` function. Then, run the assertion again to ensure it passes.


# %%
# Corrected function
def divide_numbers(numerator, denominator):
    # Corrected the mistake to use division
    return numerator / denominator


# This assertion should now pass
assert divide_numbers(10, 2) == 5, "The division result should be 5."

# %% [markdown] lang="en" tags=["subslide"]
# Discuss in the comments below the function `divide_numbers` why it's crucial to understand the error messages produced during debugging and how a systematic approach to debugging can help resolve bugs more efficiently.

# %% [markdown] lang="en" tags=["subslide"]
# Debugging Tips:
#
# - Read error messages carefully: They can guide you to the line of code where the problem occurred and sometimes suggest how to fix it.
# - Check your assumptions: Use print statements or a debugger to inspect variables and make sure they hold the values you expect.
# - Take a break: If you're stuck, stepping away for a few minutes can help clear your mind.
# - Ask for help: Discussing the problem with someone else can offer new perspectives and solutions.
