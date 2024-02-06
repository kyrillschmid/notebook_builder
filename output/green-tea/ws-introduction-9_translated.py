# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Introduction to Python Errors

# %% [markdown] lang="de" tags=["subslide"]
#
# ## Mini-Workshop: Einführung in Python-Fehler

# In diesem Mini-Workshop werden wir uns mit Python-Fehlern befassen und lernen, wie man sie liest und versteht. 

# ### Fehlermeldungen verstehen

# Bevor wir in die Fehlerbehandlung in Python einsteigen, ist es wichtig, die verschiedenen Arten von Fehlermeldungen zu verstehen, die auftreten können. 

# Es gibt drei Haupttypen von Fehlern in Python:
# - Syntaxfehler
# - Ausnahmefehler (Exceptions)
# - Semantische Fehler

# Syntaxfehler treten auf, wenn der Python-Interpreter den Code nicht verstehen kann, da er nicht der richtigen Syntax folgt. Diese Art von Fehler wird in der Regel durch Tippfehler verursacht.

# Ausnahmefehler treten während der Programmausführung auf und zeigen an, dass etwas Unerwartetes passiert ist, das Python nicht verarbeiten kann. Zum Beispiel tritt ein `ZeroDivisionError` auf, wenn versucht wird, durch Null zu teilen.

# Semantische Fehler sind die schwierigsten zu finden, da der Code ohne Fehlermeldung ausgeführt wird, aber das Ergebnis nicht das ist, was erwartet wurde. Diese Art von Fehler kann auf Fehler in der Logik des Codes zurückzuführen sein.

# ### Fehlerbehandlung in Python

# In Python können Fehler mit `try` und `except` behandelt werden. Dies ermöglicht es uns, spezifische Fehler abzufangen und entsprechend zu reagieren, anstatt dass das Programm einfach abstürzt. 

# Hier ist ein Beispiel für die Verwendung von `try` und `except`:

```python
try:
    # Hier steht der Code, in dem ein Fehler auftreten könnte
    x = 1 / 0
except ZeroDivisionError:
    # Hier wird angegeben, was passieren soll, wenn ein ZeroDivisionError auftritt
    print("Division by zero is not allowed")
```

# In diesem Beispiel wird versucht, `1` durch `0` zu teilen, was einen `ZeroDivisionError` verursachen würde. Anstatt dass das Programm abstürzt, wird die Meldung "Division by zero is not allowed" ausgegeben.

# %% [markdown] lang="en"
#
# As part of this exercise, we'll explore common syntax errors in Python and learn to interpret and fix them. Let's start with experimenting with `print` function errors.

# %% [markdown] lang="de"
#
# Im Rahmen dieser Übung werden wir häufige Syntaxfehler in Python untersuchen und lernen, sie zu interpretieren und zu beheben. Fangen wir damit an, Fehler bei der `print`-Funktion zu experimentieren.

# %% [markdown] lang="en"
# **Exercise 1**: In the following cell, intentionally make mistakes with the `print` function calls as described below. Observe and note down the errors you get:
# - Leave out one of the quotation marks in a string.
# - Leave out both quotation marks in a string.
# - Misspell the word `print`.
# - Leave out one of the parentheses, or both.

# %% [markdown] lang="de"
# **Übung 1**: Machen Sie absichtlich Fehler bei den `print`-Funktionsaufrufen in der folgenden Zelle, wie unten beschrieben. Beobachten Sie die Fehlermeldungen, die Sie erhalten:
# - Lassen Sie ein Anführungszeichen in einem String weg.
# - Lassen Sie beide Anführungszeichen in einem String weg.
# - Schreiben Sie das Wort `print` falsch.
# - Lassen Sie eine der Klammern weg oder beide.

# %%
# Try out the intentional mistakes here. For example:
print("Hello, world!
# (You can add more cells as needed to try each mistake)

# %% [markdown] lang="en" tags=["subslide"]
# **Exercise 2**: What happens if you:
# - Use a minus sign to make a negative number?
# - Put a plus sign before a number?
# - Try to use leading zeros in a number, like `09` or `011`?
# - Have two values with no operator between them?
# 
# Experiment in the cells below:

# %% [markdown] lang="de" tags=["subslide"]
# **Übung 2**: Was passiert, wenn Sie:
# - Ein Minuszeichen verwenden, um eine negative Zahl zu erstellen?
# - Ein Pluszeichen vor einer Zahl platzieren?
# - Versuchen, führende Nullen in einer Zahl zu verwenden, wie `09` oder `011`?
# - Zwei Werte ohne Operator dazwischen haben?
#
# Experimentieren Sie in den folgenden Zellen:

# %%
# Experiment with the mentioned scenarios here:

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Using Python as a Calculator

# %% [markdown] lang="de" tags=["subslide"]
## Mini-Workshop: Python als Taschenrechner verwenden

# %% [markdown] lang="en"
# **Exercise 3**: Start the Python interpreter in this Jupyter notebook and use it as a calculator to solve the following problems:
# 1. How many seconds are there in 42 minutes 42 seconds?
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
# 3. If you run a 10-kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

# %% [markdown] lang="de"
# **Übung 3**: Starten Sie den Python-Interpreter in diesem Jupyter-Notebook und verwenden Sie ihn als Taschenrechner, um die folgenden Probleme zu lösen:
# 1. Wie viele Sekunden gibt es in 42 Minuten 42 Sekunden?
# 2. Wie viele Meilen sind in 10 Kilometern? Hinweis: Es gibt 1,61 Kilometer in einer Meile.
# 3. Wenn Sie einen 10-Kilometer-Lauf in 42 Minuten 42 Sekunden absolvieren, was ist Ihr durchschnittliches Tempo (Zeit pro Meile in Minuten und Sekunden)? Was ist Ihre durchschnittliche Geschwindigkeit in Meilen pro Stunde?

# %%
# Answer for 3.1

# %%
# Answer for 3.2

# %%
# Answer for 3.3 (You might need more code cells to neatly organize the calculations)


# %% [markdown] lang="en" tags=["subslide"]
# After you've attempted the exercises, review and discuss the errors and results with peers or mentors. Understanding common errors and learning to calculate and manipulate numbers are foundational skills in programming.# %% [markdown] lang="de" tags=["subslide"]
# Nachdem Sie die Übungen versucht haben, überprüfen und besprechen Sie die Fehler und Ergebnisse mit Kollegen oder Mentoren. Das Verständnis gängiger Fehler und das Erlernen von Berechnungen und Manipulation von Zahlen sind grundlegende Fähigkeiten im Programmieren.

