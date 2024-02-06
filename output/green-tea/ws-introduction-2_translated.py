# %% [markdown] lang="en" tags=["subslide"]
# ## Mini-Workshop: Running Python

# %% [markdown] lang="de" tags=["subslide"]
# ## Mini-Workshop: Python ausführen

# Willkommen zum Mini-Workshop, in dem wir lernen werden, wie man Python-Code ausführt.

# Um Python-Code auszuführen, können Sie eine sogenannte Entwicklungsumgebung verwenden, wie z. B. Jupyter Notebook.

# In Jupyter Notebook können Sie Code in einzelnen Zellen schreiben und ausführen, wodurch es einfach ist, den Code schrittweise zu testen.

# Um eine Zelle auszuführen, können Sie "Shift + Enter" drücken oder auf "Run" in der Symbolleiste klicken.

# Probieren Sie es aus, indem Sie die folgende Code-Zelle ausführen, die "Hallo, Welt!" ausgibt:
print("Hallo, Welt!")

# %% [markdown] lang="en" tags=["slide"]
# Running Python doesn't always require installation and setup on your local machine. For newcomers to the language, starting out directly in the browser can lower the barrier to entry. There are numerous platforms available for this, such as PythonAnywhere, Jupyter Notebooks, Google Colab, etc. These platforms allow you to write and execute Python code in an interactive environment.

# %% [markdown] lang="de" tags=["slide"]
# Das Ausführen von Python erfordert nicht immer Installation und Einrichtung auf Ihrem lokalen Rechner. Für Einsteiger in die Sprache kann der direkte Einstieg im Browser die Einstiegshürde senken. Es gibt zahlreiche Plattformen dafür, wie z.B. PythonAnywhere, Jupyter Notebooks, Google Colab, etc. Diese Plattformen ermöglichen es Ihnen, Python-Code in einer interaktiven Umgebung zu schreiben und auszuführen.

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 1: Basic Python Arithmetic

# %% [markdown] lang="de"  tags=["slide"]
# ### Schritt 1: Grundlegende Python-Arithmetik

# %% [markdown] lang="en"  tags=["slide"]
# Execute the following cell to see Python perform arithmetic operations. This will help us confirm that our environment is up and running.

# %% [markdown] lang="de"  tags=["slide"]
# Führen Sie die folgende Zelle aus, um zu sehen, wie Python arithmetische Operationen durchführt. Dies wird uns bestätigen, dass unsere Umgebung einsatzbereit ist.

# %%
# This is your first Python code cell! Type 1 + 1 and hit 'Run' or 'Shift+Enter' to execute it.
1 + 1
# %% [markdown] lang="en"  tags=["slide"]
# You should see `2` as the output below the cell. This simple confirmation tells us that our Python interpreter is working as expected.
# %% [markdown] lang="de"  tags=["slide"]
# Unterhalb der Zelle sollte die Ausgabe `2` erscheinen. Diese einfache Bestätigung zeigt uns, dass unser Python-Interpreter wie erwartet funktioniert.

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 2: Exploring the Python Version

# %% [markdown] lang="de"  tags=["slide"]
# ### Schritt 2: Erkunden der Python-Version

# %% [markdown] lang="en"  tags=["slide"]
# It is always good to know which version of Python you are working with. Execute the following cell to display your Python version.

# %% [markdown] lang="de"  tags=["slide"]
# Es ist immer gut zu wissen, mit welcher Version von Python Sie arbeiten. Führen Sie die folgende Zelle aus, um Ihre Python-Version anzuzeigen.

# %%
# We can check the version of Python we are using by importing the sys module and printing the version information
import sys

print(sys.version)

# %% [markdown] lang="en"  tags=["slide"]
# Ideally, your version number should start with `3`, indicating that you're running Python 3. Python 2 is outdated and not recommended for new projects.

# %% [markdown] lang="de"  tags=["slide"]
# Idealerweise sollte Ihre Version mit `3` beginnen, was darauf hinweist, dass Sie Python 3 ausführen. Python 2 ist veraltet und für neue Projekte nicht empfohlen.

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 3: Your First Python Function

# %% [markdown] lang="de"  tags=["slide"]
# ### Schritt 3: Ihre erste Python-Funktion

# - Now that you've learned about variables and data types, it's time to dive into writing functions in Python.
# - A function is a block of reusable code that performs a specific task.
# - You can pass data, known as parameters, into a function.
# - A function can return data as a result.
# - In Python, you define a function using the `def` keyword followed by the function name and parentheses ().
# - Let's create a simple function called `greet`, which takes a name as a parameter and returns a greeting message.

# #### Example:

```python
def greet(name):
    return "Hello, " + name + "!"

message = greet("Alice")
print(message)
```

# - In this example, the `greet` function takes a `name` parameter and returns a greeting message using that name.
# - When we call the `greet` function with the argument "Alice", it returns "Hello, Alice!" which is then printed to the console.

# - Now it's your turn to create your own Python function. Try creating a function that takes two numbers as parameters and returns their sum.

# %% [markdown] lang="en"  tags=["slide"]
# Write a function `hello_world()` that prints "Hello, World!" to the screen. Then call that function in another cell to see the output.


# %% [markdown] lang="de"  tags=["slide"]
# Schreibe eine Funktion mit dem Namen `hello_world()`, die "Hallo Welt!" auf dem Bildschirm ausgibt. Rufe dann diese Funktion in einer anderen Zelle auf, um die Ausgabe zu sehen.

# %%
def hello_world():
    print("Hello, World!")


# %%
hello_world()

# %% [markdown] lang="en"  tags=["slide"]
# ### Step 4: Practice Time

# %% [markdown] lang="de"  tags=["slide"]
# ### Schritt 4: Übungszeit

# %% [markdown] lang="en"  tags=["subslide"]
# Now that you have a basic understanding of running Python code, let's practice a bit. Create a function `add(a, b)` that returns the sum of two numbers. Test this function with a few inputs to verify it works as expected.


# %% [markdown] lang="de"  tags=["subslide"]
# Jetzt, da Sie ein grundlegendes Verständnis dafür haben, wie Python-Code ausgeführt wird, wollen wir ein wenig üben. Erstellen Sie eine Funktion `add(a, b)`, die die Summe von zwei Zahlen zurückgibt. Testen Sie diese Funktion mit einigen Eingaben, um sicherzustellen, dass sie wie erwartet funktioniert.

# %%
def add(a, b):
    return a + b


# Example test cases
print(add(2, 3))  # Should print 5
print(add(-1, 1))  # Should print 0
print(add(10, 20))  # Should print 30

# %% [markdown] lang="en"  tags=["slide"]
# Congratulations! You've written your first pieces of Python code and functions in a Jupyter notebook. This interactive environment is very powerful for learning, experimenting, and even for executing complex data analysis projects.
# %% [markdown] lang="de"  tags=["slide"]
# Glückwunsch! Sie haben Ihre ersten Python-Codezeilen und Funktionen in einem Jupyter-Notebook geschrieben. Diese interaktive Umgebung ist sehr leistungsfähig zum Lernen, Experimentieren und sogar zum Ausführen komplexer Datenanalyseprojekte.

