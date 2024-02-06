# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Strings

# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `string_length(s)`, die die Länge eines Strings zurückgibt.

# %% [markdown] lang="en" tags=["slide"]
#
# Write a function `string_length(s)` that returns the length of a string.


# %%
def string_length(s):
    return len(s)


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions that verify that `string_length()` returns the correct result for the strings "apple", "" (empty string), and "python".

# %%
assert string_length("apple") == 5
assert string_length("") == 0
assert string_length("python") == 6

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `last_character(s)` that returns the last character of a string. If the string is empty, it should return an empty string.


# %%
def last_character(s):
    return s[-1] if s else ""


# %% [markdown] lang="en" tags=["subslide"]
# Test `last_character(s)` with the strings "banana", "" (empty string), and "hello world".

# %%
assert last_character("banana") == "a"
assert last_character("") == ""
assert last_character("hello world") == "d"

# %% [markdown] lang="en" tags=["subslide"]
# Now, write a function `reverse_string(s)` that returns a new string with the characters of `s` in reverse order.


# %%
def reverse_string(s):
    return s[::-1]


# %% [markdown] lang="en" tags=["subslide"]
# Test `reverse_string(s)` with the strings "banana", "" (empty string), and "hello".

# %%
assert reverse_string("banana") == "ananab"
assert reverse_string("") == ""
assert reverse_string("hello") == "olleh"
