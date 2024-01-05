""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Java Enums", "Java Enums") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction
# - Enums or Enumerations in Java are a special type of class that always contains a fixed set of constants.
# - They are the best way to define a collection of related things because they provide compile-time type safety.

""" Code cell """
# %%
public enum Days {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation for Enums
# - Enums are often used in switch statements to check for specific cases.
# - They can also be used to create a singleton, a design pattern that restricts the instantiation of a class to a single object.

""" Code cell """
# %%
public class Main {
    public static void main(String[] args) {
        Days day = Days.MONDAY;

        switch (day) {
            case MONDAY:
                System.out.println("It's Monday.");
                break;
            /* More cases... */
        }
    }
}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formal Definition
# - An enum is a special "class" that represents a group of constants (unchangeable variables, like final variables).
# - To create an enum, use the enum keyword (instead of class or interface), and separate the constants with a comma.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Applications of Enum
# - Enums can be used in Java to create a custom type with a fixed set of constants.
  
""" Code cell """
# %%
public enum Size {
    SMALL("S"), MEDIUM("M"), LARGE("L"), EXTRALARGE("XL");

    private String abbreviation;

    // enum constructor
    private Size(String abbreviation) {
        this.abbreviation = abbreviation;
    }

    public String getAbbreviation() {
        return this.abbreviation;
    }
}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations of Enums
# - Enums types have no instances other than those defined by its enum constants.
# - Enum constants are implicitly static and final and can't be changed once created.
# - Enum types cannot be instantiated.
# - Enum types cannot be subclassed.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Hands-on Workshop
# - Try to create your own enum with custom properties and methods.
# - Use your enum in a switch statement or as a type for a variable in your program.
# This hands-on exercise will give you a feel of practical Enum usage in java. Enjoy Coding!

