#Classes in pythons have different classifications
#of methods namely Instance Methods, Class Methods,
# and Static methods. Instance methods are simply
# methods that take in class instnaces in due to 
# the fact that that specific method requires
# the arguments of the class instance.

# Instance Method
# In this example, we can see an instance method
# in action. The instance method "printAll" is
# bound to the instance which is set as its argument.
# This means that the instance method relies on 
# instance variables for it to properly return the
# arguments of instance1. Instance methods are the
# most common type of class methods.

class instanceMethod():
    def __init__(self, car, color, value):
        self.car = car
        self.color = color
        self.value = value

    def printAll(self):
        return f"I am going to buy the {self.color} {self.car} that costs ${self.value}."

instance1 = instanceMethod("Ford Everest", "black", 2000)
print(instance1.printAll())
print("\n\n")
#=====================================================

# Class Methods
# In this example, class methods was utilized. One must be
# wary of the common use case of class methods. First is
# for the creation of alternative constructors. Second
# is for subclassing in the presence of inheritance.
# In this example, the first use case for class methods 
# were demonstrated. Before the explanation of the code,
# one must also be aware of the difference of a normal
# constructor and an alternative constructor.

# A normal constructor refers to a method that every 
# class has that has a set argument format. It's
# basically __init__ method in python Classes and
# even if one never explicitly codes them on the
# start of a class, an empty one is created. A 
# normal constructor is basically built-in to be 
# made in python.

# An alternative constructor on another hand is a
# user defined method (manually made method that
# is not built in in python) that takes in a value
# that is not in accordance to the argument structure
# of __init__. In this instance, an input "05-22-05",
# which is not in accordance with the __init__
# argument structure of "month", "day", and "year",
# is taken in as the input argument as "input" in 
# the class method "fullDate". The "cls" argument
# refers to the class itself. The class method, 
# updates the class after it has done the .split
# function.


class classMethod():
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    @classmethod
    def fullDate(cls, input):
        month, day, year = input.split("-")
        return cls(month, day, year)

userInput = input("Enter date: ")
testclassMethod = classMethod.fullDate(userInput)
print(f"{testclassMethod.month} {testclassMethod.day} {testclassMethod.year}")
print("\n\n")

#=========================================================

#Static Methods
# A common use case for static methods are simply for
# function. When a method would just purely do a 
# function, when a simple argument is needed for it 
# to do a job, utilize static methods. Instead of making
# it a function outside, just pair it in with methods
# of similar function inside the class. This 
# example would just show however how to create a static
# method. 

class TemperatureConverter:
    def __init__(self, unit):
        self.unit = unit

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def is_valid_celsius(value):
        return value >= -273.15

print(TemperatureConverter.celsius_to_fahrenheit(100))
print(TemperatureConverter.fahrenheit_to_celsius(100))
print(TemperatureConverter.fahrenheit_to_celsius(50))