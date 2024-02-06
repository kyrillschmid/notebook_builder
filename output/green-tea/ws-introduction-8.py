# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Introduction to Python

# %% [markdown] lang="en"
#
# In this workshop, we'll be exploring the basics of Python. We'll start with understanding what variables are and how we can use them. Let's dive in!

# %% [markdown] lang="en"
# ### What is a Variable?
# In programming, a variable is used to store information that can be referenced and manipulated in a program. It acts as a container for data.

# %% [markdown] lang="en"
# **Task:** Create a variable named `greeting` that holds the string "Hello, Python!" and print its value.

# %%
# Solution:
greeting = "Hello, Python!"
print(greeting)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Basic Data Types
# Let's explore some of the basic types in Python by creating variables of different types and checking their types using the `type()` function.

# %% [markdown] lang="en"
# **Task:** Create variables to store your age (an integer), your height in meters (a floating-point number), and your first name (a string). Print the type of each variable.

# %%
# Solution:
age = 25  # Replace 25 with your age
height = 1.75  # Replace 1.75 with your height in meters
first_name = "John"  # Replace "John" with your first name

print(type(age))
print(type(height))
print(type(first_name))

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Operators and Expressions
# In Python, operators allow you to perform computations on values. Let's try some of the basic arithmetic operators.

# %% [markdown] lang="en"
# **Task:** Calculate the sum of 15 and 23. Then, calculate the product of 15 and 23. Print both results.

# %%
# Solution:
sum_result = 15 + 23
product_result = 15 * 23

print("Sum:", sum_result)
print("Product:", product_result)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Strings and Concatenation
# String concatenation means adding strings together. Use the `+` operator to concatenate strings.

# %% [markdown] lang="en"
# **Task:** Concatenate your `first_name` variable with a string that says " is learning Python." and print the result.

# %%
# Solution:
message = first_name + " is learning Python."
print(message)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Debugging Exercise
# Often, you might encounter errors in your code. Let's purposely create an error and practice debugging.

# %% [markdown] lang="en"
# **Task:** Fix the syntax error in the code below and execute it to print "Debugging in Python."

# %%
# Intentional error for debugging exercise
# print "Debugging in Python"

# Solution:
print("Debugging in Python")
