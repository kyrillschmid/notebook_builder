# j2 from 'macros.j2' import header
# {{ header("Introduction to Visualization with Matplotlib", "Introduction to Visualization with Matplotlib") }}

# %% [markdown] lang="en" tags=["slide"]
# # Visualization with Matplotlib
# - Matplotlib is a powerful, multi-platform data visualization library built on NumPy arrays, designed to work with the entire SciPy stack.
# - It was originally created by John Hunter in 2002 as an enabling tool for interactive MATLAB-style plotting via gnuplot from the IPython command line.
# - Matplotlib has been adopted by organizations like the Space Telescope Science Institute for its plotting capabilities, which has aided in its development and the enhancement of its features.

# %% [markdown] lang="en" tags=["slide"]
# - Matplotlib is versatile, interacting well with various operating systems and graphics backends, with support for plenty of backends and output types.
# - Its cross-platform approach has strengthened its position among visualization tools, leading to a large user base and an active developer environment.
# - Despite the emergence of newer visualization tools, Matplotlib remains a robust and well-tested graphics engine.

# %% [markdown] lang="en" tags=["slide"]
# - Over the years, Matplotlib’s interface and style have started to show signs of age.
# - However, newer versions of Matplotlib allows users to define new global plotting styles more conveniently.
# - Packages such as Seaborn, and Pandas itself, have been constructed to drive Matplotlib via cleaner, APIs.
# - Even with these wrappers, you might still find yourself diving into Matplotlib's syntax to polish your final plot output, testifying to its continued importance in the field of data visualization.

# %% [markdown] lang="en" tags=["slide"]
# ## General Matplotlib Tips
# This section will provide you with some useful tips on using Matplotlib effectively.

# %% [markdown] lang="en" tags=["slide"]
# ## General Matplotlib Tips
# - Matplotlib follows standard shorthands for its import statements:
#   - `import matplotlib as mpl`
#   - `import matplotlib.pyplot as plt`
# - Most common interface for plot creation is through `plt`
# - Aesthetic styles for plots are set using `plt.style` directive
#   - Following command is used to set the `classic` Matplotlib style: `plt.style.use('classic')`
# - How you view your Matplotlib plots depends on the context
#   - The three applicable contexts are using Matplotlib in a script, in an IPython terminal, or in an IPython notebook.

# %% 
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
plt.style.use('classic')

# %% [markdown] lang="en" tags=["slide"]
# - In a script, `plt.show()` starts an event loop and opens one or more interactive windows with your active figures 
# - An example would be creating a script called `myplot.py` and running it from commandline which would then open a window with the defined plot
# - `plt.show()` should be used only once per Python session, often at the very end of the script
# - For effective usage of Matplotlib within an IPython shell, use the `%matplotlib` magic command after starting `ipython` 
# - Once `%matplotlib `command is run, any `plt` plot command will open a figure window, and further commands can update the plot.

# %%
import numpy as np

x = np.linspace(0,10,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

# %% [markdown] lang="en" tags=["slide"]
# - IPython notebook is a browser-based interactive data analysis tool 
#   - Plotting in IPython notebook can be done with the `%matplotlib` command, similar to IPython shell
# - You have the option of embedding graphics directly in the notebook
# - `%matplotlib inline` command embeds a PNG image of the resulting graphic
# - Ability to save figures in many formats with the `savefig()` command
#   - Example: To save the figure as a PNG file, run `fig.savefig('my_figure.png')`
# - File format is inferred from the extension of the given filename in `savefig()`
# - To display the file contents, `IPython's Image` object can be used: `Image('my_figure.png')`
# - To list down supported file types in your system, use: `fig.canvas.get_supported_filetypes()`

# %% 
%matplotlib inline

# %%
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');

# %%
fig.savefig('my_figure.png')

# %%
from IPython.display import Image 
Image('my_figure.png')

# %%
fig.canvas.get_supported_filetypes()# %% [markdown] lang="en" tags=["slide"]
# ## Two Interfaces for the Price of One
# - Matplotlib offers two interfaces: a MATLAB-like state-based interface and a more powerful object-oriented approach
# - Syntax of the state-based interface, accessed via the pyplot (`plt`) interface, is designed to reflect MATLAB and be familiar to its users
# - This interface is stateful, automatically keeping track of the "current" figure and axes
# - You can access these using `plt.gcf()` (get current figure) and `plt.gca()` (get current axes)
# - Though the stateful interface is great for simple plots, it can lead to complications when dealing with more complex plotting scenarios

# %% 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

# using the stateful (MATLAB-like) interface
plt.figure() # create a plot figure
plt.subplot(2, 1, 1) # create the first of two panels and set current axis
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2) # create the second panel and set current axis
plt.plot(x, np.cos(x))

# %%
# Get reference to current figure and axes
current_figure = plt.gcf()
current_axes = plt.gca()

# %% [markdown] lang="en" tags=["slide"]
# ## Object-oriented Interface
# - The object-oriented interface provides more control and is useful in complex plotting situations
# - Instead of depending on the notion of an "active" figure or axes, the object-oriented interface uses plotting functions as methods of explicit `Figure` and `Axes` objects
# - The difference between the two interfaces is often as small as switching from `plt.plot()` to `ax.plot()`, with few notable exceptions


# %%
# Using the object-oriented interface
fig, ax = plt.subplots(2) # Creates a grid of plots, ax will be an array of two Axes objects
ax[0].plot(x, np.sin(x)) # Call plot() method on the appropriate object
ax[1].plot(x, np.cos(x))

# %% [markdown] lang="en" tags=["slide"]
# ## Choosing the Interface
# - The choice of the interface largely depends on preference and the complexity of the plot
# - For more complex plots, the object-oriented approach might be the most suitable
# - Throughout this training, we will use both the MATLAB-style and object-oriented interfaces appropriately
# - In most cases, transition between the two is straightforward, but specific differences will be highlighted when encountered