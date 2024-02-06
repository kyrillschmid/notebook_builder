Based on the reference mini-workshop template, here is the structured Jupyter notebook cells tailored for the topic of strings and particularly focusing on string methods, capitalization, and substring searching:

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: String Methods

# %% [markdown] lang="en"
#
# Explore string methods that transform string case and locate substrings within strings.

# %% [markdown] lang="en"
#
# Create a function `to_upper_case(text)` that returns a new string with all uppercase letters of `text`.

# %%
def to_upper_case(text):
    return text.upper()

# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions that check that `to_upper_case()` returns the correct result for the strings `'Hello'`, `'world'`, and `'Python is fun!'`.

# %%
assert to_upper_case('Hello') == 'HELLO'
assert to_upper_case('world') == 'WORLD'
assert to_upper_case('Python is fun!') == 'PYTHON IS FUN!'

# %% [markdown] lang="en" tags=["subslide"]
# Create a function `find_substring(text, substring, start=0, end=None)` that returns the lowest index in `text` where `substring` is found, such that `substring` is contained within `text[start:end]`. Return `-1` if `substring` is not found.

# %%
def find_substring(text, substring, start=0, end=None):
    if end is None:  # If end is not provided, search till the end of the string
        end = len(text)
    return text.find(substring, start, end)

# %% [markdown] lang="en" tags=["subslide"]
# Perform tests using `find_substring()` with various examples:
# - Check if `'na'` can be found within `'banana'` and at what index.
# - Find `'na'` after the first two characters in `'banana'`.
# - Attempt to find `'ba'` in `'banana'` starting from index 3.
# - Try to find `'peach'` in `'This is a peach!'`.

# %%
assert find_substring('banana', 'na') == 2
assert find_substring('banana', 'na', 3) == 4
assert find_substring('banana', 'ba', 3) == -1
assert find_substring('This is a peach!', 'peach') == 10

# %% [markdown] lang="en" tags=["subslide"]
# Create a function `print_substring_location(text, substring)` that:
#
# - Prints `'{substring} found at index {index}.'` if the `substring` is found within `text`.
# - Prints `'{substring} not found.'` if the `substring` is not found within `text`.
#
# Use the `find_substring()` function to determine the location of `substring`.


# %%
def print_substring_location(text, substring):
    index = find_substring(text, substring)
    if index != -1:
        print(f"'{substring}' found at index {index}.")
    else:
        print(f"'{substring}' not found.")

# %% [markdown] lang="en" tags=["subslide"]
# Test `print_substring_location(text, substring)` with the pairs of values: `('banana', 'na')`, `('Hello World!', 'World')`, and `('Python programming', 'Java')`.

# %%
print_substring_location('banana', 'na')
print_substring_location('Hello World!', 'World')
print_substring_location('Python programming', 'Java')

This mini-workshop should help familiarize learners with string methods in Python, focusing on transforming string case and searching for substrings.
