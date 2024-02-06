# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Introduction to Debugging

# %% [markdown] lang="de" tags=["subslide"]
# ## Mini-Workshop: Einführung in die Fehlersuche

# In diesem Mini-Workshop werden wir einige grundlegende Konzepte der Fehlersuche in Python kennenlernen. Das Lösen von Fehlern in Ihrem Code ist ein wichtiger Schritt beim Programmieren.

# Wir werden spezifisch auf die Verwendung von print-Anweisungen, das Lesen von Fehlermeldungen und das Einkreisen von Fehlern in Ihrem Code eingehen. Diese Fähigkeiten werden Ihnen helfen, effizienter zu debuggen und Ihre Programmierfähigkeiten zu verbessern.

# Lassen Sie uns mit dem ersten Abschnitt beginnen und lernen, wie wir print-Anweisungen verwenden können, um den Ablauf Ihres Codes zu verfolgen.

# %% [markdown] lang="en"
#
# Debugging is a crucial skill in programming. It involves identifying and resolving errors or bugs in your code. Let's practice some basic debugging strategies.

# %% [markdown] lang="de"
#
# Debugging ist eine entscheidende Fähigkeit beim Programmieren. Es beinhaltet die Identifizierung und Behebung von Fehlern oder Bugs in Ihrem Code. Lassen Sie uns einige grundlegende Debugging-Strategien üben.

# %% [markdown] lang="en"
# Write a simple function `divide_numbers(numerator, denominator)` that divides two numbers and returns the result. But, make an intentional mistake in the function, for example, use multiplication instead of division.


# %% [markdown] lang="de"
# Schreiben Sie eine einfache Funktion `divide_numbers(Zähler, Nenner)`, die zwei Zahlen dividiert und das Ergebnis zurückgibt. Machen Sie jedoch einen absichtlichen Fehler in der Funktion, verwenden Sie zum Beispiel Multiplikation anstelle von Division.

# %%
def divide_numbers(numerator, denominator):
    # Intentional mistake: using multiplication instead of division
    return numerator * denominator


# %% [markdown] lang="en" tags=["subslide"]
#
# Write a test case that checks whether `divide_numbers()` returns the correct result for a division you know the answer to, e.g., 10 divided by 2. Make an assertion that you know will fail because of the intentional mistake.

# %% [markdown] lang="de" tags=["subslide"]
# Schreiben Sie einen Testfall, der überprüft, ob `divide_numbers()` das richtige Ergebnis für eine Division liefert, für die Sie die Antwort kennen, z.B. 10 geteilt durch 2. Erstellen Sie eine Behauptung, von der Sie wissen, dass sie wegen des beabsichtigten Fehlers fehlschlägt.

# %%
# This assertion should fail because of the mistake in divide_numbers
assert divide_numbers(10, 2) == 5, "The division result should be 5."

# %% [markdown] lang="en" tags=["subslide"]
# Once you've seen the assertion fail, fix the bug in the `divide_numbers` function. Then, run the assertion again to ensure it passes.


# %% [markdown] lang="de" tags=["subslide"]
# Nachdem Sie das Scheitern der Assertion gesehen haben, beheben Sie den Fehler in der Funktion `divide_numbers`. Führen Sie dann die Assertion erneut aus, um sicherzustellen, dass sie erfolgreich ist.

# %%
# Corrected function
def divide_numbers(numerator, denominator):
    # Corrected the mistake to use division
    return numerator / denominator


# This assertion should now pass
assert divide_numbers(10, 2) == 5, "The division result should be 5."

# %% [markdown] lang="en" tags=["subslide"]
# Discuss in the comments below the function `divide_numbers` why it's crucial to understand the error messages produced during debugging and how a systematic approach to debugging can help resolve bugs more efficiently.

# %% [markdown] lang="de" tags=["subslide"]
# Diskutieren Sie in den Kommentaren unten zur Funktion `divide_numbers`, warum es entscheidend ist, die während des Debuggens erzeugten Fehlermeldungen zu verstehen und wie ein systematischer Ansatz zum Debuggen dazu beitragen kann, Fehler effizienter zu beheben.

# %% [markdown] lang="en" tags=["subslide"]
# Debugging Tips:
#
# - Read error messages carefully: They can guide you to the line of code where the problem occurred and sometimes suggest how to fix it.
# - Check your assumptions: Use print statements or a debugger to inspect variables and make sure they hold the values you expect.
# - Take a break: If you're stuck, stepping away for a few minutes can help clear your mind.
# - Ask for help: Discussing the problem with someone else can offer new perspectives and solutions.
# %% [markdown] lang="de" tags=["subslide"]
# Debugging-Tipps:
#
# - Lesen Sie Fehlermeldungen sorgfältig durch: Sie können Sie zur Zeile des Codes führen, in der das Problem aufgetreten ist, und manchmal vorschlagen, wie es zu beheben ist.
# - Überprüfen Sie Ihre Annahmen: Verwenden Sie print-Anweisungen oder einen Debugger, um Variablen zu inspizieren und sicherzustellen, dass sie die erwarteten Werte enthalten.
# - Machen Sie eine Pause: Wenn Sie feststecken, kann es helfen, sich für ein paar Minuten zurückzuziehen und den Kopf frei zu bekommen.
# - Holen Sie sich Hilfe: Das Diskutieren des Problems mit jemand anderem kann neue Perspektiven und Lösungen bieten.

