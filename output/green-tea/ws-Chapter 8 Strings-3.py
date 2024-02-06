# %% [markdown]
#
# ## Mini-Workshop: String Traversals

# %% [markdown]
#
# Strings in Python can be traversed using loops. This mini-workshop focuses on how to traverse strings and modify string content effectively.

# %% [markdown]
#
# Write a function `print_char_by_char(string)` that takes a string and prints its characters one by one on individual lines.


# %%
def print_char_by_char(string):
    for char in string:
        print(char)


# %% [markdown]
#
# Write a test using `print_char_by_char(string)` with the string `"Python"`.

# %%
print_char_by_char("Python")

# %% [markdown]
#
# As an exercise, write a function `print_reversed(string)` that takes a string as an argument and displays the letters backward, one per line.


# %%
def print_reversed(string):
    for char in string[::-1]:
        print(char)


# %% [markdown]
#
# Test the function `print_reversed(string)` with the string `"Python"`.

# %%
print_reversed("Python")

# %% [markdown]
#
# Another interesting exercise is to work with specific patterns in strings. For instance, let's write a function `print_ducklings_names()` that prints out the names of ducklings in a specific pattern without relying on hardcoded names.


# %%
def print_ducklings_names():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter in ["O", "Q"]:
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


# %% [markdown]
#
# Test `print_ducklings_names()` to check if it correctly prints the modified ducklings names considering the special cases for "O" and "Q".

# %%
print_ducklings_names()

# %% [markdown]
#
# This concludes our exercise on traversing strings. We've covered printing characters, reversing strings, and applying specific patterns to strings for output.```
