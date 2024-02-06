# %% [markdown]
# # Mini-Workshop: Values and Types

# %% [markdown] lang="en" tags=["subslide"]
# In this workshop, we will explore Python values and their types, which are the fundamental components to understand before diving deep into Python programming.

# %% [markdown] lang="en"
# ## Understanding Values and Types

# %% [markdown] lang="en"
# A *value* is one of the basic things a program works with, like a letter or a number. Some values we have seen so far are 2, 42.0, and 'Hello, World!'. Values belong to different *types*: 2 is an *integer*, 42.0 is a *floating-point number*, and 'Hello, World!' is a *string*.

# %% [markdown] lang="en"
# Use Python's `type()` function to find out the type of a value. Try to predict what the type will be before you run each of the following lines:

# Here are some values
values = [2, 42.0, "Hello, World!", "2", "42.0", 1, 000, 000]

# %% [markdown] lang="en"
# Loop through the values and print their types:
# %%
for value in values:
    print(f"The type of {value} is {type(value)}")

# %% [markdown] lang="en"
# ## Exercise: Predict the Type

# %% [markdown] lang="en"
# Can you predict the type of the following values? Use the code cell below to check your predictions:
#
# 1. '2'
# 2. '42.0'
# 3. 1,000,000
#
# Note: Write your prediction before running the code.

# Write your code here to check the type of each value above
print(type("2"))
print(type("42.0"))
print(type(1, 000, 000))

# %% [markdown] lang="en"
# Were your predictions correct? Discuss any surprises or unclear results.

# %% [markdown] lang="en"
# ## Understanding Comma-separated Values

# %% [markdown] lang="en"
# When you type a large integer, you might be tempted to use commas between groups of three digits, as in `1,000,000`. This is not a legal integer in Python, as you've seen. Discuss what you observed when you checked the type of `1,000,000`.

# %% [markdown] lang="en"
# As an additional task, try printing the type and value of `1,000,000` without using the `print()` function in a loop or a specific function call. What does Python interpret this as?

# %% [markdown] lang="en"
# ## Conclusion

# %% [markdown] lang="en"
# In this workshop, you have learned about basic types in Python, such as integers, floating-point numbers, and strings. You have also seen how the `type()` function can be used to discover the type of a given value.
#
# Understanding the types of values is crucial in programming because it affects how the values can be manipulated and used in expressions. Keep experimenting with different values to get comfortable with their types.
