""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Perceptron", "Perceptron") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - The Perceptron is one of the simplest forms of a neural network, designed for binary classification problems.
# - It provides the foundation for more complex neural algorithms and is perfect to get a basic understanding of machine learning.

""" Code cell """
# %%
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron

# Create a simple binary classification problem 
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0,
                           n_clusters_per_class=1, random_state=4)

# Create Perceptron model
model = Perceptron(max_iter=1000)
model.fit(X, y)
print(f"Model Score: {model.score(X, y)}")

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Definition
# - A Perceptron is an algorithm for supervised learning of binary classifiers. 
# - This algorithm enables neurons to learn and process elements in the training set one at a time.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Binary Classification
# - A key application of Perceptron is to classify observations into one of two groups.
# - It is commonly used in natural language processing to classify text (e.g., spam/non-spam emails).

""" Code cell """
# %%
from sklearn.feature_extraction.text import CountVectorizer

corpus = ['This is the first document.',
          'This document is the second document.',
          'And this is the third one.',
          'Is this the first document?']
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = np.array([1, 2, 1, 1])

# Create Perceptron model
model = Perceptron(max_iter=1000)
model.fit(X, y)
print(f"Model Score: {model.score(X, y)}")

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations
# - Perceptron has a major limitation in that it works only with linearly separable classes.
# - It doesn't perform well when dealing with complex datasets where classes cannot be separated by a simple linear decision boundary.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Workshop: Implementing a Perceptron from Scratch
# A hands-on workshop guiding you through the steps to implement a Perceptron from scratch, analyze its performance, and understand its shortcomings.

