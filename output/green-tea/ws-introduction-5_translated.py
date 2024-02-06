# %% [markdown]
# # Mini-Workshop: Values and Types

# %% [markdown] lang="en" tags=["subslide"]
# In this workshop, we will explore Python values and their types, which are the fundamental components to understand before diving deep into Python programming.

# %% [markdown] lang="de" tags=["subslide"]
# In diesem Workshop werden wir Python-Werte und ihre Typen erkunden, die die grundlegenden Komponenten darstellen, die man verstehen sollte, bevor man tief in die Python-Programmierung einsteigt.

# %% [markdown] lang="en"
# ## Understanding Values and Types

# %% [markdown] lang="de"
# ## Verständnis von Werten und Typen

# %% [markdown] lang="en"
# A *value* is one of the basic things a program works with, like a letter or a number. Some values we have seen so far are 2, 42.0, and 'Hello, World!'. Values belong to different *types*: 2 is an *integer*, 42.0 is a *floating-point number*, and 'Hello, World!' is a *string*.

# %% [markdown] lang="de"
# Ein *Wert* ist eines der grundlegenden Dinge, mit denen ein Programm arbeitet, wie ein Buchstabe oder eine Zahl. Einige Werte, die wir bisher gesehen haben, sind 2, 42.0 und 'Hallo, Welt!'. Werte gehören verschiedenen *Typen* an: 2 ist eine *Ganzzahl*, 42.0 ist eine *Gleitkommazahl* und 'Hallo, Welt!' ist ein *String*.

# %% [markdown] lang="en"
# Use Python's `type()` function to find out the type of a value. Try to predict what the type will be before you run each of the following lines:

# Here are some values
values = [2, 42.0, "Hello, World!", "2", "42.0", 1, 000, 000]

# %% [markdown] lang="de"
# Verwenden Sie die Funktion `type()` von Python, um den Typ eines Werts herauszufinden. Versuchen Sie vorherzusagen, welcher Typ es sein wird, bevor Sie jede der folgenden Zeilen ausführen:

# Hier sind einige Werte
values = [2, 42.0, "Hallo, Welt!", "2", "42.0", 1, 000, 000]

# %% [markdown] lang="en"
# Loop through the values and print their types:
# %% [markdown] lang="de"
# Loop durch die Werte und gib ihre Typen aus:

# %%
for value in values:
    print(f"The type of {value} is {type(value)}")

# %% [markdown] lang="en"
# ## Exercise: Predict the Type

# %% [markdown] lang="de"
# ## Übung: Typ vorhersagen

# Betrachten Sie die folgenden Ausdrücke und versuchen Sie, den Typ des Ergebnisses vorherzusagen (z. B. int, float, str) bevor Sie den Code ausführen:

# 1. 15 / 4
# 2. 15 // 4
# 3. 15 % 4
# 4. 2 ** 3
# 5. "Hello" + "World"
# 6. "Hello" * 3

# Schreiben Sie Ihre Vorhersagen auf, bevor Sie den Code in einer Python-Zelle ausführen.

# %% [markdown] lang="en"
# Can you predict the type of the following values? Use the code cell below to check your predictions:
#
# 1. '2'
# 2. '42.0'
# 3. 1,000,000
#
# Note: Write your prediction before running the code.

# Write your code here to check the type of each value above
print(type("2"))
print(type("42.0"))
print(type(1, 000, 000))

# %% [markdown] lang="de"
# Können Sie den Typ der folgenden Werte vorhersagen? Verwenden Sie die Code-Zelle unten, um Ihre Vorhersagen zu überprüfen:

# 1. '2'
# 2. '42.0'
# 3. 1,000,000

# Hinweis: Schreiben Sie Ihre Vorhersage, bevor Sie den Code ausführen.

# Schreiben Sie hier Ihren Code, um den Typ jedes oben genannten Werts zu überprüfen
print(type("2"))
print(type("42.0"))
print(type(1,000,000))

# %% [markdown] lang="en"
# Were your predictions correct? Discuss any surprises or unclear results.

# %% [markdown] lang="de"
# Waren deine Vorhersagen korrekt? Diskutiere eventuelle Überraschungen oder unklare Ergebnisse.

# %% [markdown] lang="en"
# ## Understanding Comma-separated Values

# %% [markdown] lang="de"
# ## Verständnis von durch Kommas getrennten Werten

# %% [markdown] lang="en"
# When you type a large integer, you might be tempted to use commas between groups of three digits, as in `1,000,000`. This is not a legal integer in Python, as you've seen. Discuss what you observed when you checked the type of `1,000,000`.

# %% [markdown] lang="de"
# Wenn Sie eine große Ganzzahl eingeben, könnten Sie versucht sein, Kommas zwischen Gruppen von drei Ziffern zu verwenden, wie zum Beispiel `1,000,000`. Dies ist jedoch keine gültige Ganzzahl in Python, wie Sie bereits festgestellt haben. Diskutieren Sie, was passiert, wenn Sie den Typ von `1,000,000` überprüfen.

# %% [markdown] lang="en"
# As an additional task, try printing the type and value of `1,000,000` without using the `print()` function in a loop or a specific function call. What does Python interpret this as?

# %% [markdown] lang="de"
# Als zusätzliche Aufgabe versuchen Sie, den Typ und Wert von `1,000,000` ohne Verwendung der `print()`-Funktion in einer Schleife oder einem spezifischen Funktionsaufruf auszugeben. Wie interpretiert Python dies?

# %% [markdown] lang="en"
# ## Conclusion

# %% [markdown] lang="de"
# ## Fazit

# %% [markdown] lang="en"
# In this workshop, you have learned about basic types in Python, such as integers, floating-point numbers, and strings. You have also seen how the `type()` function can be used to discover the type of a given value.
#
# Understanding the types of values is crucial in programming because it affects how the values can be manipulated and used in expressions. Keep experimenting with different values to get comfortable with their types.
# %% [markdown] lang="de"
# In diesem Workshop haben Sie die grundlegenden Datentypen in Python kennengelernt, wie Ganzzahlen, Gleitkommazahlen und Zeichenketten. Sie haben auch gesehen, wie die `type()` Funktion verwendet werden kann, um den Typ eines gegebenen Werts zu entdecken.

# Das Verständnis der Werttypen ist entscheidend in der Programmierung, da es beeinflusst, wie die Werte manipuliert und in Ausdrücken verwendet werden können. Experimentieren Sie weiterhin mit verschiedenen Werten, um sich mit ihren Typen vertraut zu machen.

