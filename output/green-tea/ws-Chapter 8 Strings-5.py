# %% [markdown] lang="en" tags=["subslide"]
#
## Mini-Workshop: String Immunity

# %% [markdown] lang="en"
#
# Explain why the below code results in an error.
#
# ```python
# greeting = 'Hello, world!'
# greeting[0] = 'J'
# ```
# %% [markdown] lang="en"
#
# Answer: This code results in a `TypeError` because strings in Python are immutable, meaning they cannot be changed after creation. Attempting to assign a new value to a position in the string (like replacing 'H' with 'J') is not allowed. Instead, one must create a new string with the desired modifications.
#

# %% [markdown] lang="en"
# Write a function named `replace_first_char(string, new_char)` which returns a new string with the first character replaced by `new_char`.


# %%
def replace_first_char(string, new_char):
    return new_char + string[1:]


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions to check that `replace_first_char` works as expected for the strings 'Hello, world!' and 'Java', replacing the first character with 'J' and 'C' respectively.

# %%
assert replace_first_char("Hello, world!", "J") == "Jello, world!"
assert replace_first_char("Java", "C") == "Cava"

# %% [markdown] lang="en"
# Write a function `modify_greeting(greeting)` that takes a string `greeting` and returns a new string with 'Hello, world!' changed to 'Jello, world!'. If the original greeting is different from 'Hello, world!', return 'Greeting not recognized!'.


# %%
def modify_greeting(greeting):
    return (
        "Jello, world!" if greeting == "Hello, world!" else "Greeting not recognized!"
    )


# %% [markdown] lang="en" tags=["subslide"]
# Test `modify_greeting()` with the values 'Hello, world!' and 'Good morning!'.

# %%
assert modify_greeting("Hello, world!") == "Jello, world!"
assert modify_greeting("Good morning!") == "Greeting not recognized!"
