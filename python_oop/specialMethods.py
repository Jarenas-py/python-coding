# Special methods in python classes are called 
# magic methods or dunder methods due to the 
# fact that those methods are named with double
# underscores hence "dunder". Special methods
# are resereved python methods that it calls automatically.

# Common Dunder Methods

# 1. __str__
# This specific dunder method enables one to 
# print something by format just by calling
# the instance itself. Unlike formulating
# a custom method for returning a string,
# the __str__ dunder method does that itself given
# a format. Another difference is that one can 
# call the instance itself rather than pairing it
# with the name of the method.

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f"{self.first} {self.last}"

instance1 = Person("Joseph", "Arenas")
print(instance1)

