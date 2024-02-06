# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Introduction to Python

# %% [markdown] lang="de" tags=["subslide"]
# ## Mini-Workshop: Einführung in Python

# %% [markdown] lang="en"
#
# In this workshop, we'll be exploring the basics of Python. We'll start with understanding what variables are and how we can use them. Let's dive in!

# %% [markdown] lang="de"
#
# In diesem Workshop werden wir die Grundlagen von Python erkunden. Wir beginnen damit zu verstehen, was Variablen sind und wie wir sie verwenden können. Legen wir los!

# %% [markdown] lang="en"
# ### What is a Variable?
# In programming, a variable is used to store information that can be referenced and manipulated in a program. It acts as a container for data.

# %% [markdown] lang="de"
# ### Was ist eine Variable?
# In der Programmierung wird eine Variable verwendet, um Informationen zu speichern, auf die in einem Programm Bezug genommen und die darin manipuliert werden können. Sie fungiert als Behälter für Daten.

# %% [markdown] lang="en"
# **Task:** Create a variable named `greeting` that holds the string "Hello, Python!" and print its value.

# %% [markdown] lang="de"
# **Aufgabe**: Erstellen Sie eine Variable mit dem Namen `greeting`, die den String "Hallo, Python!" enthält, und geben Sie dessen Wert aus.

# %%
# Solution:
greeting = "Hello, Python!"
print(greeting)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Basic Data Types
# Let's explore some of the basic types in Python by creating variables of different types and checking their types using the `type()` function.

# %% [markdown] lang="de" tags=["subslide"]
#
# ### Grundlegende Datentypen
# Lassen Sie uns einige der grundlegenden Typen in Python erkunden, indem wir Variablen unterschiedlicher Typen erstellen und ihre Typen mithilfe der `type()`-Funktion überprüfen.

# %% [markdown] lang="en"
# **Task:** Create variables to store your age (an integer), your height in meters (a floating-point number), and your first name (a string). Print the type of each variable.

# %% [markdown] lang="de"
# **Aufgabe:** Erstellen Sie Variablen, um Ihr Alter (eine Ganzzahl), Ihre Größe in Metern (eine Gleitkommazahl) und Ihren Vornamen (eine Zeichenkette) zu speichern. Geben Sie den Typ jeder Variablen aus.

# %%
# Solution:
age = 25  # Replace 25 with your age
height = 1.75  # Replace 1.75 with your height in meters
first_name = "John"  # Replace "John" with your first name

print(type(age))
print(type(height))
print(type(first_name))

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Operators and Expressions
# In Python, operators allow you to perform computations on values. Let's try some of the basic arithmetic operators.

# %% [markdown] lang="de" tags=["subslide"]
#
# ### Operatoren und Ausdrücke
# In Python ermöglichen Operatoren, Berechnungen an Werten durchzuführen. Lassen Sie uns einige der grundlegenden arithmetischen Operatoren ausprobieren.

# %% [markdown] lang="en"
# **Task:** Calculate the sum of 15 and 23. Then, calculate the product of 15 and 23. Print both results.

# %% [markdown] lang="de"
# **Aufgabe:** Berechnen Sie die Summe von 15 und 23. Berechnen Sie dann das Produkt von 15 und 23. Geben Sie beide Ergebnisse aus.

# %%
# Solution:
sum_result = 15 + 23
product_result = 15 * 23

print("Sum:", sum_result)
print("Product:", product_result)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Strings and Concatenation
# String concatenation means adding strings together. Use the `+` operator to concatenate strings.

# %% [markdown] lang="de" tags=["subslide"]

# ### Zeichenketten und Verkettung
# Zeichenkettenverkettung bedeutet das Hinzufügen von Zeichenketten. Verwenden Sie den `+` Operator, um Zeichenketten zu verkettet.

# %% [markdown] lang="en"
# **Task:** Concatenate your `first_name` variable with a string that says " is learning Python." and print the result.

# %% [markdown] lang="de"
# **Aufgabe:** Verketten Sie Ihre Variable `first_name` mit einem String, der besagt "lernt Python." und geben Sie das Ergebnis aus.

# %%
# Solution:
message = first_name + " is learning Python."
print(message)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Debugging Exercise
# Often, you might encounter errors in your code. Let's purposely create an error and practice debugging.

# %% [markdown] lang="de" tags=["subslide"]
# ### Übung zur Fehlersuche
# Oft treten Fehler in Ihrem Code auf. Lassen Sie uns absichtlich einen Fehler erstellen und das Debuggen üben.

# %% [markdown] lang="en"
# **Task:** Fix the syntax error in the code below and execute it to print "Debugging in Python."

# %% [markdown] lang="de"
# **Aufgabe:** Beheben Sie den Syntaxfehler im folgenden Code und führen Sie ihn aus, um "Debugging in Python" auszudrucken.

print("Debugging in Python")

# %%
# Intentional error for debugging exercise
# print "Debugging in Python"

# Solution:
print("Debugging in Python")
