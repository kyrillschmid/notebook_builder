# %% [markdown] lang="en" tags=["slide"]
#
# # Mini-Workshop: Introduction to Programming

# %% [markdown] lang="de" tags=["slide"]
# # Mini-Workshop: Einführung in die Programmierung

# %% [markdown] lang="en"
#
# The goal of this mini-workshop is to introduce you to the idea of thinking like a computer scientist, which involves understanding how to approach problem solving in a systematic and logical manner. We'll start with a basic exercise that gives you a taste of programming and problem-solving.

# %% [markdown] lang="de"
# Das Ziel dieses Mini-Workshops ist es, Sie mit der Idee vertraut zu machen, wie ein Informatiker zu denken, was bedeutet, Problemlösungen systematisch und logisch anzugehen. Wir beginnen mit einer grundlegenden Übung, die Ihnen einen Einblick in das Programmieren und das Problemlösen gibt.

# %% [markdown] lang="en" tags=["slide"]
#
# Write a function `greet(name)` that prints a greeting to the screen. The function should take a string `name` as an argument and print the message `"Hello, {name}! Welcome to the world of Python!"`.


# %% [markdown] lang="de" tags=["slide"]
# Schreibe eine Funktion `greet(name)`, die eine Begrüßung auf dem Bildschirm ausgibt. Die Funktion sollte einen String `name` als Argument entgegennehmen und die Nachricht `"Hallo, {name}! Willkommen in der Welt von Python!"` ausgeben.

# %%
def greet(name):
    print(f"Hello, {name}! Welcome to the world of Python!")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test the function `greet(name)` with your name and observe the output.

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie die Funktion `greet(name)` mit Ihrem Namen und beobachten Sie die Ausgabe.

# %%
greet("Alice")

# %% [markdown] lang="en" tags=["subslide"]
#
# Problem solving involves breaking down a problem into smaller, more manageable parts and then solving each part. Let's practice this by writing a function `is_positive(number)` that:
#
# - Returns `True` if `number` is positive.
# - Otherwise, returns `False`.


# %% [markdown] lang="de" tags=["subslide"]
# ## Problemlösung
# Problemlösung besteht darin, ein Problem in kleinere, überschaubarere Teile zu zerlegen und dann jedes Teilproblem zu lösen. Üben wir das, indem wir eine Funktion `is_positive(number)` schreiben, die folgendes tut:
# 
# - Gibt `True` zurück, wenn `number` positiv ist.
# - Andernfalls gibt sie `False` zurück.

# %%
def is_positive(number):
    return number > 0


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions to test the `is_positive()` function to ensure it returns correct results for -1, 0, and 5.

# %% [markdown] lang="de" tags=["subslide"]
## Schreiben von Aussagen zur Überprüfung der Funktion `is_positive()`, um sicherzustellen, dass sie korrekte Ergebnisse für -1, 0 und 5 zurückgibt.

# %%
assert not is_positive(-1)
assert not is_positive(0)
assert is_positive(5)

# %% [markdown] lang="en" tags=["subslide"]
#
# By writing these small functions and testing them, you are practicing the problem-solving approach of breaking problems down and verifying solutions at each step.
#
# Next, write a function `describe_number(number)` that:
#
# - Prints "`number` is positive." if the number is positive.
# - Prints "`number` is zero." if the number is 0.
# - Prints "`number` is negative." if the number is negative.
#
# Use the `is_positive()` function as part of your solution.


# %% [markdown] lang="de" tags=["subslide"]
#
# Durch das Schreiben dieser kleinen Funktionen und das Testen von ihnen übst du den problemorientierten Ansatz, Probleme zu zerlegen und Lösungen in jedem Schritt zu überprüfen.
#
# Als nächstes schreibe eine Funktion mit dem Namen `describe_number(number)`, die folgendes macht:
#
# - Gibt aus "`number` ist positiv.", wenn die Zahl positiv ist.
# - Gibt aus "`number` ist null.", wenn die Zahl 0 ist.
# - Gibt aus "`number` ist negativ.", wenn die Zahl negativ ist.
#
# Verwende die Funktion `is_positive()` als Teil deiner Lösung.

# %%
def describe_number(number):
    if is_positive(number):
        print(f"{number} is positive.")
    elif number == 0:
        print(f"{number} is zero.")
    else:
        print(f"{number} is negative.")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `describe_number(number)` with the values -5, 0, and 10.

# %% [markdown] lang="de" tags=["subslide"]
#
# Testen Sie `describe_number(number)` mit den Werten -5, 0 und 10.

# %%
describe_number(-5)
describe_number(0)
describe_number(10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Congratulations! You've taken your first steps into the world of programming by learning to think like a computer scientist and practicing problem-solving. Remember, the key is to break down problems into smaller parts, solve each part, and then combine the solutions. Continue practicing these skills, and you'll become more proficient over time.
# %% [markdown] lang="de" tags=["subslide"]
#
# Herzlichen Glückwunsch! Sie haben Ihre ersten Schritte in die Welt der Programmierung gemacht, indem Sie gelernt haben, wie ein Informatiker zu denken und Problemlösung zu üben. Denken Sie daran, das Schlüssel liegt darin, Probleme in kleinere Teile aufzuteilen, jedes Teilproblem zu lösen und dann die Lösungen zu kombinieren. Üben Sie weiterhin diese Fähigkeiten und Sie werden im Laufe der Zeit immer versierter.

