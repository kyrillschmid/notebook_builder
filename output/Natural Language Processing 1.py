""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Natürliche Sprachverarbeitung", "Natural Language Processing") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Processing and understanding natural language, i.e., the language that humans use daily, has been a challenging task in the field of Artificial Intelligence.
# - Natural Language Processing (NLP) involves converting human languages into a form that computers can understand. It can be used to extract meaning and insights from text data in a smart and efficient manner.

""" Code cell """
# %%
# Let's see a simple example of tokenization - one of the most basic NLP tasks
sentence = "Machine learning is fascinating."
tokens = sentence.split()
print(tokens)

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Code Explanation
# - Here, our task was to tokenize the sentence, which means splitting the sentence into individual words.
# - This serves as the basic building block for more advanced NLP tasks such as sentiment analysis, language translation, etc.

""" Code cell """
# %%
# Another example - Counting the frequency of words
from collections import Counter

words_frequency = Counter(tokens)
print(words_frequency)

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Code Explanation
# - In this example, we're counting the frequency of each word in the sentence.
# - Understanding the frequency of words can help in understanding the context or subject of the sentence in a larger text corpus.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formal Definition
# - Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language. In NLP, several problems are tackled as mentioned earlier.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Sentiment Analysis
# - Sentiment analysis is used to determine the emotional tone behind words. 
# - This is useful in cases where we want to identify the mood from a text data.

""" Code cell """
# %%
# Sample code for performing sentiment analysis using NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("I love machine learning."))

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Text Summarization
# - Text summarization is the process of distilling the most important information from a source.
# - This can be useful in summarizing news articles, reports, thesis, etc.

""" Code cell """
# %%
# Sample code for performing text summarization using Gensim library
from gensim.summarization import summarize

text = "Your text document goes here. Make sure it's lengthy."
print(summarize(text))

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations of NLP
# - NLP is not 100% accurate due to the complexities and irregularities in languages.
# - Handling context, sarcasm, word-sense disambiguation, etc. are some of the challenges faced in NLP.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Hands-on Workshop
# - Try out different NLP techniques using libraries such as NLTK, Spacy, or Gensim.
# - Experiment with different texts and try to understand the results. Be aware of the limitations and challenges faced in NLP.

