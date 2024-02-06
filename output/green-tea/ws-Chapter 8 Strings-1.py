# %% [markdown]
# ## Mini-Workshop: Strings

# %% [markdown]
# ### Accessing characters in a string

# %% [markdown]
# A string is a sequence of characters. You can access individual characters using the bracket operator with an index. Remember, indices in Python start at 0.

# %% [markdown]
# Write a function `get_character(word, index)` that returns the character at position `index` from the string `word`.


# %%
def get_character(word, index):
    return word[index]


# %% [markdown]
# Write assertions to test that `get_character("banana", 0)` returns `'b'`, `get_character("apple", 2)` returns `'p'`, and trying to access index 5 of "cat" raises an `IndexError`.

# %%
assert get_character("banana", 0) == "b"
assert get_character("apple", 2) == "p"
try:
    get_character("cat", 5)
except IndexError:
    print("Passed the IndexError test.")
else:
    print("Expected an IndexError.")

# %% [markdown]
# ### String Length and Negative Indices

# %% [markdown]
# The function `len(given_string)` returns the length of the given string. Python also supports negative indices, with `-1` referring to the last character, `-2` to the second last, and so on.

# %% [markdown]
# Write a function `last_character(given_string)` that returns the last character of a string.


# %%
def last_character(given_string):
    return given_string[-1]


# %% [markdown]
# Write assertions to check that `last_character("banana")` returns `'a'`, and `last_character("fun")` returns `'n'`.

# %%
assert last_character("banana") == "a"
assert last_character("fun") == "n"

# %% [markdown]
# ### Iterating Over Strings

# %% [markdown]
# You can iterate over each character in a string using a `for` loop.

# %% [markdown]
# Write a function `print_characters(word)` that prints each character of a string on a new line.


# %%
def print_characters(word):
    for character in word:
        print(character)


# %% [markdown]
# Call `print_characters("hello")` to test your function.

# %%
print_characters("hello")
