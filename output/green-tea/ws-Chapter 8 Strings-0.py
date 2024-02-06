# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Strings

# %% [markdown] lang="en"
# A string is a sequence of characters. In Python, strings can be created by enclosing characters in quotes (" or ').
# Let's explore the basic operations and methods you can perform on strings.

# %% [markdown] lang="en"
# Write a function `is_palindrome(s)` that returns `True`,
# if `s` is a palindrome (i.e., it reads the same forward and backward, ignoring spaces, punctuation, and case) and `False` otherwise.


# %%
def is_palindrome(s):
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    return filtered_chars == filtered_chars[::-1]


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions that check that `is_palindrome()` returns the correct result
# for the strings "radar", "hello", and "A man, a plan, a canal – Panama".

# %%
assert is_palindrome("radar")
assert not is_palindrome("hello")
assert is_palindrome("A man, a plan, a canal – Panama")

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `count_vowels(s)` that counts and returns the number of vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) in a string `s`.
# Note: the function should be case-insensitive.


# %%
def count_vowels(s):
    vowels = "aeiou"
    return sum(c.lower() in vowels for c in s)


# %% [markdown] lang="en" tags=["subslide"]
# Test `count_vowels(s)` with the strings "hello", "world", and "AEIOU".

# %%
print(count_vowels("hello"))  # Expected output: 2
print(count_vowels("world"))  # Expected output: 1
print(count_vowels("AEIOU"))  # Expected output: 5
