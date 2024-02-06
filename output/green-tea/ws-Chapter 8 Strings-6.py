# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Strings - Searching

# %% [markdown] lang="en"
#
# What does the following function do? Analyze the function and describe its behavior.
#
# ```python
# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1
# ```
#
# Given a word and a letter, this function attempts to find the index of the first occurrence of the specified letter within the word. It returns the index if found; otherwise, it returns -1.
#

# %% [markdown] lang="en"
#
# Modify the `find` function so that it accepts a third parameter, which is the index in `word` where it should start looking for `letter`.


# %%
def find(word, letter, start=0):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions to test the modified `find` function. Test that it returns the correct index for different scenarios including cases where the letter is not found.

# %%
assert find("hello", "e") == 1
assert find("hello", "l") == 2
assert find("hello", "l", 3) == 3
assert find("hello", "y") == -1
assert find("python programming", "p", 1) == 7

# %% [markdown] lang="en" tags=["subslide"]
# Implement a function `find_all(word, letter)` that returns a list of all the indices where `letter` appears in `word`.


# %%
def find_all(word, letter):
    indices = []
    index = 0
    while index < len(word):
        if word[index] == letter:
            indices.append(index)
        index = index + 1
    return indices


# %% [markdown] lang="en" tags=["subslide"]
# Test the `find_all` function with various inputs to ensure it correctly identifies all positions of the specified letter.

# %%
assert find_all("hello world", "l") == [2, 3, 9]
assert find_all("hello world", "o") == [4, 7]
assert find_all("hello world", "z") == []
assert find_all("banana", "a") == [1, 3, 5]

# %% [markdown] lang="en" tags=["subslide"]
# Congratulations! You have completed the mini-workshop on searching within strings in Python.
