# %% [markdown] lang="en" tags=["subslide"]
# ## Mini-Workshop: Running Python

# %% [markdown] lang="en" tags=["slide"]
# Running Python doesn't always require installation and setup on your local machine. For newcomers to the language, starting out directly in the browser can lower the barrier to entry. There are numerous platforms available for this, such as PythonAnywhere, Jupyter Notebooks, Google Colab, etc. These platforms allow you to write and execute Python code in an interactive environment.

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 1: Basic Python Arithmetic

# %% [markdown] lang="en"  tags=["slide"]
# Execute the following cell to see Python perform arithmetic operations. This will help us confirm that our environment is up and running.

# %%
# This is your first Python code cell! Type 1 + 1 and hit 'Run' or 'Shift+Enter' to execute it.
1 + 1
# %% [markdown] lang="en"  tags=["slide"]
# You should see `2` as the output below the cell. This simple confirmation tells us that our Python interpreter is working as expected.
# %% [markdown] lang="en"  tags=["slide"]
# ### Step 2: Exploring the Python Version

# %% [markdown] lang="en"  tags=["slide"]
# It is always good to know which version of Python you are working with. Execute the following cell to display your Python version.

# %%
# We can check the version of Python we are using by importing the sys module and printing the version information
import sys

print(sys.version)

# %% [markdown] lang="en"  tags=["slide"]
# Ideally, your version number should start with `3`, indicating that you're running Python 3. Python 2 is outdated and not recommended for new projects.

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 3: Your First Python Function

# %% [markdown] lang="en"  tags=["slide"]
# Write a function `hello_world()` that prints "Hello, World!" to the screen. Then call that function in another cell to see the output.


# %%
def hello_world():
    print("Hello, World!")


# %%
hello_world()

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 4: Practice Time

# %% [markdown] lang="en"  tags=["subslide"]
# Now that you have a basic understanding of running Python code, let's practice a bit. Create a function `add(a, b)` that returns the sum of two numbers. Test this function with a few inputs to verify it works as expected.


# %%
def add(a, b):
    return a + b


# Example test cases
print(add(2, 3))  # Should print 5
print(add(-1, 1))  # Should print 0
print(add(10, 20))  # Should print 30

# %% [markdown] lang="en"  tags=["slide"]
# Congratulations! You've written your first pieces of Python code and functions in a Jupyter notebook. This interactive environment is very powerful for learning, experimenting, and even for executing complex data analysis projects.
