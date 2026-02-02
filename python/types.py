"""
Python has types and collection types as well.
int, str, list, tuple, dict, set

Collection types are passed by reference which means they are mutable i.e. through a function

Functions can have variable types annotated which helps with readability and if you want to have a library statically look at your code.
"""

# All of the annotation is done without changing any functionality.
a: int = 1
b: str = "hi"

c_i: list[int] = [1, 2, 3]
c_s: list[str] = ["a","b","c"]

d_fixed: tuple[int, int] = (1, 2) 
d_variable: tuple[int, ...] = (1,2,3,4,5,6) # object can be used to denote a variable type

e: dict[str, int] = {"toast": 42}
ez: dict[int, int] = {1:2}

f: set[int] = {1, 2, 3}

# Practically, functions, classes, and modules can have the annotations listeda
def example(num: int) -> int:
    return num + 1

print(example.__annotations__)
