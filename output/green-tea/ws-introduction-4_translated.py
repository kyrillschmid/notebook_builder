# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Intro to Arithmetic Operators

# %% [markdown] lang="de" tags=["subslide"]

# ## Mini-Workshop: Einführung in arithmetische Operatoren

# - Arithmetic operators are used to perform mathematical operations in Python.
# - The basic arithmetic operators in Python are:
     - Addition: +
     - Subtraction: -
     - Multiplication: *
     - Division: /
     - Modulo: %
     - Exponentiation: **
     
### Addition
```python
a = 5
b = 3
result = a + b
print(result)  # Output: 8
```

### Subtraction
```python
a = 5
b = 3
result = a - b
print(result)  # Output: 2
```

### Multiplication
```python
a = 5
b = 3
result = a * b
print(result)  # Output: 15
```

### Division
```python
a = 6
b = 2
result = a / b
print(result)  # Output: 3.0
```

### Modulo
```python
a = 7
b = 4
result = a % b
print(result)  # Output: 3
```

### Exponentiation
```python
a = 2
b = 3
result = a ** b
print(result)  # Output: 8
```

# %% [markdown] lang="en" tags=["subslide"]
#
# Python provides various arithmetic operators such as `+`, `-`, `*`, `/`, and `**`. Let's use these operators to perform some basic arithmetic operations.

# %% [markdown] lang="de" tags=["subslide"]
# Python bietet verschiedene arithmetische Operatoren wie `+`, `-`, `*`, `/` und `**`. Lassen Sie uns diese Operatoren verwenden, um einige grundlegende arithmetische Operationen durchzuführen.

# %% [markdown] lang="en"
# Write a function `perform_operations(a, b)` that takes two numbers `a` and `b` as arguments and returns a tuple. The tuple should contain the result of: addition (`a + b`), subtraction (`a - b`), multiplication (`a * b`), division (`a / b`), and exponentiation (`a ** b`).


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion 'perform_operations(a, b)', die zwei Zahlen 'a' und 'b' als Argumente erhält und ein Tupel zurückgibt. Das Tupel sollte das Ergebnis der Addition ('a + b'), Subtraktion ('a - b'), Multiplikation ('a * b'), Division ('a / b') und Potenzierung ('a ** b') enthalten.

# %%
def perform_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    exponentiation = a**b
    return addition, subtraction, multiplication, division, exponentiation


# %% [markdown] lang="en" tags=["subslide"]
#
# Assert that `perform_operations(6, 2)` returns the correct results for the operations: addition => 8, subtraction => 4, multiplication => 12, division => 3.0, and exponentiation => 36.

# %% [markdown] lang="de" tags=["subslide"]
#
# Stellen Sie sicher, dass `perform_operations(6, 2)` die korrekten Ergebnisse für die Operationen zurückgibt: Addition => 8, Subtraktion => 4, Multiplikation => 12, Division => 3.0 und Potenzierung => 36.

# %%
assert perform_operations(6, 2) == (8, 4, 12, 3.0, 36)

# %% [markdown] lang="en" tags=["subslide"]
# Write a function `print_operations(a, b)` that
#
# - takes two numbers `a` and `b`,
# - performs the same arithmetic operations as `perform_operations`, and
# - prints the results in a user-friendly way.
#
# Ensure you clearly label each operation in the output.


# %% [markdown] lang="de" tags=["subslide"]
# Schreiben Sie eine Funktion `print_operations(a, b)`, die
#
# - zwei Zahlen `a` und `b` annimmt,
# - die gleichen arithmetischen Operationen wie `perform_operations` durchführt und
# - die Ergebnisse benutzerfreundlich ausgibt.
#
# Stellen Sie sicher, dass jede Operation im Output klar gekennzeichnet ist.

# %%
def print_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    exponentiation = a**b
    print(f"Addition: {a} + {b} = {addition}")
    print(f"Subtraction: {a} - {b} = {subtraction}")
    print(f"Multiplication: {a} * {b} = {multiplication}")
    print(f"Division: {a} / {b} = {division}")
    print(f"Exponentiation: {a} ** {b} = {exponentiation}")


# %% [markdown] lang="en" tags=["subslide"]
# Test the `print_operations(a, b)` function with the values 6 and 2.

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie die `print_operations(a, b)` Funktion mit den Werten 6 und 2.

# %%
print_operations(6, 2)
