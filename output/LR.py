""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Lineare Regression", "Linear Regression") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Linear Regression is a fundamental concept in Machine Learning.
# - It is a simple yet powerful algorithm that helps us understand relationships between variables.

""" Code cell """
# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

plt.scatter(x, y,s=10)
plt.xlabel('x')
plt.ylabel('y')

lr_model = LinearRegression()
lr_model.fit(x, y)
y_predicted = lr_model.predict(x)
plt.plot(x, y_predicted, color='r')
plt.show()

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formale Definition
# - Linear regression is a linear approach for modeling the relationship between a scalar dependent variable y and one or more independent variables denoted X.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Anwendung
# - Predictive Analysis
# - Trendline in Stock Market Analysis

""" Code cell """
# %%
features = np.array([[1], [2], [3], [4], [5]])
labels = np.array([[2], [4], [6], [8], [10]])

lr = LinearRegression()
lr.fit(features, labels)

test_features = np.array([[10], [11]])
predictions = lr.predict(test_features)

print("Predictions: ", predictions)

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Einschränkungen
# - It assumes a linear relationship between dependent and independent variables, which is not always the case in real-world situations.
# - It is sensitive to outliers.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Hands-On Workshop
# - Analyze the relationship between temperature and ice-cream sales using the dataset provided.
# - Fit a linear regression model to the data.
# - Predict the ice-cream sales for a given temperature.

