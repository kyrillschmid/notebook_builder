# j2 from 'macros.j2' import header
# {{ header("Operating on Data in Pandas", "Operating on Data in Pandas") }}

# %% [markdown] lang="en" tags=["slide"]
# # Operating on Data in Pandas
# - NumPy's capability for quick element-wise operations, encompassing basic arithmetic and sophisticated functions, is an essential part.
# - Much of this functionality is inherited by Pandas, driven by ufuncs.
# - Unique twists in Pandas include: For unary operations like negation and trigonometric functions, ufuncs will preserve index and column labels in the output.
# - For binary operations such as addition and multiplication, Pandas aligns indices automatically when passing the objects to the ufunc.

# %% [markdown] lang="en" tags=["slide"]
# ## Operating on Data in Pandas (contd.)
# - These Pandas features make data context maintenance and combining data - tasks prone to errors with raw NumPy arrays - essentially foolproof.
# - Pandas also supports well-defined operations between one-dimensional `Series` structures and two-dimensional `DataFrame` structures.

# %% [markdown] lang="en" tags=["slide"]
# ## Ufuncs: Index Preservation
# - Ufuncs or universal functions in Pandas are used for vectorized operations and they preserve the index and labels while executing calculations.# %% [markdown] lang="en" tags=["slide"]
# ## Ufuncs: Index Preservation
# - Pandas is designed to work with NumPy, hence any NumPy ufunc will operate on Pandas `Series` and `DataFrame` objects.
# - We will demonstrate this by defining a simple `Series` and `DataFrame`.
# - Applying a NumPy ufunc on these objects will return another Pandas object with the indices preserved.

# %% 
import pandas as pd 
import numpy as np

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
ser

# %% 
df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns = ['A', 'B', 'C', 'D'])
df

# %% [markdown] lang="en" tags=["slide"]
# - For example, applying `np.exp()` function on the `Series` object:
   
# %% 
np.exp(ser)

# %% [markdown] lang="en" tags=["slide"]
# - And, for a slightly more complex calculation using `np.sin()` function:

# %%  
np.sin(df * np.pi / 4)

# %% [markdown] lang="en" tags=["slide"]
# - All the ufuncs we have learned in NumPy can be used similarly on Pandas data structures.

# %% [markdown] lang="en" tags=["slide"]
# ## UFuncs: Index Alignment
# - (The following content for this topic will be covered in the next section)# %% [markdown] lang="en" tags=["slide"]
# ## UFuncs: Index Alignment
# - `Pandas` aligns indices during binary operations on `Series` or `DataFrame` objects
# - This is useful when dealing with incomplete data
# - `Pandas` performs index alignment when combining data from different sources
# - When an operation is done using the data from these sources, the result contains the `union` of indices from both data sets
# - Any element that does not have an entry (missing data) is marked with `NaN`

# %%
import pandas as pd

area = pd.Series({'Alaska': 1723337, 'Texas': 695662, 'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127}, name='population')

population / area

# %%
# Show the union of indices
area.index | population.index

# %% [markdown] lang="en" tags=["slide"]
# ## Handling Missing Data
# - Index matching is implemented for Python's built-in arithmetic expressions with missing values filled in with NaN
# - The behavior of using NaN values can be modified using appropriate object methods in place of the operators
# - Object methods also allow explicit specification of the fill value for any element that might be missing 

# %%
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A + B

# Filling missing elements with 0
A.add(B, fill_value = 0)

# %% [markdown] lang="en" tags=["slide"]
# ## Index Alignment for DataFrame
# - Similar type of alignment takes place for both columns and indices when operations are performed on `DataFrame`s
# - Indices align correctly irrespective of their order in the objects, and indices in the result are sorted
# - You can pass any desired `fill_value` to be used in place of missing entries

# %%
rng = np.random.default_rng(42)  # Creating a default random number generator

A = pd.DataFrame(rng.integers(0, 20, (2, 2)), columns=list('AB'))

B = pd.DataFrame(rng.integers(0, 10, (3, 3)), columns=list('BAC'))

A + B

# Filling with the mean of all values in A
fill = A.stack().mean()
A.add(B, fill_value = fill)

# %% [markdown] lang="en" tags=["slide"]
# ## Python Operators and Pandas Object Methods
# - Python arithmetic operators have corresponding Pandas object methods
# - These can be used to handle special operations like filling missing values

#%% [markdown] lang="en" tags=["slide"]
# ## Ufuncs: Operations Between DataFrame and Series
# - Upcoming sections delve into operations between `DataFrame` and `Series` objects
# - This provides flexibility when operating on data with different dimensions# %% [markdown] lang="en" tags=["slide"]
# ## Ufuncs: Operations Between DataFrame and Series
# - Operations between a `DataFrame` and a `Series` maintain index and column alignment similar to operations between a two-dimensional and one-dimensional NumPy array.
# - Common operation include finding the difference of a two-dimensional array and one of its rows.
# - According to NumPy's broadcasting rules, subtraction between a two-dimensional array and one of its rows is applied row-wise.

# %%
A = rng.randint(10, size=(3, 4))
A

# %% [markdown] lang="en" tags=["slide"]
# - In Pandas, the convention operates row-wise by default.
# - If you wish to operate column-wise, you can use object methods and specify the `axis` keyword.

# %%
A - A[0]

# %%
df = pd.DataFrame(A, columns=list('QRST'))

# %%
df - df.iloc[0]

# %% [markdown] lang="en" tags=["slide"]
# - `DataFrame`/`Series` operations will automatically align indices between the two elements.
# - This alignment of indices and columns ensures that operations on data in Pandas will always maintain the data context. This can prevent errors when working with heterogeneous and/or misaligned data in raw NumPy arrays.

# %%
df.subtract(df['R'], axis=0)

# %%
halfrow = df.iloc[0, ::2]

# %%
df - halfrow
