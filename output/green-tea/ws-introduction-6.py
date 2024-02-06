# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Formal and Natural Languages

# %% [markdown] lang="en"
#
# ### Understanding Languages
#
# A brief exploration of the differences between natural and formal languages.

# %% [markdown] lang="en"
#
# **Task 1:** Create a function `is_natural_language(language)` that returns `True` for natural languages ('English', 'Spanish', 'French') and `False` for others.


# %%
def is_natural_language(language):
    natural_languages = ["English", "Spanish", "French"]
    return language in natural_languages


# %% [markdown] lang="en" tags=["subslide"]
#
# Write an assertion that checks if 'Python' is considered a formal or natural language by your function.

# %%
assert not is_natural_language(
    "Python"
)  # 'Python' is a formal language, not a natural one.

# %% [markdown] lang="en" tags=["subslide"]
# **Task 2:** Create a function `is_formal_language(sentence)` that returns `True` if the provided sentence adheres to formal language syntax (for simplicity, let's assume formal syntax means does not contain '$' or '@' symbols) and `False` otherwise.


# %%
def is_formal_language(sentence):
    return "$" not in sentence and "@" not in sentence


# %% [markdown] lang="en" tags=["subslide"]
# Test the `is_formal_language()` function with the following sentences:
# - "This is @ well-structured Engli$h sentence with invalid t*kens in it."
# - "3 + 3 = 6"

# %%
assert not is_formal_language(
    "This is @ well-structured Engli$h sentence with invalid t*kens in it."
)
assert is_formal_language("3 + 3 = 6")

# %% [markdown] lang="en" tags=["subslide"]
# **Task 3:** Reflecting on Syntax and Structure
#
# Considering the definition of formal languages, reflect on why programming languages like Python are considered formal languages. Think about the role of ambiguity, redundancy, and literalness in programming.

# %% [markdown] lang="en"
# *Your reflection here*

# Example Reflection:
# "Programming languages like Python are considered formal languages because they have strict syntax rules and are designed to be unambiguous. In programming, ambiguity can lead to unexpected behavior or errors, hence the necessity for clear and precise language. Unlike natural languages where idioms and metaphors enrich communication, programming languages benefit from being literal as this ensures the intended operations are performed exactly as the programmer specifies. This literalness and lack of ambiguity allow computers to execute code reliably and efficiently."

# %% [markdown] lang="en" tags=["subslide"]
#
# Congratulations! You have completed the mini-workshop on understanding the differences between formal and natural languages.
