# j2 from 'macros.j2' import header
# {{ header("Strings", "Strings") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Chapter 8: Strings
# - Strings differ substantially from data types like integers, floats, and booleans
# - A string is a sequence, indicating it’s an ordered collection of other values
# - This chapter explores accessing string characters and introduces string methods

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Strings in Python
# - Strings in Python are sequences of characters
# - Each character in a string can be accessed using indexing
# - Python strings are immutable, meaning they cannot be changed after creation
# - Plenty of methods are available for string manipulation and inquiry
# %% [markdown] lang="en" tags=["slide"]
# ## A String as a Sequence
# - Strings in Python are sequences of characters allowing access to each character using brackets `[]`.
# - Selecting a character using its index in the format `string[index]` retrieves the character at that position.
# - Indexing starts at 0, hence `fruit[0]` references the first character of the string `fruit`.
# - Index values must be integers, not floats or other types. Attempting to use a non-integer index results in a `TypeError`.

# %%
fruit = 'banana'
letter = fruit[1]

# %%
letter

# %%
letter = fruit[0]

# %%
letter

# %%
i = 1
selected_letter = fruit[i]
next_letter = fruit[i+1]

# %%
selected_letter, next_letter

# %%
# Attempting to use a non-integer index:
# letter = fruit[1.5] # Uncommenting this line will raise a TypeError
# %% [markdown] lang="en" tags=["slide"]
# ## Understanding `len` Function in Strings
# - `len` is a built-in function that returns the total number of characters in a string.
# - It is used to determine the length of the string, aiding in various string manipulation operations.

# %% [markdown] lang="en" tags=["slide"]
# ## Accessing the Last Character
# - Attempting to access the string index equal to its length results in `IndexError`.
# - Strings in Python are zero-indexed, hence indices run from `0` to `length-1`.
# - To access the last character, subtract `1` from the string's length.

# %% [markdown] lang="en" tags=["slide"]
# ## Using Negative Indices
# - An alternative to get the last character is using negative indices.
# - Negative indexing starts from `-1` at the end of the string moving backwards, making it easier to access the end characters.

# %%
fruit = 'banana'
len(fruit)

# %%
length = len(fruit)
# Attempting to access index equal to length of the string causes an error
# last = fruit[length] # Uncommenting this will cause an IndexError

# %%
# Correct way to access the last character
last = fruit[length-1]
print(last)

# %%
# Using negative indices to simplify access
print(fruit[-1]) # Last character
print(fruit[-2]) # Second last character
# %% [markdown] lang="en" tags=["slide"]
# ## Strings: Traversal with a `for` loop
# - Traversing a string involves processing it one character at a time
# - Commonly, traversal starts from the beginning, processes each character, and continues until the end
# - This section covers the basics of string traversal using both `while` and `for` loops

# %% [markdown] lang="en" tags=["slide"]
# ### Using a `while` Loop for Traversal
# - A `while` loop can be used for string traversal by incrementing an index from 0 to the length of the string - 1
# - The loop displays each character of the string on a new line
# - As an exercise, consider writing a function to display a string's characters in reverse order

# %%
index = 0
fruit = "banana"
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# %% [markdown] lang="en" tags=["slide"]
# ### Traversal with a `for` Loop
# - A `for` loop simplifies traversal by automatically iterating over each character in a string
# - No explicit handling of the string length or index is necessary
# - The following examples demonstrate string operations and concatenation in a traversal context

# %%
fruit = "banana"
for letter in fruit:
    print(letter)

# %% [markdown] lang="en" tags=["slide"]
# ### Generating an Abecedarian Series
# - String concatenation and `for` loops can generate sequences like the abecedarian series
# - Example given: Generating names from "Make Way for Ducklings" by Robert McCloskey
# - Exercise: Correct the output to accurately spell "Ouack" and "Quack"

# %%
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

# %% [markdown] lang="en" tags=["slide"]
# ### Correcting Spelling in the Series
# - Modifying the previous loop to correctly spell names such as "Ouack" and "Quack" presents a practical exercise in string manipulation

# %%
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in ["O", "Q"]:
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
# %% [markdown] lang="en" tags=["slide"]
# ## 8.4 String slices
# - A slice of a string selects a segment of the string. This operation is similar to selecting a single character but focuses on a range.
# - Use the syntax `s[n:m]` to return the string segment from the "n-th" character to the "m-th" character, including the first but excluding the last.
# - Imagine indices pointing between characters for better intuition. 

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding String Slices
# - Omitting the first index in the slice starts it at the beginning of the string.
# - Omitting the second index extends the slice to the end of the string.
# - A slice where the first index is greater than or equal to the second results in an empty string.

# %%
# Demonstration of string slicing
s = 'Monty Python'
print(s[0:5])  # Outputs 'Monty'
print(s[6:12])  # Outputs 'Python'

# %%
# Slicing with omitted indices
fruit = 'banana'
print(fruit[:3])  # Outputs 'ban', starting from the beginning
print(fruit[3:])  # Outputs 'ana', extending to the end of the string

# %%
# Example of an empty string result from slicing
print(fruit[3:3])  # Outputs '', an empty string

# %% [markdown] lang="en" tags=["slide"]
# - Experimenting with slices, such as `fruit[:]`, helps to understand the behavior of Python strings. Try different slices to see their results.
# %% [markdown] lang="en" tags=["slide"]
# ## Strings are Immutable
# - Attempting to change a character in a string using the `[]` operator triggers a `TypeError`
# - Strings in Python are immutable, meaning their characters cannot be altered after creation
# - To modify a string, a new string must be created as a variation of the original

# %% [markdown] lang="en" tags=["slide"]
# ### Attempting to Modify a String
# - Incorrect approach: Using `[]` on the left side of an assignment in hopes of changing a character
# - Correct approach: Create a new string incorporating the desired changes
# - Example: Concatenating a new character with a slice of the original string creates a modified version

# %%
# Incorrect approach that leads to TypeError
greeting = 'Hello, world!'
# greeting[0] = 'J'  # Uncommenting this line would result in a TypeError

# %%
# Correct approach to modify a string
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)  # Outputs: 'Jello, world!'
# %% [markdown] lang="en" tags=["slide"]
# ## 8.6 Searching
# - Discuss the purpose and functionality of custom search functions in Python
# - Explore a specific example of a search function in Python

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding the `find` Function
# - A function designed to search for the first occurrence of a character within a string
# - Returns the index of the found character or -1 if not found
# - Utilizes a `while` loop to traverse the string until the character is found or the end of the string is reached

# %%
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# %% [markdown] lang="en" tags=["slide"]
# ## How `find` Works
# - Deconstructs the process of searching by traversing through each character of a string
# - Highlights the significance of the `return` statement in controlling loop termination and function output
# - Embodies a common programming pattern known as a "search"

# %% [markdown] lang="en" tags=["slide"]
# ## Enhancing the `find` Function
# - Exercise: Extend the functionality of `find` by introducing a third parameter
# - This parameter specifies the starting index for the search within the string
# - Aims to provide more flexibility in how and where searches are conducted within strings

# %%
# Example enhancement of the find function
def find_with_start(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
# %% [markdown] lang="en" tags=["slide"]
# ## 8.7 Looping and Counting
# - Learn to count specific characters in a string
# - Understand the concept of a counter within loops
# - Encapsulate counting logic into a function for reusability
# - Implement an alternative approach using the `find` method

# %% [markdown] lang="en" tags=["slide"]
# ### Counting Letter Occurrences in Strings
# - The goal is to count how many times a particular letter appears in a string
# - A counter variable is used to keep track of the occurrences
# - This introduces a common pattern in programming known as a counter

# Example Code:
# %%
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# %% [markdown] lang="en" tags=["slide"]
# ### Creating a General Function
# - Encapsulate the counting logic into a function named `count`
# - The function should accept both the string and the letter to search for as arguments
# - This makes the counting operation more flexible and reusable

# %% 
def count(word, search_letter):
    count = 0
    for letter in word:
        if letter == search_letter:
            count += 1
    return count

# Test the function
print(count('banana', 'a'))  # Expected output: 3

# %% [markdown] lang="en" tags=["slide"]
# ### Alternative Approach Using `find`
# - Instead of looping through the string manually, use the string method `find` to simplify the process
# - The `find` method can accept three parameters: the character to find, the start position, and the end position

# Implementing the updated `count` function:
# %%
def count_using_find(word, search_letter):
    count = 0
    start = 0
    while True:
        start = word.find(search_letter, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move to the next character
    return count

# Test the function
print(count_using_find('banana', 'a'))  # Expected output: 3
# %% [markdown] lang="en" tags=["slide"]
# ## String Methods
# - String objects in Python are equipped with a variety of useful methods for text manipulation.
# - Methods are similar to functions but are invoked using a different syntax, often enhancing readability and conciseness.
# - This section explores common string methods like `upper()` and `find()`, demonstrating their usefulness through examples.

# %% [markdown] lang="en" tags=["slide"]
# ## Invoking String Methods
# - The `upper()` method transforms a string into all uppercase letters, following the syntax `word.upper()`.
# - Unlike a regular function call, methods use dot notation and often do not require any arguments.
# - Methods return a new string resulting from the operation, leaving the original string unchanged.

# %% [markdown] lang="en" tags=["slide"]
# ## Example: Using `upper()`
# - Let's convert the word 'banana' into uppercase letters using the `upper()` method.
# - Notice how the method call is made directly on the string object.

# %%
word = 'banana'
new_word = word.upper()
new_word

# %% [markdown] lang="en" tags=["slide"]
# ## The `find()` Method
# - The `find()` method searches for a substring within a string and returns the index of its first occurrence.
# - It's more general than simple character searches, as it can locate substrings as well.
# - The method can take optional arguments to specify the start and end positions for the search.

# %% [markdown] lang="en" tags=["slide"]
# ## Example: Simple `find()`
# - Using `find()` to locate the first occurrence of 'a' in 'banana'.
# - Demonstrating its ability to find substrings, not just individual characters.

# %%
word = 'banana'
index = word.find('a')
index

# %%
substr_index = word.find('na')
substr_index

# %% [markdown] lang="en" tags=["slide"]
# ## Advanced `find()` Usage
# - `find()` allows specifying where to start the search with an optional second argument.
# - A third optional argument can define where the search should end, enhancing its flexibility.
# - This makes `find()` consistent with Python’s slicing operator, which also does not include the end index in its range.

# %%
start_search_index = word.find('na', 3)
start_search_index

# %%
# Searching with both start and end limits.
name = 'bob'
search_fail = name.find('b', 1, 2)
search_fail
# %% [markdown] lang="en" tags=["slide"]
# ## The `in` Operator
# - The `in` operator is a boolean operator used to check if one string contains another
# - It returns `True` if the first string appears as a substring in the second
# - Useful in functions to compare strings or find common characters

# %% [markdown] lang="en" tags=["slide"]
# ## Example of `in` Operator
# - To check if 'a' exists in 'banana': `'a' in 'banana'` results in `True`
# - Checking if 'seed' is a substring of 'banana': `'seed' in 'banana'` results in `False`

# %%
'a' in 'banana'

# %%
'seed' in 'banana'

# %% [markdown] lang="en" tags=["slide"]
# ## Function Utilizing `in` Operator
# - A function `in_both` can highlight intersecting letters between two words
# - It iterates through one word to find common letters present in another
# - This showcases the readability of Python with well-chosen variable names

# %%
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

# %% [markdown] lang="en" tags=["slide"]
# ## Demonstrative Example with `in_both` Function
# - Using `in_both` to compare 'apples' with 'oranges' outputs common letters
# - The letters 'a', 'e', and 's' are printed, illustrating shared characters

# %%
in_both('apples', 'oranges')
# %% [markdown] lang="en" tags=["slide"]
# ## 8.10  String Comparison
# - Relational operators can be used to compare strings in Python.
# - Checking equality between strings is done using `==`.
# - Alphabetical ordering of words can be checked with relational operators.

# %% [markdown] lang="en" tags=["slide"]
# ## String Comparison in Practice
# - Be aware that Python distinguishes between uppercase and lowercase letters during comparison.
# - Uppercase letters are considered "smaller" than lowercase letters.
# - It's a good practice to convert strings to a common format (e.g., all lowercase) before comparison.

# %%
if word == 'banana':
    print('All right, bananas.')

# %%
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# %%
# Example of how uppercase letters are considered in comparison
print('Pineapple' < 'banana')  # This will print True due to uppercase 'P' being "smaller" than lowercase 'b'

# %%
# Converting strings to lowercase for comparison
word = 'Pineapple'
if word.lower() < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word.lower() > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')
# %% [markdown] lang="en" tags=["slide"]
# ## Debugging Strings in Python
# - Debugging involves strategies like checking indices in loops to prevent errors
# - Guardian patterns help validate assumptions, improving code reliability
# - Identifying and fixing index range errors is crucial in string manipulation
# - A step-by-step approach, with diagnostic prints, aids in isolating issues

# %% [markdown] lang="en" tags=["slide"]
# ### Understanding the Issue with String Indices
# - Incorrect indices in traversing strings can lead to `IndexError`
# - It's essential to start and end traversal appropriately to avoid out-of-range errors
# - The `is_reverse` function illustrates a common mistake by accessing an out-of-range index

# %%
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)

    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

# %% [markdown] lang="en" tags=["slide"]
# ### Debugging Step by Step
# - Debugging starts by printing indices to understand the error's nature
# - After identifying the error, adjust indices correctly for effective string traversal
# - Validate the fix by rerunning and observing the code behavior

# %%
# Inserting print statement for debugging
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)

    while j > 0:
        print(i, j)        # Debug print
        
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

# Error demonstration
# This will cause an IndexError due to incorrect j index
# >>> is_reverse('pots', 'stop')

# %% [markdown] lang="en" tags=["slide"]
# ### Correcting the Initial Index Error
# - Adjust the initial index of `j` to `len(word2) - 1` to match the last character's index
# - Code correction leads to successful comparison for reverse strings without index errors
# - Continuous debugging may reveal additional logical errors needing attention

# %%
# Corrected code
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1  # Corrected initialization of j

    while j >= 0:  # Corrected condition to include 0
        print(i, j)  # Debug print
        
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

# Correct usage example
# >>> is_reverse('pots', 'stop')

# %% [markdown] lang="en" tags=["slide"]
# ### Solving Logical Errors and Finalizing Debugging
# - Observing the loop's iteration count can reveal logical discrepancies
# - Drawing state diagrams or other visual aids helps conceptualize execution flow
# - Fixing logical errors alongside index errors ensures correct and expected function behavior
# %% [markdown] lang="en" tags=["slide"]
# ## Python Strings: Glossary
# - An object or value can refer to many things, including sequences and strings
# - Sequences are ordered collections, accessible by index, starting at 0 in Python
# - Items are elements in a sequence; an index is used to select them

# %% [markdown] lang="en" tags=["slide"]
# ## String Operations and Characteristics
# - A slice of a string is a subrange, specified by indices
# - The empty string is denoted as `""`, having zero length
# - Strings are immutable, meaning their elements cannot be altered after creation

# %% [markdown] lang="en" tags=["slide"]
# ## Navigating and Utilizing Strings
# - To traverse a string means to iterate over its items, often performing operations
# - Searching in strings involves traversing until a specific condition or item is found
# - A counter is typically used to tally occurrences or track positions, starting from 0

# %% [markdown] lang="en" tags=["slide"]
# ## Advanced String Operations
# - Method invocation is the process of calling a function or method in a string
# - Some functions or methods accept optional arguments, which are not mandatory for the operation
# %% [markdown] lang="en" tags=["slide"]
# ## 8.13  Exercises - String Manipulations
# - Explore Python's string methods through the [official documentation](http://docs.python.org/3/library/stdtypes.html#string-methods). Experiment with methods like `strip` and `replace`.
# - Utilize the string method `find(sub[, start[, end]])` to understand optional arguments.
# - Learn and apply the string method `count` to count occurrences of 'a' in 'banana'.

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 1: String Method Exploration
# - Consult the Python documentation to learn about string methods.
# - Practice with methods such as `strip` and `replace` for string cleaning and manipulation.
# - Delve into method syntax, for example, `find(sub[, start[, end]])` illustrates optional arguments.

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 2: Counting Characters
# - Understand the `count` string method by reading its documentation.
# - Use `count` to determine the number of times 'a' appears in "banana".

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 3: Slicing and Steps
# - Learn how string slicing can accept a third index for step size.
# - Experiment with step sizes, including using -1 for reversing a string.
# - Apply this technique to craft a one-liner `is_palindrome` function.

# %%
# Example of slicing with steps
fruit = 'banana'
fruit[0:5:2]

# %%
# Example of reversing a string with slicing
fruit[::-1]

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 4: Case Detection Functions
# - Below are functions intended to check for lowercase letters in strings. Some have flaws.
# - Examine and test each function to determine its correctness.
# - Discuss what each function actually does and identify any errors.

# %% [markdown] lang="en" tags=["slide"]
# ### Function any_lowercase1
# - Intended to check if any characters in a string are lowercase.
# - Only checks the first character, then returns either `True` or `False`.

# %%
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# %% [markdown] lang="en" tags=["slide"]
# ### Function any_lowercase2
# - Purports to check for lowercase characters.
# - Incorrectly checks the string 'c' instead of the variable `c`.

# %%
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# %% [markdown] lang="en" tags=["slide"]
# ### Function any_lowercase3
# - Aims to detect any lowercase letters.
# - Only returns the case of the last character in the string.

# %%
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# %% [markdown] lang="en" tags=["slide"]
# ### Function any_lowercase4
# - Checks for any lowercase letters in a string.
# - Correctly accumulates the check across all characters.

# %%
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# %% [markdown] lang="en" tags=["slide"]
# ### Function any_lowercase5
# - Tests if all characters in a string are lowercase.
# - Returns False at the first uppercase character, correctly checks the entire string otherwise.

# %%
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# %% [markdown] lang="en" tags=["slide"]
# ## Exercise 5: Caesar Cipher
# - Understand how a Caesar cipher encrypts text by rotating letters.
# - Implement a function, `rotate_word`, to rotate each letter of a word by a specified amount.
# - Utilize `ord` and `chr` functions for character code conversion.
# - Decipher jokes encoded in ROT13 as an application of the Caesar cipher.

# %%
def rotate_word(s, n):
    """
    Rotates each letter in the input string s by n places.
    """
    rotated = ''
    for char in s:
        rotated += chr(((ord(char) - ord('a') + n) % 26) + ord('a'))
    return rotated

# Usage example
rotate_word('hello', 3)
# j2 from 'macros.j2' import header
# {{ header("Strings", "Strings") }}

# j2 from 'macros.j2' import header
# {{ header("Strings", "Strings") }}

