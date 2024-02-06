# j2 from 'macros.j2' import header
# {{ header("What is a program?", "What is a program?") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Chapter 1: The Way of The Program
# - The goal of this chapter is to encourage you to think like a computer scientist
# - Computer scientists blend the best aspects of mathematics, engineering, and natural science
#   - They use formal languages to denote ideas similar to mathematicians,
#   - They assemble components into systems and considering tradeoffs like engineers,
#   - They observe and analyse the behavior of complex systems like scientists,

# %% [markdown] lang="de" tags=["slide"]
# ## Kapitel 1: Der Weg des Programms
# - Das Ziel dieses Kapitels ist es, Sie dazu zu ermutigen, wie ein Informatiker zu denken.
# - Informatiker vereinen die besten Aspekte der Mathematik, Ingenieurwissenschaften und Naturwissenschaften.
#   - Sie verwenden formale Sprachen, um Ideen ähnlich wie Mathematiker darzustellen,
#   - Sie setzen Komponenten zu Systemen zusammen und berücksichtigen dabei Kompromisse wie Ingenieure,
#   - Sie beobachten und analysieren das Verhalten komplexer Systeme wie Wissenschaftler.

# %% [markdown] lang="en" tags=["slide"]
# ## Problem-Solving Skills in Programming
# - The primary skill for a computer scientist is problem solving
# - Problem solving involves the ability to formulate problems, think creatively about solutions, and express them clearly and accurately
# - Learning to program is an excellent opportunity to practice problem-solving skills

# %% [markdown] lang="de" tags=["slide"]
## Problemlösungsfähigkeiten in der Programmierung
- Die wichtigste Fähigkeit für einen Informatiker ist das Problemlösen.
- Problemlösung beinhaltet die Fähigkeit, Probleme zu formulieren, kreativ über Lösungen nachzudenken und sie klar und präzise auszudrücken.
- Das Erlernen des Programmierens ist eine ausgezeichnete Gelegenheit, um Problemlösungsfähigkeiten zu trainieren.

# %% [markdown] lang="en" tags=["slide"]
# ## The Objective of Programming
# - On one level, the objective is to learn to program, a practical skill in itself
# - On another level, programming will be used as a tool to achieve another goal, which will be made clear as we proceed

# %% [markdown] lang="de" tags=["slide"]
# ## Das Ziel des Programmierens
# - Auf einer Ebene besteht das Ziel darin, das Programmieren als praktische Fähigkeit zu erlernen.
# - Auf einer anderen Ebene wird Programmierung als Werkzeug verwendet, um ein anderes Ziel zu erreichen, das im weiteren Verlauf klar wird.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.1 What is a program?
# - A program is a sequence of instructions for computing.
# - Computations can be mathematical (like solving systems of equations) or symbolic (such as text searching).
# - Whether graphical processing or video playing, it all boils down into basic instructions which are common across languages.

# %% [markdown] lang="de" tags=["slide"]
# ## 1.1 Was ist ein Programm?
# - Ein Programm ist eine Abfolge von Anweisungen zur Datenverarbeitung.
# - Berechnungen können mathematisch sein (wie das Lösen von Gleichungssystemen) oder symbolisch (wie die Textsuche).
# - Ob grafische Verarbeitung oder Videowiedergabe, letztendlich basiert alles auf grundlegenden Anweisungen, die sprachübergreifend gleich sind.

# %% [markdown] lang="en" tags=["slide"]
# ## Basic Instructions in Programming
# - **Input**: Obtaining data from various sources.
# - **Output**: Displaying results or saving to different destinations.
# - **Math**: Executing basic arithmetic calculations.

# %% [markdown] lang="de" tags=["slide"]
# ## Grundlegende Anweisungen in der Programmierung
# - **Eingabe**: Daten aus verschiedenen Quellen abrufen.
# - **Ausgabe**: Ergebnisse anzeigen oder an verschiedenen Zielen speichern.
# - **Mathematik**: Ausführen grundlegender arithmetischer Berechnungen.

# %% [markdown] lang="en" tags=["slide"]
# ## Basic Instructions in Programming (Continuation)
# - **Conditional Execution**: Checking conditions and executing appropriate code.
# - **Repetition**: Performing actions multiple times, often with slight modifications.
# - Every complex program is made up of these fundamental instructions.

# %% [markdown] lang="de" tags=["slide"]
## Grundlegende Anweisungen in der Programmierung (Fortsetzung)
- **Bedingte Ausführung**: Überprüfen von Bedingungen und Ausführen entsprechenden Codes.
- **Wiederholung**: Mehrfaches Ausführen von Aktionen, oft mit leichten Modifikationen.
- Jedes komplexe Programm setzt sich aus diesen grundlegenden Anweisungen zusammen.

# %% [markdown] lang="en" tags=["slide"]
# ## Programming as a Process
# - Programming can be considered as a process of breaking down complex tasks into smaller subtasks.
# - Subtasks are further simplified until they can be performed using the basic instructions.

# %% [markdown] lang="de" tags=["slide"]
# ## Programmieren als Prozess
# - Programmieren kann als ein Prozess betrachtet werden, bei dem komplexe Aufgaben in kleinere Teilaufgaben aufgeteilt werden.
# - Diese Teilaufgaben werden weiter vereinfacht, bis sie mit den grundlegenden Anweisungen ausgeführt werden können.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.2 Running Python
# - Running Python can be a challenge for beginners who might have to install Python and related software
# - To avoid the simultaneous stress of learning system administration and programming Python can be run in a browser
# - There are several webpages where Python can be run, one of them is PythonAnywhere
# - For beginners, Python 3 is recommended as it is similar to Python 2 but has few differences

# %% [markdown] lang="de" tags=["slide"]
# ## 1.2 Python ausführen
# - Das Ausführen von Python kann für Anfänger eine Herausforderung darstellen, da sie Python und verwandte Software installieren müssen.
# - Um den gleichzeitigen Stress des Erlernens der Systemadministration und des Programmierens zu vermeiden, kann Python im Browser ausgeführt werden.
# - Es gibt mehrere Webseiten, auf denen Python ausgeführt werden kann, eine davon ist PythonAnywhere.
# - Für Anfänger wird Python 3 empfohlen, da es ähnlich wie Python 2 ist, aber einige Unterschiede aufweist.

# %% [markdown] lang="en" tags=["slide"]
# - Python interpreter is a program that reads and executes Python code.
# - Your environment determines how you start the interpreter, possibly by clicking an icon or typing `python` on a command line.
# - The interpreter gives out information about itself and its running environment when it starts

# %% [markdown] lang="de" tags=["slide"]
# - Der Python-Interpreter ist ein Programm, das Python-Code liest und ausführt.
# - Ihre Umgebung bestimmt, wie Sie den Interpreter starten, möglicherweise durch Klicken auf ein Symbol oder durch Eingabe von `python` in einer Befehlszeile.
# - Der Interpreter gibt Informationen über sich selbst und seine laufende Umgebung aus, wenn er gestartet wird.

# %%
print("Python 3.4.0 (default, Jun 19 2015, 14:20:21) [GCC 4.8.2] on linux")
print('Type "help", "copyright", "credits" or "license" for more information.')
print(">>>")

# %% [markdown] lang="en" tags=["slide"]
# - The displayed information would differ depending on your operating system, you need to check that the version number starts with a 3.
# - An indicated version number starting with 2 would mean you are running Python 2
# - The last line displayed is a prompt for you to enter code

# %% [markdown] lang="de" tags=["slide"]
# - Die angezeigten Informationen würden je nach Betriebssystem variieren, Sie müssen überprüfen, ob die Versionsnummer mit einer 3 beginnt.
# - Eine angegebene Versionsnummer, die mit 2 beginnt, würde bedeuten, dass Sie Python 2 ausführen.
# - Die letzte angezeigte Zeile ist eine Aufforderung, Code einzugeben.

# %%
print(">>> 1 + 1")
print(2)

# %% [markdown] lang="en" tags=["slide"]
# - If you type a line of code and hit Enter, the interpreter displays the result
# - Once you are comfortable starting the Python interpreter and running code, you are ready to get started
# - Henceforth, the assumption is that you know how to start the Python interpreter and run code.

# %% [markdown] lang="de" tags=["slide"]
# - Wenn Sie eine Zeile Code eingeben und Enter drücken, zeigt der Interpreter das Ergebnis an.
# - Sobald Sie sich wohl dabei fühlen, den Python-Interpreter zu starten und Code auszuführen, können Sie beginnen.
# - Daher wird im Folgenden davon ausgegangen, dass Sie wissen, wie man den Python-Interpreter startet und Code ausführt.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.3 The First Program
# - The first program typically written in any new language is "Hello, World!".
# - This program simply displays the words "Hello, World!".
# - In Python, the "Hello, World!" program utilizes the `print` function to display result on the screen.
# - A `print` statement does not actually print anything on paper.

# %% [markdown] lang="de" tags=["slide"]
# ## 1.3 Das erste Programm
# - Das erste Programm, das in einer neuen Sprache geschrieben wird, ist in der Regel "Hallo Welt!".
# - Dieses Programm zeigt einfach die Worte "Hallo Welt!" an.
# - In Python verwendet das "Hallo Welt!"-Programm die `print` Funktion, um das Ergebnis auf dem Bildschirm anzuzeigen.
# - Eine `print` Anweisung druckt tatsächlich nichts auf Papier aus.

# %%
print("Hello, World!")

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Python Syntax
# - Quotation marks in a `print` statement define the starting and ending of the text to be displayed.
# - These quotation marks do not appear in the output.
# - Parentheses indicate that `print` is a function.
# - Further details on functions will be covered in Chapter 3.

# %% [markdown] lang="de" tags=["slide"]
# ## Verständnis der Python-Syntax
# - Anführungszeichen in einer `print`-Anweisung definieren den Beginn und das Ende des anzuzeigenden Textes.
# - Diese Anführungszeichen erscheinen nicht in der Ausgabe.
# - Klammern zeigen an, dass `print` eine Funktion ist.
# - Weitere Details zu Funktionen werden im Kapitel 3 behandelt.

# %% [markdown] lang="en" tags=["slide"]
# ## Differences in Python Version
# - In Python 2, the `print` statement is not a function and thus, does not use parentheses.
# - Agreater clarity on this distinction between Python 2 and Python 3 will be provided in subsequent sessions.

# %% [markdown] lang="de" tags=["slide"]
# ## Unterschiede in den Python-Versionen
# - In Python 2 ist die `print`-Anweisung kein Funktion und wird daher ohne Klammern verwendet.
# - Eine genauere Erläuterung dieser Unterscheidung zwischen Python 2 und Python 3 wird in den folgenden Sitzungen gegeben.

# %%
# Example of print statement in Python 2
# print 'Hello, World!'
# %% [markdown] lang="en" tags=["slide"]
# ## 1.4 Arithmetic operators
# - Python provides special symbols known as arithmetic operators for mathematical computations.
# - These operators include + (addition), - (subtraction), * (multiplication), and / (division).
# - There's also the ** operator, used for exponentiation, which means raising a number to a power.
# - A notable operator in other languages, ^, is a bitwise operator called XOR in Python, not used for exponentiation as one might expect.

# %% [markdown] lang="de" tags=["slide"]
# ## 1.4 Rechenoperatoren
# - Python bietet spezielle Symbole namens Rechenoperatoren für mathematische Berechnungen.
# - Diese Operatoren umfassen + (Addition), - (Subtraktion), * (Multiplikation) und / (Division).
# - Es gibt auch den ** Operator, der für die Potenzierung verwendet wird, was bedeutet, eine Zahl potenzieren.
# - Ein bemerkenswerter Operator in anderen Sprachen, ^, ist ein bitweiser Operator namens XOR in Python, nicht für Potenzierung wie man es erwarten könnte.

# %%
# Arithmetic operations examples
print(40 + 2)  # Addition
print(43 - 1)  # Subtraction
print(6 * 7)  # Multiplication

# %% [markdown] lang="en" tags=["slide"]
# - The operator / performs division.
#   - The division result may be a float even if the mathematical result is a whole number.
#   - This characteristic will be explained later.
# - The operator ** performs exponentiation (raising a number to a power).
# - In other languages, the operator ^ is used for exponentiation, but in Python it's used as a bitwise operator called XOR.

# %% [markdown] lang="de" tags=["slide"]
# - Der Operator / führt eine Division durch.
#   - Das Divisionsergebnis kann eine Gleitkommazahl sein, auch wenn das mathematische Ergebnis eine ganze Zahl ist.
#   - Diese Eigenschaft wird später erklärt.
# - Der Operator ** führt eine Potenzierung (das Erheben einer Zahl zur Potenz) durch.
# - In anderen Sprachen wird der Operator ^ für die Potenzierung verwendet, aber in Python wird er als ein bitweiser Operator namens XOR verwendet.

# %%
# More arithmetic operations examples
print(84 / 2)  # Division
print(6**2 + 6)  # Exponentiation

# %% [markdown] lang="en" tags=["slide"]
# - The operator ^ in Python is a bitwise operator called XOR, which may offer unexpected results if used for exponentiation.
# - Note: Bitwise operators are not covered in this notebook, but you can learn more about them from Python's official documentation or other online resources.

# %% [markdown] lang="de" tags=["slide"]
# - Der Operator ^ in Python ist ein bitweiser Operator namens XOR, der unerwartete Ergebnisse liefern kann, wenn er zur Potenzierung verwendet wird.
# - Hinweis: Bitweise Operatoren werden in diesem Notebook nicht behandelt, aber Sie können mehr über sie in der offiziellen Dokumentation von Python oder anderen Online-Ressourcen erfahren.

# %%
# Example of XOR operation
print(6 ^ 2)  # XOR operation (not exponentiation)
# %% [markdown] lang="en" tags=["slide"]
# ## 1.5 Values and types
# - A program manipulates basic items like letters and numbers, known as 'values'
# - Each value belongs to a type such as integer (`int`), floating-point number (`float`), or string (`str`)
# - The Python interpreter can reveal the type of a value using the `type()` function
# - The term 'class' in the results refers to a category of values
# - Each value type falls into a distinct class

# %% [markdown] lang="de" tags=["slide"]
# ## 1.5 Werte und Typen
# - Ein Programm manipuliert grundlegende Elemente wie Buchstaben und Zahlen, die als 'Werte' bezeichnet werden
# - Jeder Wert gehört zu einem Typ wie Ganzzahl ('int'), Gleitkommazahl ('float') oder Zeichenkette ('str')
# - Der Python-Interpreter kann den Typ eines Werts mithilfe der Funktion `type()` anzeigen
# - Der Begriff 'Klasse' im Ergebnis bezieht sich auf eine Kategorie von Werten
# - Jeder Werttyp gehört zu einer eigenen Klasse

# %%
# Displaying the type of different value
print(type(2))
print(type(42.0))
print(type("Hello, World!"))

# %% [markdown] lang="en" tags=["slide"]
# - Values like '2' and '42.0' might look like numbers but they are strings as they are enclosed in quotation marks
# - Python interprets numbers with commas (e.g., 1,000,000) as a comma-separated sequence of integers, not as a single integer

# %% [markdown] lang="de" tags=["slide"]
# - Werte wie '2' und '42.0' mögen wie Zahlen aussehen, sind jedoch Zeichenketten, da sie in Anführungszeichen eingeschlossen sind.
# - Python interpretiert Zahlen mit Kommas (z. B. 1.000.000) als durch Kommas getrennte Sequenz von Ganzzahlen, nicht als einzelne Ganzzahl.

# %%
# Checking the types of numeric values represented as strings
print(type("2"))
print(type("42.0"))

# %%
# Python treating comma-separated numbers as separate integers
print(1, 000, 000)
# %% [markdown] lang="en" tags=["slide"]
# ## 1.6 Formal and Natural languages
# - Natural languages are the languages people speak, such as English, Spanish, and French, they evolved naturally not designed by people.
# - Formal languages are designed by people for specific applications like mathematics, chemistry and programming languages which have strict syntax rules.

# %% [markdown] lang="de" tags=["slide"]
# ## 1.6 Formale und natürliche Sprachen
# - Natürliche Sprachen sind die Sprachen, die Menschen sprechen, wie Englisch, Spanisch und Französisch. Sie haben sich natürlich entwickelt und wurden nicht von Menschen entworfen.
# - Formale Sprachen werden von Menschen für spezifische Anwendungen entworfen, wie Mathematik, Chemie und Programmiersprachen, die strenge Syntaxregeln haben.

# %% [markdown] lang="en" tags=["slide"]
# ## Syntax in languages
# - Syntax rules govern the structure of statements, for instance, '3 + 3 = 6' is syntactically correct while '3 + = 3 $ 6' is not in mathematics.
# - Syntax rules come in two flavors: tokens and structure.
#   - Tokens are the basic elements of a language, such as words, numbers, and chemical elements.
#   - The second type of syntax rule pertains to the way tokens are combined.

# %% [markdown] lang="de" tags=["slide"]
# ## Syntax in Sprachen
# - Syntaxregeln regeln die Struktur von Anweisungen, zum Beispiel ist '3 + 3 = 6' in der Mathematik syntaktisch korrekt, während '3 + = 3 $ 6' es nicht ist.
# - Syntaxregeln kommen in zwei Varianten vor: Token und Struktur.
#   - Tokens sind die grundlegenden Elemente einer Sprache, wie Wörter, Zahlen und chemische Elemente.
#   - Der zweite Typ von Syntaxregel bezieht sich darauf, wie Tokens kombiniert werden.

# %% [markdown] lang="en" tags=["slide"]
# ## Parsing and Main Features of Languages
# - The process of figuring out the structure of a sentence in a language is called parsing.
# - Formal and natural languages share certain features such as tokens, structure, and syntax.
# - There are key differences between these languages in terms of ambiguity, redundancy, and literalness.

# %% [markdown] lang="de" tags=["slide"]
# ## Parsing und Hauptmerkmale von Sprachen
# - Der Prozess, die Struktur eines Satzes in einer Sprache zu ermitteln, wird als Parsing bezeichnet.
# - Formale und natürliche Sprachen teilen bestimmte Merkmale wie Tokens, Struktur und Syntax.
# - Es gibt wesentliche Unterschiede zwischen diesen Sprachen in Bezug auf Ambiguität, Redundanz und Wörtlichkeit.

# %% [markdown] lang="en" tags=["slide"]
# ## Contrast between Natural and Formal Languages
# - Natural languages, due to inherent ambiguity, employ lots of redundancy and often verbose while formal languages are less redundant and more concise.
# - Natural languages are full of idiom and metaphor and may not mean exactly what they say while formal languages mean exactly what they say.

# %% [markdown] lang="de" tags=["slide"]
# ## Unterschied zwischen natürlichen und formalen Sprachen
# - Natürliche Sprachen verwenden aufgrund ihrer inhärenten Mehrdeutigkeit viele Redundanzen und sind oft ausführlich, während formale Sprachen weniger redundant und prägnanter sind.
# - Natürliche Sprachen sind voll von Redewendungen und Metaphern und bedeuten möglicherweise nicht genau das, was sie sagen, während formale Sprachen genau das bedeuten, was sie sagen.

# %% [markdown] lang="en" tags=["slide"]
# ## Importance of Understanding Formal Languages
# - As we all grow up speaking natural languages, it might require some adjustment to understand and use formal languages.
# - The understanding of a computer program, a form of formal language, is unambiguous and literal and is fully obtained from analysis of the tokens and structure.
# - Reading formal languages involves careful parsing and attention to detail in punctuation and spelling as unlike in natural languages, a small mistake can cause significant errors.

# %% [markdown] lang="de" tags=["slide"]
# ## Bedeutung des Verständnisses formaler Sprachen
# - Da wir alle mit natürlichen Sprachen aufwachsen, kann es einige Anpassungen erfordern, formale Sprachen zu verstehen und zu verwenden.
# - Das Verständnis eines Computerprogramms, einer Form formaler Sprache, ist eindeutig und wörtlich und wird vollständig aus der Analyse der Tokens und der Struktur gewonnen.
# - Das Lesen formaler Sprachen erfordert sorgfältiges Parsen sowie Aufmerksamkeit für Details in Interpunktion und Rechtschreibung, da im Gegensatz zu natürlichen Sprachen ein kleiner Fehler zu erheblichen Fehlern führen kann.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.7 Debugging
# - Programming can often involve making mistakes, which are commonly referred to as 'bugs'.
# - The process of identifying and fixing these mistakes is known as 'debugging'.
# - Debugging can sometimes trigger strong emotions such as anger, despondency, or embarrassment.

# %% [markdown] lang="de" tags=["slide"]
# ## 1.7 Debugging
# - Programmieren kann oft Fehler beinhalten, die gemeinhin als 'Bugs' bezeichnet werden.
# - Der Prozess, diese Fehler zu identifizieren und zu beheben, wird als 'Debugging' bezeichnet.
# - Debugging kann manchmal starke Emotionen wie Wut, Mutlosigkeit oder Peinlichkeit auslösen.

# %% [markdown] lang="en" tags=["slide"]
# - People tend to respond to computers in a way similar to their responses to people.
# - Should computers work effectively, they're treated as helpful teammates, but when they get obstinate or difficult, our responses often mirror those we would exhibit towards uncooperative individuals.

# %% [markdown] lang="de" tags=["slide"]
# - Menschen neigen dazu, auf Computer ähnlich zu reagieren wie auf andere Menschen.
# - Wenn Computer effektiv funktionieren, werden sie als hilfreiche Teammitglieder behandelt, aber wenn sie störrisch oder schwierig werden, spiegeln unsere Reaktionen oft diejenigen wider, die wir gegenüber unkooperativen Personen zeigen würden.

# %% [markdown] lang="en" tags=["slide"]
# - Considering the computer as an employee with specific strengths like speed and precision, and weaknesses such as an inability to grasp larger concepts or empathize can be helpful.
# - As a programmer, your job becomes managing these strengths and weaknesses: leveraging the strengths and mitigating the weaknesses.

# %% [markdown] lang="de" tags=["slide"]
# - Wenn man den Computer als Mitarbeiter mit spezifischen Stärken wie Geschwindigkeit und Präzision und Schwächen wie Unfähigkeit, größere Konzepte zu erfassen oder sich in andere hineinzuversetzen, betrachtet, kann das hilfreich sein.
# - Als Programmierer besteht Ihre Aufgabe darin, diese Stärken und Schwächen zu managen: die Stärken zu nutzen und die Schwächen zu minimieren.

# %% [markdown] lang="en" tags=["slide"]
# - Emotions should be utilized to engage with problems, but they should not interfere with productive work.
# - Debugging, while challenging, hones a valuable skill that is applicable to many activities beyond programming.
# - Each chapter's end contains suggestions for debugging to aid your learning process.

# %% [markdown] lang="de" tags=["slide"]
# - Emotionen sollten genutzt werden, um sich mit Problemen auseinanderzusetzen, dürfen aber nicht die produktive Arbeit beeinträchtigen.
# - Das Debugging, obwohl anspruchsvoll, schärft eine wertvolle Fähigkeit, die auf viele Aktivitäten über das Programmieren hinaus anwendbar ist.
# - Am Ende jedes Kapitels gibt es Vorschläge zum Debugging, um Ihren Lernprozess zu unterstützen.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.8 Glossary
# - Problem solving: The process of formulating a problem, finding a solution, and expressing it.
# - High-level language: A programming language like Python that is designed to be easy for humans to read and write.
# - Low-level language: A programming language that is designed to be easy for a computer to run; also called "machine language" or "assembly language".
# - Portability: A property of a program that can run on more than one kind of computer.

# %% [markdown] lang="de" tags=["slide"]
# ## 1.8 Glossar
# - Problemlösung: Der Prozess, ein Problem zu formulieren, eine Lösung zu finden und auszudrücken.
# - Hochsprache: Eine Programmiersprache wie Python, die darauf ausgelegt ist, von Menschen leicht gelesen und geschrieben zu werden.
# - Niedrigrsprache: Eine Programmiersprache, die darauf ausgelegt ist, von einem Computer leicht ausgeführt zu werden; auch als "Maschinensprache" oder "Assemblersprache" bezeichnet.
# - Portabilität: Eine Eigenschaft eines Programms, das auf mehr als einem Typ von Computer ausgeführt werden kann.

# %% [markdown] lang="en" tags=["slide"]
# - Interpreter: A program that reads another program and executes it.
# - Prompt: Characters displayed by the interpreter to indicate that it is ready to take input from the user.
# - Program: A set of instructions that specifies a computation.
# - Print statement: An instruction that causes the Python interpreter to display a value on the screen.

# %% [markdown] lang="de" tags=["slide"]
# - Interpreter: Ein Programm, das ein anderes Programm liest und ausführt.
# - Eingabeaufforderung: Zeichen, die vom Interpreter angezeigt werden, um anzuzeigen, dass er bereit ist, Eingaben vom Benutzer entgegenzunehmen.
# - Programm: Eine Reihe von Anweisungen, die eine Berechnung festlegen.
# - Print-Anweisung: Eine Anweisung, die den Python-Interpreter dazu bringt, einen Wert auf dem Bildschirm anzuzeigen.

# %% [markdown] lang="en" tags=["slide"]
# - Operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
# - Value: One of the basic units of data, like a number or string, that a program manipulates.
# - Type: A category of values such as integers (typeint), floating-point numbers (typefloat), and strings (typestr).
# - Integer: A type that represents whole numbers.

# %% [markdown] lang="de" tags=["slide"]
# - Operator: Ein spezielles Symbol, das eine einfache Berechnung wie Addition, Multiplikation oder Zeichenkettenverkettung darstellt.
# - Wert: Eine der grundlegenden Daten-Einheiten, wie eine Zahl oder Zeichenkette, die ein Programm manipuliert.
# - Typ: Eine Kategorie von Werten wie Ganzzahlen (Typ int), Gleitkommazahlen (Typ float) und Zeichenketten (Typ str).
# - Ganzzahl: Ein Typ, der ganze Zahlen darstellt.

# %% [markdown] lang="en" tags=["slide"]
# - Floating-point: A type that represents numbers with fractional parts.
# - String: A type that represents sequences of characters.
# - Natural language: Any one of the languages that people speak that evolved naturally.
# - Formal language: Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs.

# %% [markdown] lang="de" tags=["slide"]
# - Gleitkommazahl: Ein Typ, der Zahlen mit Dezimalstellen darstellt.
# - Zeichenkette: Ein Typ, der Zeichenfolgen darstellt.
# - Natürliche Sprache: Eine der Sprachen, die Menschen sprechen und die sich natürlich entwickelt haben.
# - Formale Sprache: Eine der Sprachen, die Menschen für spezifische Zwecke entworfen haben, wie z.B. zur Darstellung mathematischer Ideen oder Computerprogramme.

# %% [markdown] lang="en" tags=["slide"]
# - Token: One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.
# - Syntax: The rules that govern the structure of a program.
# - Parse: To examine a program and analyze the syntactic structure.
# - Bug: An error in a program.

# %% [markdown] lang="de" tags=["slide"]
# - Token: Eines der grundlegenden Elemente der syntaktischen Struktur eines Programms, analog zu einem Wort in einer natürlichen Sprache.
# - Syntax: Die Regeln, die die Struktur eines Programms regeln.
# - Parsen: Ein Programm untersuchen und die syntaktische Struktur analysieren.
# - Fehler: Ein Fehler in einem Programm.

# %% [markdown] lang="en" tags=["slide"]
# - Debugging: The process of finding and correcting bugs.
# %% [markdown] lang="de" tags=["slide"]
# - Debugging: Der Prozess des Findens und Behebens von Fehlern.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.9 Exercises
# - Explore and experiment with Python interactively as you learn.
# - Try intentionally making errors when writing code to learn about error messages.
#     - e.g., misspell a function, remove a necessary character.
# - Learning by doing not only enhances comprehension but also familiarizes you with troubleshooting.
# - Anticipating common errors minimizes accidental mistakes in the future.
# %% [markdown] lang="de" tags=["slide"]
# ## 1.9 Übungen
# - Erkunden und experimentieren Sie interaktiv mit Python, während Sie lernen.
# - Versuchen Sie absichtlich Fehler zu machen, wenn Sie Code schreiben, um mehr über Fehlermeldungen zu lernen.
#     - z.B. eine Funktion falsch schreiben, ein erforderliches Zeichen entfernen.
# - Durch Learning by doing wird nicht nur das Verständnis verbessert, sondern Sie werden auch mit der Fehlerbehebung vertraut gemacht.
# - Das Antizipieren von häufigen Fehlern minimiert zukünftige versehentliche Fehler.

# %% [markdown] lang="en" tags=["slide"]
# ## Experiment: Print Statement
# - Experiment with print statements.
#     - What if you omit one or both parentheses in a print statement?
#     - Try printing a string without the quotation marks.
# %% [markdown] lang="de" tags=["slide"]
# ## Experiment: Print-Anweisung
# - Experimentiere mit Print-Anweisungen.
#     - Was passiert, wenn du eine oder beide Klammern in einer Print-Anweisung weglässt?
#     - Versuche, einen String ohne Anführungszeichen zu drucken.

# %% [markdown] lang="en" tags=["slide"]
# ## Experiment: Python Notation
# - Experiment with numeric notation in Python.
#     - Can you use a plus sign (+) or a minus sign (-) before a number in Python?
#     - Try adding leading zeros before a number e.g., `09`, `011`.
#     - What happens if you have two values with no operator between them?

# %% [markdown] lang="de" tags=["slide"]
# ## Experiment: Python Notation
# - Experimentieren Sie mit numerischer Notation in Python.
#     - Können Sie in Python ein Pluszeichen (+) oder ein Minuszeichen (-) vor einer Zahl verwenden?
#     - Versuchen Sie, führende Nullen vor einer Zahl hinzuzufügen, z.B. `09`, `011`.
#     - Was passiert, wenn Sie zwei Werte haben, zwischen denen kein Operator steht?

# %% [markdown] lang="en" tags=["slide"]
# ## Exercises: Python as a Calculator
# - In this exercise session, use Python's capability as an interactive calculator.
#     - Compute the total seconds in 42 minutes and 42 seconds.
#     - Convert 10 kilometers into miles.
#     - Guess your average pace and average speed if you run a 10 kilometer race in 42 minutes 42 seconds.

# %% [markdown] lang="de" tags=["slide"]
# ## Übungen: Python als Taschenrechner
# - In dieser Übungssitzung verwenden Sie die Fähigkeit von Python als interaktiven Taschenrechner.
#     - Berechnen Sie die Gesamtsekunden in 42 Minuten und 42 Sekunden.
#     - Konvertieren Sie 10 Kilometer in Meilen.
#     - Schätzen Sie Ihr durchschnittliches Tempo und Ihre durchschnittliche Geschwindigkeit, wenn Sie einen 10-Kilometer-Lauf in 42 Minuten 42 Sekunden absolvieren.

# %% [markdown] lang="en" tags=["slide"]
# ## Python Notations
# Python supports many mathematical operations which are useful for calculating numeric expressions. Let's check out the snippet below.

# %% [markdown] lang="de" tags=["slide"]
# ## Python Notationen
# Python unterstützt viele mathematische Operationen, die nützlich sind, um numerische Ausdrücke zu berechnen. Schauen wir uns das Beispiel unten an.

# %%
# Calculation of seconds in 42 minutes 42 seconds
total_seconds = (42 * 60) + 42
print(f"Total Seconds: {total_seconds}")

# %%
# Conversion of kilometers to miles
miles = 10 / 1.61
print(f"Miles: {miles}")

# %%
# Calculation of average pace
avg_pace = total_seconds / miles
print(f"Average Pace (seconds per mile): {avg_pace}")

# %%
# Conversion of seconds to minutes and seconds
minutes = avg_pace // 60
seconds = avg_pace % 60
print(
    f"Average Pace (minutes and seconds per mile): {minutes} minutes {seconds} seconds"
)

# %%
# Calculation of average speed in miles per hour
avg_speed = miles / (total_seconds / 3600)
print(f"Average Speed (miles per hour): {avg_speed}")
