# j2 from 'macros.j2' import header
# {{ header("What is a program?", "What is a program?") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Chapter 1: The Way of The Program
# - The goal of this chapter is to encourage you to think like a computer scientist
# - Computer scientists blend the best aspects of mathematics, engineering, and natural science
#   - They use formal languages to denote ideas similar to mathematicians,
#   - They assemble components into systems and considering tradeoffs like engineers,
#   - They observe and analyse the behavior of complex systems like scientists,

# %% [markdown] lang="en" tags=["slide"]
# ## Problem-Solving Skills in Programming
# - The primary skill for a computer scientist is problem solving
# - Problem solving involves the ability to formulate problems, think creatively about solutions, and express them clearly and accurately
# - Learning to program is an excellent opportunity to practice problem-solving skills

# %% [markdown] lang="en" tags=["slide"]
# ## The Objective of Programming
# - On one level, the objective is to learn to program, a practical skill in itself
# - On another level, programming will be used as a tool to achieve another goal, which will be made clear as we proceed

# %% [markdown] lang="en" tags=["slide"]
# ## 1.1 What is a program?
# - A program is a sequence of instructions for computing.
# - Computations can be mathematical (like solving systems of equations) or symbolic (such as text searching).
# - Whether graphical processing or video playing, it all boils down into basic instructions which are common across languages.

# %% [markdown] lang="en" tags=["slide"]
# ## Basic Instructions in Programming
# - **Input**: Obtaining data from various sources.
# - **Output**: Displaying results or saving to different destinations.
# - **Math**: Executing basic arithmetic calculations.

# %% [markdown] lang="en" tags=["slide"]
# ## Basic Instructions in Programming (Continuation)
# - **Conditional Execution**: Checking conditions and executing appropriate code.
# - **Repetition**: Performing actions multiple times, often with slight modifications.
# - Every complex program is made up of these fundamental instructions.

# %% [markdown] lang="en" tags=["slide"]
# ## Programming as a Process
# - Programming can be considered as a process of breaking down complex tasks into smaller subtasks.
# - Subtasks are further simplified until they can be performed using the basic instructions.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.2 Running Python
# - Running Python can be a challenge for beginners who might have to install Python and related software
# - To avoid the simultaneous stress of learning system administration and programming Python can be run in a browser
# - There are several webpages where Python can be run, one of them is PythonAnywhere
# - For beginners, Python 3 is recommended as it is similar to Python 2 but has few differences

# %% [markdown] lang="en" tags=["slide"]
# - Python interpreter is a program that reads and executes Python code.
# - Your environment determines how you start the interpreter, possibly by clicking an icon or typing `python` on a command line.
# - The interpreter gives out information about itself and its running environment when it starts

# %%
print("Python 3.4.0 (default, Jun 19 2015, 14:20:21) [GCC 4.8.2] on linux")
print('Type "help", "copyright", "credits" or "license" for more information.')
print(">>>")

# %% [markdown] lang="en" tags=["slide"]
# - The displayed information would differ depending on your operating system, you need to check that the version number starts with a 3.
# - An indicated version number starting with 2 would mean you are running Python 2
# - The last line displayed is a prompt for you to enter code

# %%
print(">>> 1 + 1")
print(2)

# %% [markdown] lang="en" tags=["slide"]
# - If you type a line of code and hit Enter, the interpreter displays the result
# - Once you are comfortable starting the Python interpreter and running code, you are ready to get started
# - Henceforth, the assumption is that you know how to start the Python interpreter and run code.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.3 The First Program
# - The first program typically written in any new language is "Hello, World!".
# - This program simply displays the words "Hello, World!".
# - In Python, the "Hello, World!" program utilizes the `print` function to display result on the screen.
# - A `print` statement does not actually print anything on paper.

# %%
print("Hello, World!")

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Python Syntax
# - Quotation marks in a `print` statement define the starting and ending of the text to be displayed.
# - These quotation marks do not appear in the output.
# - Parentheses indicate that `print` is a function.
# - Further details on functions will be covered in Chapter 3.

# %% [markdown] lang="en" tags=["slide"]
# ## Differences in Python Version
# - In Python 2, the `print` statement is not a function and thus, does not use parentheses.
# - Agreater clarity on this distinction between Python 2 and Python 3 will be provided in subsequent sessions.

# %%
# Example of print statement in Python 2
# print 'Hello, World!'
# %% [markdown] lang="en" tags=["slide"]
# ## 1.4 Arithmetic operators
# - Python provides special symbols known as arithmetic operators for mathematical computations.
# - These operators include + (addition), - (subtraction), * (multiplication), and / (division).
# - There's also the ** operator, used for exponentiation, which means raising a number to a power.
# - A notable operator in other languages, ^, is a bitwise operator called XOR in Python, not used for exponentiation as one might expect.

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

# %%
# More arithmetic operations examples
print(84 / 2)  # Division
print(6**2 + 6)  # Exponentiation

# %% [markdown] lang="en" tags=["slide"]
# - The operator ^ in Python is a bitwise operator called XOR, which may offer unexpected results if used for exponentiation.
# - Note: Bitwise operators are not covered in this notebook, but you can learn more about them from Python's official documentation or other online resources.

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

# %%
# Displaying the type of different value
print(type(2))
print(type(42.0))
print(type("Hello, World!"))

# %% [markdown] lang="en" tags=["slide"]
# - Values like '2' and '42.0' might look like numbers but they are strings as they are enclosed in quotation marks
# - Python interprets numbers with commas (e.g., 1,000,000) as a comma-separated sequence of integers, not as a single integer

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

# %% [markdown] lang="en" tags=["slide"]
# ## Syntax in languages
# - Syntax rules govern the structure of statements, for instance, '3 + 3 = 6' is syntactically correct while '3 + = 3 $ 6' is not in mathematics.
# - Syntax rules come in two flavors: tokens and structure.
#   - Tokens are the basic elements of a language, such as words, numbers, and chemical elements.
#   - The second type of syntax rule pertains to the way tokens are combined.

# %% [markdown] lang="en" tags=["slide"]
# ## Parsing and Main Features of Languages
# - The process of figuring out the structure of a sentence in a language is called parsing.
# - Formal and natural languages share certain features such as tokens, structure, and syntax.
# - There are key differences between these languages in terms of ambiguity, redundancy, and literalness.

# %% [markdown] lang="en" tags=["slide"]
# ## Contrast between Natural and Formal Languages
# - Natural languages, due to inherent ambiguity, employ lots of redundancy and often verbose while formal languages are less redundant and more concise.
# - Natural languages are full of idiom and metaphor and may not mean exactly what they say while formal languages mean exactly what they say.

# %% [markdown] lang="en" tags=["slide"]
# ## Importance of Understanding Formal Languages
# - As we all grow up speaking natural languages, it might require some adjustment to understand and use formal languages.
# - The understanding of a computer program, a form of formal language, is unambiguous and literal and is fully obtained from analysis of the tokens and structure.
# - Reading formal languages involves careful parsing and attention to detail in punctuation and spelling as unlike in natural languages, a small mistake can cause significant errors.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.7 Debugging
# - Programming can often involve making mistakes, which are commonly referred to as 'bugs'.
# - The process of identifying and fixing these mistakes is known as 'debugging'.
# - Debugging can sometimes trigger strong emotions such as anger, despondency, or embarrassment.

# %% [markdown] lang="en" tags=["slide"]
# - People tend to respond to computers in a way similar to their responses to people.
# - Should computers work effectively, they're treated as helpful teammates, but when they get obstinate or difficult, our responses often mirror those we would exhibit towards uncooperative individuals.

# %% [markdown] lang="en" tags=["slide"]
# - Considering the computer as an employee with specific strengths like speed and precision, and weaknesses such as an inability to grasp larger concepts or empathize can be helpful.
# - As a programmer, your job becomes managing these strengths and weaknesses: leveraging the strengths and mitigating the weaknesses.

# %% [markdown] lang="en" tags=["slide"]
# - Emotions should be utilized to engage with problems, but they should not interfere with productive work.
# - Debugging, while challenging, hones a valuable skill that is applicable to many activities beyond programming.
# - Each chapter's end contains suggestions for debugging to aid your learning process.

# %% [markdown] lang="en" tags=["slide"]
# ## 1.8 Glossary
# - Problem solving: The process of formulating a problem, finding a solution, and expressing it.
# - High-level language: A programming language like Python that is designed to be easy for humans to read and write.
# - Low-level language: A programming language that is designed to be easy for a computer to run; also called "machine language" or "assembly language".
# - Portability: A property of a program that can run on more than one kind of computer.

# %% [markdown] lang="en" tags=["slide"]
# - Interpreter: A program that reads another program and executes it.
# - Prompt: Characters displayed by the interpreter to indicate that it is ready to take input from the user.
# - Program: A set of instructions that specifies a computation.
# - Print statement: An instruction that causes the Python interpreter to display a value on the screen.

# %% [markdown] lang="en" tags=["slide"]
# - Operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
# - Value: One of the basic units of data, like a number or string, that a program manipulates.
# - Type: A category of values such as integers (typeint), floating-point numbers (typefloat), and strings (typestr).
# - Integer: A type that represents whole numbers.

# %% [markdown] lang="en" tags=["slide"]
# - Floating-point: A type that represents numbers with fractional parts.
# - String: A type that represents sequences of characters.
# - Natural language: Any one of the languages that people speak that evolved naturally.
# - Formal language: Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs.

# %% [markdown] lang="en" tags=["slide"]
# - Token: One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.
# - Syntax: The rules that govern the structure of a program.
# - Parse: To examine a program and analyze the syntactic structure.
# - Bug: An error in a program.

# %% [markdown] lang="en" tags=["slide"]
# - Debugging: The process of finding and correcting bugs.
# %% [markdown] lang="en" tags=["slide"]
# ## 1.9 Exercises
# - Explore and experiment with Python interactively as you learn.
# - Try intentionally making errors when writing code to learn about error messages.
#     - e.g., misspell a function, remove a necessary character.
# - Learning by doing not only enhances comprehension but also familiarizes you with troubleshooting.
# - Anticipating common errors minimizes accidental mistakes in the future.
# %% [markdown] lang="en" tags=["slide"]
# ## Experiment: Print Statement
# - Experiment with print statements.
#     - What if you omit one or both parentheses in a print statement?
#     - Try printing a string without the quotation marks.
# %% [markdown] lang="en" tags=["slide"]
# ## Experiment: Python Notation
# - Experiment with numeric notation in Python.
#     - Can you use a plus sign (+) or a minus sign (-) before a number in Python?
#     - Try adding leading zeros before a number e.g., `09`, `011`.
#     - What happens if you have two values with no operator between them?

# %% [markdown] lang="en" tags=["slide"]
# ## Exercises: Python as a Calculator
# - In this exercise session, use Python's capability as an interactive calculator.
#     - Compute the total seconds in 42 minutes and 42 seconds.
#     - Convert 10 kilometers into miles.
#     - Guess your average pace and average speed if you run a 10 kilometer race in 42 minutes 42 seconds.

# %% [markdown] lang="en" tags=["slide"]
# ## Python Notations
# Python supports many mathematical operations which are useful for calculating numeric expressions. Let's check out the snippet below.

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
