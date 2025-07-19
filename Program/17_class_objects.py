"""Python Classes and Objects"""
# Almmost everthingn in Python is an object. with its properties and Methods.
# A class is like an object constructor, or a "Blueprint" for creating objects.

"""Create a Class"""
# to create a class, use a the keyword class:
# Example: Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
    
"""Create a Object"""
# How we can use the class named MyClass to create objects:
# Example: Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x) # --> 5

"""The __init___() Function"""

# The examples aboves are classes and objects in their form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(). which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.

# Example: Create a class named Person, use the __init__() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Victor', 42)

print(p1.name) #--> Victor
print(p1.age) #--> 42

# Note: the __init__() function is called automatically every time the class is being used to create a new object

"""T"""