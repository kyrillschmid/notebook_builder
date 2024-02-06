Certainly! Taking inspiration from the provided example, let's craft a mini-workshop focused on the topic of Strings and their comparison within Python. We will maintain the structure as seen in the example and adapt the new content accordingly. Here's how it can look as a Jupyter notebook:

```python
# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Strings in Comparison

# %% [markdown] lang="en"
#
# String comparison in Python can be performed using relational operators. This feature is useful for numerous applications, such as sorting and searching within text data. Let's dive into understanding how strings can be compared and ordered in Python.

# %% [markdown] lang="en"
# 
# ### Comparing Strings
# 
# Python utilizes ASCII values for comparison, which means all uppercase letters are considered smaller than lowercase letters. Therefore, comparing 'A' with 'a' would result in 'A' being smaller. However, when comparing whole words, the comparison is made character by character from the left. Hence, 'Apple' comes before 'banana' in such comparison because 'A' is smaller than 'b'.

# %% [markdown] lang="en"
# 
# Write a function `compare_strings(string1, string2)` that prints how the two strings relate to each other (i.e., which one comes first alphabetically or if they are equal). Ensure the comparison is case-insensitive.

# %%
def compare_strings(string1, string2):
    str1_lower = string1.lower()
    str2_lower = string2.lower()
    if str1_lower < str2_lower:
        print(f'"{string1}" comes before "{string2}" alphabetically.')
    elif str1_lower > str2_lower:
        print(f'"{string1}" comes after "{string2}" alphabetically.')
    else:
        print(f'"{string1}" and "{string2}" are the same word.')

# %% [markdown] lang="en" tags=["subslide"]
# 
# Test the `compare_strings` function with the pairs 'Apple', 'banana' and 'Pineapple', 'Banana'.

# %%
compare_strings('Apple', 'banana')
compare_strings('Pineapple', 'Banana')

# %% [markdown] lang="en" tags=["subslide"]
# 
# ### Sorting a List of Strings
# 
# Given Python's comparison logic, when sorting a list of strings, the list will be ordered considering the ASCII values. This means all uppercase letters will precede lowercase ones. Sorting 'Banana', 'apple', 'Orange' will result in 'Banana' coming first, followed by 'Orange', and then 'apple'.

# %% [markdown] lang="en"
# 
# Write a function `sort_strings_case_insensitive(strings)` that takes a list of strings and returns a new list of these strings sorted alphabetically, ignoring case.
 
# %%
def sort_strings_case_insensitive(strings):
    return sorted(strings, key=lambda s: s.lower())

# %% [markdown] lang="en" tags=["subslide"]
# 
# Test `sort_strings_case_insensitive` with the list ['Banana', 'apple', 'Orange'].

# %%
print(sort_strings_case_insensitive(['Banana', 'apple', 'Orange']))

# %% [markdown] lang="en" tags=["subslide"]
# 
# This exercise demonstrates how to perform and utilize string comparisons in Python for various purposes, such as sorting and textual analysis, while handling the case-sensitivity appropriately.
```

This mini-workshop starts with a brief overview of how strings are compared in Python, explicitly dealing with the ASCII values and the impact of case sensitivity. It then proceeds with practical exercises asking to create functions for comparing strings and sorting lists of strings in a case-insensitive manner, thereby reinforcing understanding through application.
