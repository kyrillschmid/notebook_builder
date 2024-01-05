""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Natürliche Sprachverarbeitung", "Natural Language Processing") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# # Motivation for Natural Language Processing
# - Natural Language Processing (NLP) is a fundamental aspect of artificial intelligence that helps computers understand, interpret and manipulate human language.
# - It allows machines to communicate with people in their own language and scale other language-related functions, such as automatically translating web pages into different languages, and many more.

""" Code cell """
# %%
# Importing required libraries
from nltk.corpus import brown
# Fetching a small sample of data
data_sample = brown.sents(categories='news')[:2]
data_sample

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# # Motivational code example
# These lines of code demonstrate how we can use Python’s NLTK library to fetch a small sample of text data.

""" Code cell """
# %%
from nltk.tokenize import word_tokenize
# Tokenization of the first sentence
tokens = word_tokenize(' '.join(data_sample[0]))
tokens

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formal Definition of NLP
# - Natural Language Processing (NLP) is a subfield of computer science, artificial intelligence, and computational linguistics that focuses on interactions between computers and human languages.
# - It consists of several tasks including parsing, machine translation, natural language understanding and generation, etc.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Applications of NLP
# - Text Translation
# - Sentiment Analysis
# - Speech Recognition

""" Code cell """
# %%
# Using NLTK's in-built machine translation functionality
from nltk.translate.bleu_score import sentence_bleu
reference = word_tokenize('It is a nice day')
candidate = word_tokenize('It is a good day')
score = sentence_bleu([reference], candidate)
score

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations of NLP
# - Sarcasm and irony are not well understood by NLP models.
# - Often struggles with understanding cultural nuances and slang.
# - Difficulty in parsing sentences with complex structures.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# # Hands-On Workshop on NLP
# We will perform textual data cleaning, tokenization, and lemmatization using Python's NLTK (Natural Language Toolkit) library. Following that, we will use Word2Vec to develop a model for word representation. We will then create a text classification model using the BERT transformer. Let's start!

