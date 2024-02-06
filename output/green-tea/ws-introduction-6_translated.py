# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Formal and Natural Languages

# %% [markdown] lang="de" tags=["subslide"]
# ## Mini-Workshop: Formale und natürliche Sprachen

# %% [markdown] lang="en"
#
# ### Understanding Languages
#
# A brief exploration of the differences between natural and formal languages.

# %% [markdown] lang="de"
# ### Verständnis von Sprachen
#
# Eine kurze Erkundung der Unterschiede zwischen natürlichen und formalen Sprachen.

# %% [markdown] lang="en"
#
# **Task 1:** Create a function `is_natural_language(language)` that returns `True` for natural languages ('English', 'Spanish', 'French') and `False` for others.


# %% [markdown] lang="de"
# **Aufgabe 1:** Erstellen Sie eine Funktion `is_natural_language(sprache)`, die `True` für natürliche Sprachen ('Englisch', 'Spanisch', 'Französisch') und `False` für andere zurückgibt.

# %%
def is_natural_language(language):
    natural_languages = ["English", "Spanish", "French"]
    return language in natural_languages


# %% [markdown] lang="en" tags=["subslide"]
#
# Write an assertion that checks if 'Python' is considered a formal or natural language by your function.

# %% [markdown] lang="de" tags=["subslide"]
# Schreiben Sie eine Behauptung, die überprüft, ob 'Python' von Ihrer Funktion als formale oder natürliche Sprache betrachtet wird.

# %%
assert not is_natural_language(
    "Python"
)  # 'Python' is a formal language, not a natural one.

# %% [markdown] lang="en" tags=["subslide"]
# **Task 2:** Create a function `is_formal_language(sentence)` that returns `True` if the provided sentence adheres to formal language syntax (for simplicity, let's assume formal syntax means does not contain '$' or '@' symbols) and `False` otherwise.


# %% [markdown] lang="de" tags=["subslide"]
# **Aufgabe 2:** Erstellen Sie eine Funktion `is_formal_language(sentence)`, die `True` zurückgibt, wenn der bereitgestellte Satz der Syntax formaler Sprache entspricht (vereinfacht ausgedrückt bedeutet formale Syntax, dass keine '$' oder '@' Symbole enthalten sind) und andernfalls `False`.

# %%
def is_formal_language(sentence):
    return "$" not in sentence and "@" not in sentence


# %% [markdown] lang="en" tags=["subslide"]
# Test the `is_formal_language()` function with the following sentences:
# - "This is @ well-structured Engli$h sentence with invalid t*kens in it."
# - "3 + 3 = 6"

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie die Funktion `is_formal_language()` mit den folgenden Sätzen:
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

# %% [markdown] lang="de" tags=["subslide"]
# **Aufgabe 3:** Reflektion über Syntax und Struktur
#
# Betrachten Sie die Definition formaler Sprachen und überlegen Sie, warum Programmiersprachen wie Python als formale Sprachen betrachtet werden. Denken Sie über die Rolle von Ambiguität, Redundanz und Wörtlichkeit in der Programmierung nach.

# %% [markdown] lang="en"
# *Your reflection here*

# Example Reflection:
# "Programming languages like Python are considered formal languages because they have strict syntax rules and are designed to be unambiguous. In programming, ambiguity can lead to unexpected behavior or errors, hence the necessity for clear and precise language. Unlike natural languages where idioms and metaphors enrich communication, programming languages benefit from being literal as this ensures the intended operations are performed exactly as the programmer specifies. This literalness and lack of ambiguity allow computers to execute code reliably and efficiently."

# %% [markdown] lang="de"
# *Ihre Reflexion hier*

# Beispielreflexion:
# "Programmiersprachen wie Python gelten als formale Sprachen, da sie strenge Syntaxregeln haben und darauf ausgelegt sind, eindeutig zu sein. In der Programmierung kann Mehrdeutigkeit zu unerwartetem Verhalten oder Fehlern führen, daher die Notwendigkeit einer klaren und präzisen Sprache. Im Gegensatz zu natürlichen Sprachen, in denen Redewendungen und Metaphern die Kommunikation bereichern, profitieren Programmiersprachen davon, wörtlich zu sein, da so sichergestellt wird, dass die beabsichtigten Operationen genau so ausgeführt werden, wie der Programmierer angibt. Diese Wörtlichkeit und fehlende Mehrdeutigkeit ermöglichen es Computern, Code zuverlässig und effizient auszuführen."

# %% [markdown] lang="en" tags=["subslide"]
#
# Congratulations! You have completed the mini-workshop on understanding the differences between formal and natural languages.
# %% [markdown] lang="de" tags=["subslide"]
#
# Glückwunsch! Sie haben den Mini-Workshop zur Unterscheidung zwischen formalen und natürlichen Sprachen abgeschlossen.

