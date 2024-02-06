# j2 from 'macros.j2' import header
# {{ header("Data Indexing and Selection", "Data Indexing and Selection") }}

# %% [markdown] lang="en" tags=["slide"]
# # Data Indexing and Selection
# - Previously, we looked in detail at ways to access, modify, and set values in NumPy arrays
#   - Indexing (`arr[2, 1]`), slicing (`arr[:, 1:5]`), masking (`arr[arr > 0]`), fancy indexing (`arr[0, [1, 5]]`), etc.
# - Now, we'll focus on similar means of accessing & modifying values in Pandas `Series` and `DataFrame` objects
# - If you're comfortable with NumPy patterns, corresponding patterns in Pandas won't be unfamiliar

# %% [markdown] lang="en" tags=["slide"]
# - There are quirky aspects in Pandas' data indexing & selection that we need to keep an eye on
# - We'll start with the simpler one-dimensional `Series` object
# - We'll then delve into the two-dimensional `DataFrame` object which is a bit more complex

# %% [markdown] lang="en" tags=["slide"]
# ## Data Selection in Series
# Here, we'll begin with indexing and selection within `Series` objects# %% [markdown] lang="en" tags=["slide"]
# ## Data Selection in Series
# - A Series behaves like both - a one-dimensional NumPy array and a Python dictionary.
# - As such, it provides a mapping from a collection of keys to values, just like a dictionary.
# - Dictionary-like expressions can be used to explore the keys/indices and values in a Series.
# - Just like assigning a new key adds to a dictionary, you can extend a Series via assigning to a new index value.

# %%
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])
data

# %%
data["b"]

# %%
"a" in data

# %%
data.keys()

# %%
list(data.items())

# %% [markdown] lang="en" tags=["slide"]
# - Like a dictionary, you can also modify a Series. Assigning to a new index value will extend the series.
# - Series also provides array-style item selection, similar to a NumPy array.
# - These include slicing, masking and fancy indexing.
# - The explicit index is included in the slice with slicing, the implicit index is excluded from the slice.

# %%
# New index assignment
data["e"] = 1.25
data

# %%
# Slicing by explicit index
data["a":"c"]

# %%
# Slicing by implicit integer index
data[0:2]

# %%
# Masking
data[(data > 0.3) & (data < 0.8)]

# %%
# Fancy indexing
data[["a", "e"]]

# %% [markdown] lang="en" tags=["slide"]
# - However, these slicing and indexing conventions can lead to confusion.
# - An explicit integer index during an indexing operation will use the explicit indices whereas a slicing operation will use the implicit Python-style index.
# - To avoid such confusion, especially with integer indexes, Pandas provides special indexing attributes.
# - These attributes, which aren't functional methods, enable a particular slicing interface to access the data in the Series.

# %%
# Explicit integer index
data_i = pd.Series(["a", "b", "c"], index=[1, 3, 5])
data_i

# %%
# Explicit index when indexing
data_i[1]

# %%
# Implicit index when slicing
data_i[1:3]

# %% [markdown] lang="en" tags=["slide"]
# - Of these indexing attributes, `loc` enables indexing and slicing that always refer to the explicit index.
# - `iloc` allows indexing and slicing using the implicit Python-style index.
# - A third indexing attribute, `ix`, is a hybrid of the two. For Series objects, this attribute is equivalent to standard []-based indexing.
# - The functionality of `ix` indexer will be clearer in the context of DataFrame objects.
# - With its explicit nature, `loc` and `iloc` are quite handy in maintaining a neat and understandable code. These are highly recommended when dealing with integer indexes.

# %%
# loc attribute
data_i.loc[1]

# %%
data_i.loc[1:3]

# %%
# iloc attribute
data_i.iloc[1]

# %%
data_i.iloc[1:3]

# %% [markdown] lang="en" tags=["slide"]
# ## Data Selection in DataFrame
# - After discussing data selection in Series, let's move onto DataFrame objects.
# - In the next section, we will explore how data indexing and selection are performed in DataFrame objects.# %% [markdown] lang="en" tags=["slide"]
# ## Data Selection in DataFrame
# - A `DataFrame` functions like a two-dimensional or structured array, and as a dictionary of `Series` sharing the same index
# - Envisioning the `DataFrame` as a dictionary of related `Series`, facilitates data selection within the structure
# - In the example given, 'area' and 'population of states' are created as separate `Series` and combined into a `DataFrame`
# - Columns of a `DataFrame` can be accessed via dictionary-style indexing of the column name

# %%
import pandas as pd

area = pd.Series(
    {
        "California": 423967,
        "Texas": 695662,
        "New York": 141297,
        "Florida": 170312,
        "Illinois": 149995,
    }
)
pop = pd.Series(
    {
        "California": 38332521,
        "Texas": 26448193,
        "New York": 19651127,
        "Florida": 19552860,
        "Illinois": 12882135,
    }
)
data = pd.DataFrame({"area": area, "pop": pop})
data

# %%
# Access data using dictionary style indexing
data["area"]

# %% [markdown] lang="en" tags=["slide"]
# - Columns from `DataFrame` can also be accessed using attribute-style access with column names that are strings
# - The attribute-style column access and the dictionary-style access point to the same object
# - Remember that attribute-style access works only with column names that are strings and those that do not conflict with `DataFrame` methods
# - For instance, `DataFrame` has a `pop()` method. Hence `data.pop` will refer to this method instead of the "pop" column

# %%
# Attribute-style access to the data
data.area

# %%
# Check if both styles of access point to the same object
data.area is data["area"]

# %%
# The attribute access does not point to 'pop' column as it conflicts with `DataFrame`'s method
data.pop is data["pop"]

# %% [markdown] lang="en" tags=["slide"]
# - Avoid assigning column data using attributes. Instead, use dictionary-style syntax
# - This style can be used to add and modify columns in the `DataFrame`
# - A `DataFrame` can be viewed as an enhanced two-dimensional array. You can examine its raw data using the `values` attribute
# - `DataFrame` can be transposed to interchange rows and columns using `.T`

# %%
# Add a new column to the DataFrame
data["density"] = data["pop"] / data["area"]
data

# %%
# Access the raw data
data.values

# %%
# Transpose the DataFrame
data.T

# %% [markdown] lang="en" tags=["slide"]
# - The dictionary-style indexing method hinders treating a `DataFrame` as NumPy array
# - While passing a single index to an array accesses a row, passing a single "index" to a `DataFrame` gets a column
# - For array-style indexing, we need a different convention
# - In pandas, `loc`, `iloc`, and `ix` indexers can be used.
# - The `iloc` indexer lets us index the underlying array like a simple NumPy array
# - The `loc` indexer allows array-like indexing using explicit index and column names

# %%
# Indexing DataFrame like an numpy array
data.values[0]

# %%
# Access a specific column in DataFrame
data["area"]

# %% [markdown] lang="en" tags=["slide"]
# - The `ix` indexer allows a combination of both `loc` and `iloc` styles
# - Any NumPy-style data access patterns can also be used within the above indexers
# - For instance, in the `loc` indexer we can combine masking and fancy indexing
# - Any of these indexing methods can also be used to set or modify values
# - Which is very similar to the standard way of working with NumPy

# %%
# Indexing with the iloc indexer
data.iloc[:3, :2]

# %%
# Indexing using the loc indexer
data.loc[:"Illinois", :"pop"]

# %%
# ix indexer hybrid of the two
data.ix[:3, :"pop"]

# %%
# Modifying dataframe using iloc
data.iloc[0, 2] = 90
data

# %% [markdown] lang="en" tags=["slide"]
# - The discrepancy between indexing and slicing in `DataFrame` is worth noting
# - While indexing refers to columns, slicing refers to rows
# - Such slices can also refer to rows by number rather than by index
# - Direct masking operations are also interpreted row-wise rather than column-wise:
# - These two conventions are similar to those used in NumPy array

# %%
# Slicing rows
data["Florida":"Illinois"]

# %%
# Slicing rows by number
data[1:3]

# %%
# Masking operations
data[data.density > 100]
