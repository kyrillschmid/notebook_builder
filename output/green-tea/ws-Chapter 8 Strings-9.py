Let's now create the Mini-Workshop for Strings using the similar structure as shown in the example workshop. 

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: The `in` Operator in Strings

# %% [markdown] lang="en"
#
# The word `in` is a boolean operator that checks if the first string appears as a substring in the second string.

# %% [markdown] lang="en"
# Write a function `substring_check(substring, string)` that returns `True` if `substring` is found within `string` and `False` otherwise.

# %%
def substring_check(substring, string):
    return substring in string

# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions that check that `substring_check()` returns the correct result for "a" in "banana", "seed" in "banana", and "app" in "apple".

# %%
assert substring_check("a", "banana")
assert not substring_check("seed", "banana")
assert substring_check("app", "apple")

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `in_both(word1, word2)` that prints all the letters from `word1` that also appear in `word2`.

# %%
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

# %% [markdown] lang="en" tags=["subslide"]
# Test `in_both(word1, word2)` with the words "apples" and "oranges".

# %%
in_both("apples", "oranges")

# %% [markdown] lang="en" tags=["subslide"]
# Discuss: How would you modify `in_both()` so that each letter from `word1` is printed only once even if it appears multiple times in `word2`?

# %% [markdown] lang="en"
# To modify `in_both()` so each letter from `word1` is printed only once, you can use a set to keep track of already printed letters. Let's implement this enhanced version named `in_both_unique()`.

# %%
def in_both_unique(word1, word2):
    printed_letters = set()
    for letter in word1:
        if letter in word2 and letter not in printed_letters:
            print(letter)
            printed_letters.add(letter)

# %% [markdown] lang="en" tags=["subslide"]
# Now, test `in_both_unique(word1, word2)` with the words "banana" and "bandana".

# %%
in_both_unique("banana", "bandana")
