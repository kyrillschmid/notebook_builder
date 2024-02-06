# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop: Colors (Part 1)
#
# - Define a variable `primary_colors` containing a list of the strings
#  `"red"`, `"green"` and `"blue"`.
# - Define a variable `mixed_colors` containing a list of the strings
#  `"cyan"`, `"yellow"`, and `"magenta"`.

# %% lang="en"
primary_colors = ["red", "green", "blue"]

# %% lang="en"
mixed_colors = ["cyan", "yellow", "magenta"]

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a list `colors` containing the elements of `primary_colors`
# followed by the elements of `mixed_colors`.

# %% lang="en"
colors = primary_colors + mixed_colors
colors

# %% [markdown] lang="en" tags=["subslide"]
#
# Create a list containing 15 times the number `1`.

# %%
[1] * 15

# %% [markdown] lang="en" tags=["subslide"]
#
# Create the list `["r", "g", "b"]` from the string `"rgb"`.

# %%
list("rgb")
