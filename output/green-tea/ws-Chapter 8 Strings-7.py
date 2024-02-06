# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Looping and Counting

# %% [markdown] lang="en"
#
# Write a function `count_letter(word, letter)` that counts how many times `letter` appears in `word`. The function should be case sensitive.

# %%
def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions to test that `count_letter()` returns the correct result for several cases.

# %%
assert count_letter("banana", "b") == 1
assert count_letter("banana", "a") == 3
assert count_letter("Mississippi", "s") == 4
assert count_letter("Mississippi", "p") == 2

# %% [markdown] lang="en" tags=["subslide"]
# Now, rewrite the function `count_letter` using the string method `find`. The function should still accept the string and the letter as arguments but should use `find` internally to count the letter appearances.


# %%
def count_letter_with_find(word, letter):
    count = 0
    start = 0
    while True:
        start = word.find(letter, start)
        if start == -1: 
            break
        count += 1
        start += 1  # Move past the current match
    return count


# %% [markdown] lang="en" tags=["subslide"]
# Test the `count_letter_with_find` function to ensure it also returns correct results.

# %%
assert count_letter_with_find("banana", "b") == 1
assert count_letter_with_find("banana", "a") == 3
assert count_letter_with_find("Mississippi", "s") == 4
assert count_letter_with_find("Mississippi", "p") == 2

# %% [markdown] lang="en" tags=["subslide"]
# Time to test your knowledge! Define a new function `most_common_letter(word)` that returns the most common letter in the string. If several letters have the same highest frequency, return any one of them.


# %%
def most_common_letter(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return max(letter_count, key=letter_count.get)


# %% [markdown] lang="en" tags=["subslide"]
# Test the `most_common_letter` function to ensure it works correctly.

# %%
assert most_common_letter("banana") == "a"
assert most_common_letter("Mississippi") in ["s", "i"]
assert most_common_letter("evening") == "e"

# %% [markdown] lang="en"
# Congratulations on completing the workshop!
