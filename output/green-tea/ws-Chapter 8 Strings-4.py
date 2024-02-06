# %% [markdown] lang="en" tags=["subslide"]
#
## Mini-Workshop: String Slices

# %% [markdown] lang="en"
#
# - Write a function `extract_slice(string, start, end)` that extracts a slice from the provided `string` from index `start` to index `end` (inclusive start and exclusive end).
# - If `end` is not provided, extract the slice from `start` to the end of the string.
# - If `start` and `end` are not provided, return the entire string.


# %%
def extract_slice(string, start=None, end=None):
    if start is None and end is None:
        return string
    elif end is None:
        return string[start:]
    else:
        return string[start:end]


# %% [markdown] lang="en" tags=["subslide"]
#
# - Write assertions to check that `extract_slice()` returns the correct result for the string `'Monty Python'` with indices (0, 5), (6, 12), and also checks the functionality when omitting start or end indices.


# %%
assert extract_slice("Monty Python", 0, 5) == "Monty"
assert extract_slice("Monty Python", 6, 12) == "Python"
assert extract_slice("Monty Python", 6) == "Python"
assert extract_slice("Monty Python", None, 5) == "Monty"
assert extract_slice("Monty Python") == "Monty Python"

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `is_empty(string)` that returns `True` if the `string` is empty and `False` otherwise. Utilize string slices to check for an empty string by comparing the whole string slice `string[:]` with an empty string `''`.


# %%
def is_empty(string):
    return string[:] == ""


# %% [markdown] lang="en" tags=["subslide"]
# Test `is_empty(string)` with an empty string, a string containing only spaces, and a non-empty string.

# %%
assert is_empty("")
assert not is_empty(" ")
assert not is_empty("Monty Python")
