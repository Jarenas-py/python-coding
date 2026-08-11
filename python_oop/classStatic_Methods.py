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