# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# # Simple Scatter Plots
# - Scatter plots are a common type of plot similar to line plots.
# - Instead of joining points with line segments as in line plots, scatter plots represent individual points with dots, circles, or other shapes.
# - In this section, we'll start by setting up the notebook for plotting and importing the necessary modules.
# - We'll then dive into creating scatter plots using Matplotlib.

# %%
# Importing necessary libraries
import matplotlib.pyplot as plt

# Setting plot style
plt.style.use('seaborn-whitegrid')

import numpy as np

# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with `plt.plot`
# - plt.plot can also be used to create scatter plots
# - This is done by modifying the third argument for the function
# - Here, we can use character codes to define the nature of the plot
# - For instance, 'o' would generate a dot plot. 
# - Let's dive into some examples.# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with plt.plot
# - In addition to line plots, the `plt.plot` function can be used to generate scatter plots
# - The third argument in the function call defines the type of marker used for the plotting
# - Just like line style can be controlled using options such as '-', '--', the marker style can be controlled using string codes
# - These marker style codes and their inputs can be seen in the `plt.plot` documentation

# %% 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black')

# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plot Markers
# - There are numerous types of markers that can be used in scatter plots
# - We can present a few examples like 'o', '.', ',', 'x', '+', 'v', etc.
# - Beyond these, you can use a mix of line, color and character codes to design more complex plots
# - The `plt.plot` function offers flexibility for a wide range of visualization options

# %%
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

# %%

plt.plot(x, y, '-ok')

# %% [markdown] lang="en" tags=["slide"]
# ## Properties of Lines and Markers
# - There are additional keyword arguments to `plt.plot` that help specify various properties of lines and markers
# - For example, color, markersize, linewidth, etc.
# - These properties allow the user to craft detailed, personalized visualizations using matplotlib
# - Please refer the `plt.plot` documentation for a complete list of the options available.

# %%
plt.plot(x, y, '-p', color='gray', markersize=15, linewidth=4, 
         markerfacecolor='white', markeredgecolor='gray', markeredgewidth=2)
plt.ylim(-1.2, 1.2)

# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with plt.scatter
# - Beyond `plt.plot`, matplotlib provides another function for creating scatter plots, `plt.scatter`
# - The `plt.scatter` function provides some advantages over `plt.plot` for certain use-cases but also has its limitations
# - In the following section, we will explore scatter plots using `plt.scatter` in more detail
# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with `plt.scatter`
# - `plt.scatter` is a powerful tool for creating scatter plots and is similar in use to `plt.plot`
# - The unique aspect about `plt.scatter` is that it allows customization of each individual point (size, color, edge color)
# - It can be used to represent multidimensional data where various properties of points convey different dimensions
# - For instance, color and size can be set to different variables, enabling visualisation of more than two variables per scatter plot

# %% 
plt.scatter(x, y, marker='o') # basic usage of plt.scatter

# %% [markdown] lang="en" tags=["slide"]
# - To demonstrate its capabilities, let's plot a random scatter plot with points of many colors and sizes
# - We also use the `alpha` parameter to adjust the transparency level to visibly see overlapping points
# - The `color` argument is mapped to a color scale which can be shown using `colorbar()` command
# - The `size` argument specifies the size of points in pixels

# %%
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar() # show color scale

# %% [markdown] lang="en" tags=["slide"]
# - For example, let's visualize Iris data from Scikit-Learn that has petal and sepal sizes of three types of flowers
# - We can plot the sepal length and width on x, y axes, the petal width can be tied to the size of each point, and the type of flower tied to the color of each point
# - Multicolor and multifeature scatter plots like this can be very useful for data exploration and presentation

# %%
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2, 
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# %% [markdown] lang="en" tags=["slide"]
# ## `plot` Versus `scatter`: A Note on Efficiency
# - It is important to note the difference in efficiency between `plt.plot` and `plt.scatter`
# - Although `plt.scatter` allows high level of customization, it can be close to an order of magnitude slower than `plt.plot`
# - Therefore, for large datasets, it is recommended to favor `plt.plot` over `plt.scatter` whenever possible# %% [markdown] lang="en" tags=["slide"]
# ## `plot` Versus `scatter`: A Note on Efficiency
# - Both `plt.plot` and `plt.scatter` are used to graph data but their usage depends upon the size of data.
# - For smaller datasets, the difference in performance between `plt.plot` and `plt.scatter` isn't quite significant.
# - However, as datasets become larger (more than a few thousand points), `plt.plot` can be more efficient due to the way it renders data points.

# %% [markdown] lang="en" tags=["slide"]
# ## Details about `scatter` and `plot`
# - The `plt.scatter` function has the capability to render different size and/or color for each point, therefore, it constructs each point individually.
# - On the other hand, in `plt.plot`, the data points are clones of each other, so it determines the appearance of the points only once for the whole set.
# - Due to this fundamental difference, `plt.plot` offers better performance for large datasets and is generally preferred over `plt.scatter` in such scenarios.# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# # What is Machine Learning?
# - Machine learning can be thought of as a subfield of artificial intelligence but is better described as a method for building data models.
# - The concept of "learning" comes from giving these models adjustable parameters that adapt to observed data, and thereby "learn" from it.
# - These fitted models can be used to predict and comprehend aspects of future observed data.

# %% [markdown] lang="en" tags=["slide"]
# - Understanding the machine learning problem setting is vital for effectively using these tools. 
# - It is a mix of the practical and philosophical, whether the mathematical, model-based "learning" of machine learning algorithms can compare to human learning.
# - Up next, we will delve into some broad categories of machine learning approaches.

# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - Machine Learning techniques can be broadly categorised, which we will discuss further.# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - Machine learning can be broadly classified into two categories: Supervised Learning and Unsupervised Learning.

# %% [markdown] lang="en" tags=["slide"]
# - **Supervised learning** involves modeling the relationship between the features of the data and some label associated with the data.
#  - Once this model is established, it can be used to assign labels to new or unfamiliar data.
#  - There are two main types of supervised learning: **Classification** and **Regression**.
#    - In Classification, the labels are discrete categories.
#    - While in Regression, the labels are continuous quantities.

# %% [markdown] lang="en" tags=["slide"]
# - **Unsupervised learning** involves the processing of a dataset without referring to any label.
#    - This type of learning approach is often described as enabling a dataset to represent itself.
#  - Unsupervised learning involves tasks such as **Clustering** and **Dimensionality Reduction**.
#    - Clustering algorithms help to identify distinct groups within the data.
#    - Dimensionality reduction algorithms strive to find succinct representations of the data.

# %% [markdown] lang="en" tags=["slide"]
# - Another type of machine learning strategy is **Semi-supervised learning**.
#    - These methods fall somewhere between Supervised Learning and Unsupervised Learning.
#    - These methods are particularly beneficial when are only partially available labels.

# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
# - As we proceed, we will delve into examples of uses of these machine learning strategies.# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
# - Machine learning tasks can be broadly categorised into: Classification, Regression and Unsupervised learning
# - We will be looking at simple examples to get an intuitive understanding of these tasks
# - The more technical aspects of the models will be explored in later sections

# %% [markdown] lang="en" tags=["slide"]
# ## Classification tasks in machine learning
# - Classification tasks involve labelling unlabeled data points based on a set of labeled points
# - Classification is usually performed when the data has discrete class labels
# - The goal of the classification model is to find a line or boundary that separates different classes

# %% [markdown] lang="en" tags=["slide"]
# ## Training and prediction in machine learning
# - Machine learning involves learning model parameters from the data, this stage is often referred to as 'training the model'
# - Once the model is trained, it can be generalised to new, unlabeled data for prediction
# - An example of a classification task is email spam detection

# %% [markdown] lang="en" tags=["slide"]
# ## Regression tasks in machine learning
# - Regression tasks differ from classification tasks as the labels in regression are continuous quantities
# - Regression models predict a continuous output based on input features
# - Linear regression model takes two-dimensional data and assumes a plane can be fitted to the data

# %% [markdown] lang="en" tags=["slide"]
# ## Unsupervised learning in machine learning
# - Unsupervised learning models describe data without referring to any known labels
# - An example of unsupervised learning is "clustering", where data points are automatically assigned to some number of discrete groups
# - Another example is dimensionality reduction, which seeks to pull out a low dimensional representation of the data

# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - Machine learning tasks include Classification, Regression, and Unsupervised learning
# - Classification involves labelling data points based on a set of labels
# - Regression involves predicting a continuous value, while Unsupervised learning involves automatically partitioning data into groups or reducing its dimensionality# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - We saw examples of basic types of machine learning approaches, covering supervised and unsupervised learning
# - Supervised learning predicts labels based on labeled training data
# - Unsupervised learning identifies structure in unlabeled data
# - In subsequent sections, we will explore these categories in greater depth and see interesting examples. 

# Note: All figures are generated from actual machine learning computations. The code for these can be found in .# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# # What Is Machine Learning?
# - Machine learning is often considered a subset of artificial intelligence.
# - However, within the context of data science applications, machine learning can be better described as a method for building models of data.

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Machine Learning
# - Machine learning involves constructing mathematical models to aid in data comprehension.
# - The term "learning" comes into play when we provide these models with tunable parameters that adjust based on observed data, hence the program can be said to "learn" from the data.
# - Once these models have been calibrated to previously observed data, they can be employed to predict and comprehend aspects of newly encountered data.

# %% [markdown] lang="en" tags=["slide"]
# ## Machine Learning Context 
# - Comprehending the problem setting in machine learning is vital for the effective use of these tools.
# - Therefore, we will commence with some broad classifications of the types of strategies we will discuss.

# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - The categories of Machine Learning form the basis for understanding different models and methodologies.
# - We will delve deeper into the different categories in the upcoming sections.# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - Machine learning broadly falls into two categories: supervised learning and unsupervised learning
# - Supervised learning involves creating a model that strains relationships between features and labels in the data
#   - It is further divided into: classification (discrete categories labels) and regression (continuous quantity labels)

# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning contd..
# - Unsupervised learning, on the other hand, models features of a dataset without any label reference
#   - Unsupervised learning includes tasks such as clustering (identifying distinct data groups) and dimensionality reduction (searching for succinct data representations)
# - Semi-supervised learning methods, resting between supervised and unsupervised learning, can be useful when labels are incompletely available

# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
# - The next section will provide examples of these categories of machine learning, displaying their practical applications in action# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
# - Overview of types of machine learning tasks using simple qualitative examples
# - These tasks can include classification, regression, and unsupervised learning tasks like clustering and dimensionality reduction
# - We'll discuss the concept behind each task, illustrate with a simple example, and introduce some associated algorithms

# %% [markdown] lang="en" tags=["slide"]
# ## Classification
# - In a classification task, you're given a set of features and labels for each data point
# - The goal is to create a model that can correctly classify new, unlabeled data based on the learned features and associated labels
# - An example is depicted below, where a straight line separates two classes of data:

# %% [markdown] lang="en" tags=["slide"]
# ## Classification (Continued)
# - The location and orientation of the separating line constitutes the quantitative model and its parameters
# - These parameters are learned from the data, a process often referred to as "training the model"
# - Once trained, the model can be used to predict labels for new, unlabeled data, a stage usually called "prediction"

# %% [markdown] lang="en" tags=["slide"]
# ## Classification Use Case: Spam Detection
# - An example of a real-life classification task is automated spam detection for emails
# - The features could be thousands or millions of words or phrases from the emails, and the labels would indicate whether an email is spam or not
# - Some important classification algorithms we'll discuss are Gaussian naive Bayes, support vector machines, and random forest classification

# %% [markdown] lang="en" tags=["slide"]
# ## Regression
# - In a regression task, the labels are continuous quantities instead of discrete classes
# - A simple example is predicting the continuous labels for a set of points based on two-dimensional features
# - A possible model for this is a simple linear regression, which assumes that a plane can fit the data

# %% [markdown] lang="en" tags=["slide"]
# ## Regression (Continued)
# - The plane of fit forms the model which can predict labels for new points
# - Like with classification, regression methods can be applied to data with many features
# - Real life example include predicting distances to galaxies observed through a telescope based on various features
# - Some key regression algorithms are linear regression, support vector machines, and random forest regression

# %% [markdown] lang="en" tags=["slide"]
# ## Unsupervised Learning: Clustering
# - Clustering is an unsupervised machine learning task where data is automatically grouped into discrete clusters based on the intrinsic structure of the data
# - A common and intuitive algorithm for this is the k-means algorithm
# - It fits a model consisting of k cluster centers optimized to minimize the distance of each point from its assigned center

# %% [markdown] lang="en" tags=["slide"]
# ## Unsupervised Learning: Dimensionality Reduction
# - Dimensionality reduction is another type of unsupervised learning where labels or information are deduced from the structure of the dataset itself
# - It seeks to represent data in a lower-dimensional space while preserving relevant qualities of the full dataset
# - For example, one-dimensional data arranged in a spiral within a two-dimensional space can be represented in just one dimension
# - The Isomap algorithm, a manifold learning algorithm, could achieve this

# %% [markdown] lang="en" tags=["slide"]
# ## Dimensionality Reduction (Continued)
# - The power of dimensionality reduction algorithms becomes clearer in higher-dimensional cases
# - The goal might be to visualize important relationships within a dataset with many features by reducing the data to two or three dimensions
# - Some popular dimensionality reduction algorithms include principal component analysis, and manifold learning algorithms like Isomap and locally linear embedding

# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - Covered the principles behind different types of machine learning tasks and illustrate with simple examples
# - Also introduced some common algorithms associated with each type of task
# - While the examples used were simple, the methods discussed can be applied to much larger and complex datasets.# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - The basic types of machine learning approaches have been illustrated by a few examples in this section.
# - Important practical details have been omitted, but the main objective was to provide a fundamental understanding of machine learning problem-solving.

# %% [markdown] lang="en" tags=["slide"]
# - Supervised learning: These models can predict labels based on labeled training data.
# - Unsupervised learning: These models identify structure in unlabeled data.
# - In the upcoming sections, we will delve further into these categories and provide more intriguing examples of their applications.

# %% [markdown] lang="en" tags=["slide"]
# - All figures presented are generated from actual machine learning computations.
# - Refer to the code samples accompanying each figure for a more detailed understanding.# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# ## What Is Machine Learning?
- Machine learning is a subfield of artificial intelligence focused on building models of data
- It involves building mathematical models with tunable parameters that can be adapted to observed data
- Once models have been fit to previously seen data, they can be used to predict and understand aspects of newly observed data
- Understanding the problem setting in machine learning is essential to using these tools effectively

# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
- Supervised learning: the algorithm learns from labeled training data, making predictions on unseen data
- Unsupervised learning: the algorithm learns from data without being given correct answers, finding patterns and relationships
- Reinforcement learning: the algorithm learns the best course of action from feedback from the environment# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - Machine learning can be categorized into two main types: supervised learning and unsupervised learning
# - Supervised learning entails modeling the relationship between measured features of data and some label associated with the data
#   - This is further subdivided into classification tasks and regression tasks
# - In classification, the labels are discrete categories, while in regression, the labels are continuous quantities
# - Unsupervised learning involves modeling the features of a dataset without reference to any label
#   - It is often described as "letting the dataset speak for itself"
# - Unsupervised learning includes tasks such as clustering and dimensionality reduction
#   - Clustering algorithms identify distinct groups of data, while dimensionality reduction algorithms search for more succinct representations of the data
# - In addition, there are semi-supervised learning methods, which falls somewhere between supervised learning and unsupervised learning
#   - These methods are often useful when only incomplete labels are available

# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
- Simple examples of machine learning tasks
- Classification and regression tasks
- Visual representations of trained models
- Supervised and unsupervised learning algorithms
- Important algorithms for classification, regression, clustering, and dimensionality reduction# %% [markdown] lang="en" tags=["slide"]
# ## Summary
- Machine learning approaches can solve various types of problems
- Supervised learning models predict labels based on training data
- Unsupervised learning models identify structure in unlabeled data
- The upcoming sections will delve deeper into these categories
- Figures in this discussion are based on actual machine learning computations# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# ## What Is Machine Learning?
- Machine learning is a means of building models of data
- It involves building mathematical models with tunable parameters that can be adapted to observed data
- Once models have been fit to previously seen data, they can be used to predict and understand aspects of newly observed data

# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning

# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - At the most fundamental level, machine learning can be categorized into two main types: supervised learning and unsupervised learning
#   - Supervised learning involves modeling the relationship between measured features of data and some label associated with the data, and can be subdivided into classification tasks and regression tasks
#   - Unsupervised learning involves modeling the features of a dataset without reference to any label, and includes tasks such as clustering and dimensionality reduction
# - Additionally, there are semi-supervised learning methods, which fall somewhere between supervised learning and unsupervised learning and are often useful when only incomplete labels are available

# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
# - Very simple examples of a machine learning task are presented
# - Tasks are meant to give an intuitive, non-quantitative overview of the types of machine learning tasks 
# - We will delve into the particular models and how they are used in later sections
# - Python source code that generates these figures is available
# - First look at a simple classification task where labeled points are given to classify unlabeled points# %% [markdown] lang="en" tags=["slide"]
# ## Summary
- We have seen simple examples of basic types of machine learning approaches
- Important practical details were glossed over, but we covered the basic idea of problems machine learning can solve
- We saw the following:
  - *Supervised learning*: Models predict labels based on labeled training data
  - *Unsupervised learning*: Models identify structure in unlabeled data
- In the following sections, we will delve deeper into these categories and explore more interesting examples
- All figures in the discussion are generated based on actual machine learning computations

# %% [markdown] lang="en" tags=["slide"]
# ## Summary (Continued)
- The code behind the figures can be found in [add_code_link_here]
- In summary, machine learning approaches provide solutions for predicting labels based on training data and identify patterns in unlabeled data
- We will explore more examples and delve deeper into the categories of supervised and unsupervised learning in the following sections# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# ## What Is Machine Learning?
- Machine learning is a subfield of artificial intelligence but is more helpful to think of machine learning as a means of building models of data in the context of data science
- It involves building mathematical models to help understand data and learning from the data when models have tunable parameters
- Once the models have been fit to previously seen data, they can be used to predict and understand aspects of newly observed data
- Understanding the problem setting in machine learning is essential to using these tools effectively
# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
- Introduction to the broad categorizations of the types of approaches we'll discuss in machine learning# %% [markdown] lang="en" tags=["slide"]
# ## Categories of Machine Learning
# - Machine learning can be categorized into two main types: supervised learning and unsupervised learning
# - Supervised learning involves modeling the relationship between measured features of data and a label associated with the data
#   - This is further subdivided into classification tasks and regression tasks
# - In classification, the labels are discrete categories, while in regression, the labels are continuous quantities
# - Unsupervised learning involves modeling the features of a dataset without reference to any label
#   - This includes tasks such as clustering and dimensionality reduction
# - Clustering algorithms identify distinct groups of data, while dimensionality reduction algorithms search for more succinct representations of the data
# - There are also semi-supervised learning methods, which fall between supervised and unsupervised learning
#   - These methods are useful when only incomplete labels are available

# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications# %% [markdown] lang="en" tags=["slide"]
# ## Qualitative Examples of Machine Learning Applications
# - Machine learning tasks are illustrated with qualitative examples
# - A classification task is demonstrated with a simple model separating two groups of points by a straight line
# - The concept of model training and prediction is introduced
# - Regression task is showcased with a simple linear regression model predicting continuous labels for points
# - Supervised and unsupervised learning algorithms are discussed
# - Important classification, regression, clustering, and dimensionality reduction algorithms are mentioned# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - We have seen simple examples of basic machine learning approaches
# - This section gives a basic idea about the problems machine learning approaches can solve
# - Types of machine learning approaches:
#   - Supervised learning: Models predict labels based on labeled training data
#   - Unsupervised learning: Models identify structure in unlabeled data
# - The following sections will delve deeper into these categories and provide more interesting examples
# - All figures in the discussion are generated based on actual machine learning computations

# %% [markdown] lang="en" tags=["slide"]
# - Code behind the figures can be found in the document indicated in the text