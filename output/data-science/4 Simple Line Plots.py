# %% [markdown] lang="en" tags=["slide"]
# # Simple Line Plots
# - Line plots are one of the simplest types of plots visualizing a single function $y = f(x)$.
# - The first step in any plotting exercise is setting up the environment and importing necessary packages.
# - In Matplotlib, every plot starts with creating a figure and then an axes.

# %%
%matplotlib inline
import matplotlib.pyplot as plt 
plt.style.use('seaborn-whitegrid')
import numpy as np

# %% [markdown] lang="en" tags=["slide"]
# - The figure in Matplotlib can be thought of as a container holding all the components such as axes, graphics, text, and labels that make up the plot.
# - The axes is a bounding box with ticks and labels that will hold the plot elements like lines, points etc.
# - Conventionally, we generally use variable names 'fig' and 'ax' for a figure and axes instance respectively.
# - Even for a simple line plot, an axes instance ('ax') is required. We use `ax.plot` function to plot the data.

# %%
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));

# %% [markdown] lang="en" tags=["slide"]
# - Alternatively, Matplotlib offers an pylab interface where the figure and axes can be created automatically in the background.
# - To plot multiple lines in the same figure, simple recall the `plot` function with the new data.
# - We will now delve deeper into finer adjustments to the appearance of axes and lines.

# %%
plt.plot(x, np.sin(x));
plt.plot(x, np.cos(x));

# %% [markdown] lang="en" tags=["slide"]
# ## Adjusting the Plot: Line Colors and Styles
# - In the next section, we will explore how to adjust line colors and styles in Matplotlib.# %% [markdown] lang="en" tags=["slide"]
# ## Adjusting the Plot: Line Colors and Styles
# - The `plt.plot()` function takes additional arguments to control line colors and styles.
# - The color can be specified using `color` keyword in different ways - by color name, short color code, grayscale value, hex code, RGB tuple, etc. If no color is specified, Matplotlib will cycle through default colors for multiple lines.
# - Line style can be adjusted using `linestyle` keyword. You can also use single character codes for line styles.
# - The `color` and `linestyle` arguments can be combined into a single non-keyword argument.
# - There are many other keyword arguments for further fine-tuning of plot appearance.

# %% 
# color and style example codes
plt.plot(x, np.sin(x - 0), color='blue') # specify color by name 
plt.plot(x, np.sin(x - 1), color='g') # short color code (rgbcmyk) 
plt.plot(x, np.sin(x - 2), color='0.75') # Grayscale between 0 and 1 
plt.plot(x, np.sin(x - 3), color='#FFDD44') # Hex code (RRGGBB from 00 to FF) 
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3)) # RGB tuple, values 0 to 1 
plt.plot(x, np.sin(x - 5), color='chartreuse') # all HTML color names supported

# %%
# linestyle examples
plt.plot(x, x + 0, linestyle='solid') 
plt.plot(x, x + 1, linestyle='dashed') 
plt.plot(x, x + 2, linestyle='dashdot') 
plt.plot(x, x + 3, linestyle='dotted')

# short codes
plt.plot(x, x + 4, linestyle='-') # solid 
plt.plot(x, x + 5, linestyle='--') # dashed 
plt.plot(x, x + 6, linestyle='-.') # dashdot 
plt.plot(x, x + 7, linestyle=':') # dotted

# %%
# combined color and linestyle
plt.plot(x, x + 0, '-g') # solid green 
plt.plot(x, x + 1, '--c') # dashed cyan 
plt.plot(x, x + 2, '-.k') # dashdot black 
plt.plot(x, x + 3, ':r') # dotted red

# %% [markdown] lang="en" tags=["slide"]
# ## Adjusting the Plot: Axes Limits
# To learn more details about fine-tuning the plot, it is advised to explore the docstring of the `plt.plot()` function. This includes information on how to adjust the axes limits of the plot.# %% [markdown] lang="en" tags=["slide"]
# ## Adjusting the Plot: Axes Limits
# - Matplotlib has built-in default axes limits, but users have the ability to adjust those limits for finer control.
# - The `plt.xlim()` and `plt.ylim()` methods are the most basic ways to adjust the axis limits.
# - Axis limits can also be displayed in reverse order.
# - The `plt.axis()` method allows for setting the x and y limits with a single function call by passing a list - `[xmin, xmax, ymin, ymax]`.
# - The `plt.axis()` method also has the capability to tighten the bounds around the current plot or ensure an equal aspect ratio.

# %%
# Code to demonstrate the use of plt.xlim() and plt.ylim()
plt.plot(x, np.sin(x)) 
plt.xlim(-1, 11) 
plt.ylim(-1.5, 1.5)

# %%
# Code to demonstrate reversing the order of the arguments
plt.plot(x, np.sin(x)) 
plt.xlim(10, 0) 
plt.ylim(1.2, -1.2)

# %%
# Code to demonstrate the use of plt.axis
plt.plot(x, np.sin(x)) 
plt.axis([-1, 11, -1.5, 1.5])

# %%
# Code to demonstrate tightening the bounds around the current plot using the plt.axis method
plt.plot(x, np.sin(x)) 
plt.axis('tight')

# %%
# Code to demonstrate ensuring an equal aspect ratio using the plt.axis
plt.plot(x, np.sin(x)) 
plt.axis('equal')

# %% [markdown] lang="en" tags=["slide"]
# ## Labeling Plots
# - Labeling plots is a crucial aspect to make them understandable and interpretable.
# - In the next section, we'll discuss how to properly label your plots.# %% [markdown] lang="en" tags=["slide"]
# ## Labeling Plots
# - Plot labeling involves adding various labels like titles, axis labels, and legends to plots.
# - Titles and Axis labels can be quickly added to the plots using specific methods.
# - These labels can be customized in terms of their position, size, and style.

# %% 
import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");

# %% [markdown] lang="en" tags=["slide"]
# ## Labeling Plots (Contd.)
# - When plotting multiple lines within a single plot, it may be beneficial to have a legend that labels each line type.
# - Matplotlib offers a built-in method, `plt.legend()`, for quickly creating such a legend.
# - The `label` keyword of the plot function can be used to specify the label for each line.

# %% 
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend();

# %% [markdown] lang="en" tags=["slide"]
# ## Labeling Plots (Contd.)
# - The `plt.legend()` function keeps a record of the line style and color and matches these with the correct label.
# - More information about how to specify and format plot legends can be found in the `plt.legend` docstring.
# - In upcoming sections we will also cover some more advanced options for plot legends.

# %% [markdown] lang="en" tags=["slide"]
# ## Aside: Matplotlib Gotchas
# - In the process of working with Matplotlib, you might encounter some unexpected behaviours or limitations, also often referred as "gotchas".
# - In this section, we'll delve into some of these potential issues that one might encounter while using Matplotlib for creating visualizations.# %% [markdown] lang="en" tags=["slide"]
# ## Matplotlib Gotchas
# - Many `plt` functions translate directly to similar commands for `ax` objects (like `plt.plot()` → `ax.plot()`, `plt.legend()` → `ax.legend()` etc).
# - However, some function translation isn't straightforward. Particularly, those to set labels, limits, and titles have slight modifications.
# - Transitioning between MATLAB-style and object-oriented methods, various changes have to be noted.
# - In the object-oriented interface, it's often convenient to use `ax.set()` method to set all properties at once.

# %% 
# A simple plot with the ax.set() method
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2), xlabel='x', ylabel='sin(x)', title='A Simple Plot');