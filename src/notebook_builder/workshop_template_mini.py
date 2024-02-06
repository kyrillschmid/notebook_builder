# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Even number
#
# Write a function `is_even(number)` that returns `True`,
# if `number` is even and `False` if `number` is odd.


# %%
def is_even(number):
    return number % 2 == 0


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions that check that `is_even()` returns the correct result
# for arguments 0, 1 and 8.

# %%
assert is_even(0)
assert not is_even(1)
assert is_even(8)

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `print_is_even(number)` that
#
# - prints `{number} is even.` on the screen if `number` is even and
# - Prints `{number} is odd.` to the screen if `number` is not
#   is straight.
#
# Use the `is even()` function to check if `number` is even.


# %%
def print_is_even(number):
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# %% [markdown] lang="en" tags=["subslide"]
# Test `print_is_even(number)` with the values 0, 1 and 8.

# %%
print_is_even(0)
print_is_even(1)
print_is_even(8)
