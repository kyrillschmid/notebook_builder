""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Einführung in Neuronale Netzwerke", "Introduction to Neural Networks") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation 
# - Neural Networks can optimize complex functions by learning from training data
# - They can be applied in various fields such as image recognition, language processing and game playing 

""" Code cell """
# %%
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlp = MLPClassifier(hidden_layer_sizes=(64,64), max_iter=50, alpha=1e-4, solver='sgd', verbose=10, tol=1e-4, random_state=1, learning_rate_init=.1)
mlp.fit(X_train, y_train)
print(f"Training set score: {mlp.score(X_train, y_train)}")
print(f"Test set score: {mlp.score(X_test, y_test)}")

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formal Definition
# - A neural network is a network or circuit of neurons, composed of artificial neurons or nodes
# - It changes its structure based on input and output and can compute a target class given an input vector

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Image Recognition
# - Neural Networks are widely used for image recognition tasks, as they can parse hierarchical features

""" Code cell """
# %%
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

(X_train, y_train), (X_test, y_test) = mnist.load_data()
num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')
X_train = X_train / 255
X_test = X_test / 255
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

model = Sequential()
model.add(Dense(num_pixels, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_test, y_test))

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations
# - Neural networks can be complex and computationally expensive
# - They require large volumes of labeled data 
# - They can be sensitive to irrelevant features

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Hands-On Workshop
# - Implement a simple neural network for a classification problem
# - Analyze its performance using different metrics
# - Tweak its parameters and structure to enhance its performance

