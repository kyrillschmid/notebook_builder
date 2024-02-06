Using the given reference and content, let's create a new workshop focused on Strings. We'll structure this new mini-workshop similarly to the reference and ensure that it's focused on the string operations and concepts given in the content.

```python
# %% [markdown]
# ## Mini-Workshop: Strings in Python

# %% [markdown]
# ### Defining Strings

# %% [markdown]
# Define a variable `hello_world` that contains the string "Hello, world!".

# %%
hello_world = "Hello, world!"

# %% [markdown]
# ### String Length

# %% [markdown]
# Write a function `length_of_string(s)` that returns the length of a string.

# %%
def length_of_string(s):
    return len(s)

# %% [markdown]
# Test the `length_of_string` function with the string "Hello, world!".

# %%
assert length_of_string(hello_world) == 13

# %% [markdown]
# ### Accessing Characters and Substrings

# %% [markdown]
# Write a function `get_char_at(s, index)` that returns the character at a specific index in s. Remember that indexing starts at 0.

# %%
def get_char_at(s, index):
    return s[index]

# %% [markdown]
# Test the function `get_char_at` to get the character 'e' from the string "Hello, world!".

# %%
assert get_char_at(hello_world, 1) == 'e'

# %% [markdown]
# Write a function `get_slice_of_string(s, start, end)` that returns a slice of the string from `start` index to `end` index.

# %%
def get_slice_of_string(s, start, end):
    return s[start:end]

# %% [markdown]
# Test `get_slice_of_string` to get "Hello" from "Hello, world!"

# %%
assert get_slice_of_string(hello_world, 0, 5) == "Hello"

# %% [markdown]
# ### Immutable Strings

# %% [markdown]
# Show that strings are immutable by attempting to change the first character of `hello_world` to 'J'.
# Use a try-except block to catch the TypeError.

# %%
try:
    hello_world[0] = 'J'
except TypeError as error:
    print(error)

# %% [markdown]
# ### Looping Through Strings

# %% [markdown]
# Write a function `count_letter(s, letter)` that counts how many times a letter occurs in a string.

# %%
def count_letter(s, letter):
    count = 0
    for char in s:
        if char == letter:
            count += 1
    return count

# %% [markdown]
# Test `count_letter` with the letter 'l' in "Hello, world!"

# %%
assert count_letter(hello_world, 'l') == 3

# %% [markdown]
# This mini-workshop has introduced you to basic string operations in Python, including defining strings, getting their length, accessing specific characters or substrings, demonstrating their immutability, and counting occurrences within the string.
```
This Python Jupyter notebook cells workshop should be engaging for participants, offering a comprehensive hands-on introduction to string operations and characteristics within Python.
