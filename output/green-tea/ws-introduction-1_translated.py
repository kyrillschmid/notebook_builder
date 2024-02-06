# %% [markdown] lang="en" tags=["slide"]
#
# ## Mini-Workshop: Basics of Programming

# %% [markdown] lang="de" tags=["slide"]
# ## Mini-Workshop: Grundlagen des Programmierens

# %% [markdown] lang="en" tags=["subslide"]
#
# Let's start with understanding what a program is and delve into some core concepts through practice.

# %% [markdown] lang="de" tags=["subslide"]
# Beginnen wir mit dem Verständnis, was ein Programm ist, und tauchen wir durch praktische Übungen in einige Grundkonzepte ein.

# %% [markdown] lang="en" tags=["subslide"]
#
# ### What is a program?

# %% [markdown] lang="de" tags=["subslide"]
# ### Was ist ein Programm?

# %% [markdown] lang="en" tags=["subslide"]
#
# A program is a sequence of instructions that specifies how to perform a computation. This could involve various activities like mathematical operations, data processing, conditional execution, and repetition among others. In this activity, we will get a taste of these concepts.

# %% [markdown] lang="de" tags=["subslide"]
#
# Ein Programm ist eine Abfolge von Anweisungen, die angibt, wie eine Berechnung durchgeführt wird. Dies kann verschiedene Aktivitäten wie mathematische Operationen, Datenverarbeitung, bedingte Ausführung und Wiederholung umfassen. In dieser Aktivität werden wir einen Einblick in diese Konzepte erhalten.

# %% [markdown] lang="en" tags=["subslide"]
# ### Basic Operations
#
# Write a function `perform_operations()` that takes in two numbers and prints their sum, difference, and product.
#


# %% [markdown] lang="de" tags=["subslide"]
# ### Grundlegende Operationen
#
# Schreiben Sie eine Funktion `perform_operations()`, die zwei Zahlen entgegennimmt und ihre Summe, Differenz und Produkt ausgibt.

# %%
def perform_operations(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
    print(f"The difference between {a} and {b} is {a - b}")
    print(f"The product of {a} and {b} is {a * b}")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `perform_operations()` with the numbers 5 and 2.

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie `perform_operations()` mit den Zahlen 5 und 2.

# %%
perform_operations(5, 2)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Conditional Execution
#
# Write a function `compare_numbers(a, b)` that prints which number is larger or if they are equal.


# %% [markdown] lang="de" tags=["subslide"]
# ### Bedingte Ausführung

# Schreiben Sie eine Funktion `vergleiche_zahlen(a, b)`, die ausgibt, welche Zahl größer ist oder ob sie gleich sind.

# %%
def compare_numbers(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are equal")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `compare_numbers(a, b)` with the pairs (3, 5), (10, 7), and (4, 4).

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie `compare_numbers(a, b)` mit den Paaren (3, 5), (10, 7) und (4, 4).

# %%
compare_numbers(3, 5)
compare_numbers(10, 7)
compare_numbers(4, 4)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Repetition
#
# Write a function `print_numbers(n)` that prints all numbers from 1 to `n`.


# %% [markdown] lang="de" tags=["subslide"]
# ### Wiederholung
#
# Schreiben Sie eine Funktion `print_numbers(n)`, die alle Zahlen von 1 bis `n` ausgibt.

# %%
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `print_numbers(n)` with `n` as 5.

# %% [markdown] lang="de" tags=["subslide"]
#
# Testen Sie 'print_numbers(n)' mit 'n' als 5.

# %%
print_numbers(5)
