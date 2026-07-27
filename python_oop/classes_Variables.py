#Class variables are simply variables inside a class. 
# They are different from instance variables because 
# instance variables are tied to the instance 
# itself and is exclusive to itself. A class variable 
# gives the ability to share class objects despite 
# the instance that is accessing them. Simply put,
#class variables give more flexibility/options to the 
# developer if values are to be inherited all
# throughout classes rather than fixing them on a 
# method.

class testClass():

    raise_value = 1.5
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + "@gmail.com"

    def printAll(self):
        return f"""
First Name: {self.first}
Last Name: {self.last}
Pay: {self.pay}
Email: {self.email}"""

    def applyRaise_class(self):
        raise_applied = self.pay * testClass.raise_value
        return f"Pay Raised Value: {raise_applied}"

    def applyRaise_instance(self):
        raise_applied2 = self.pay * self.raise_value
        return f"Pay Raised Value: {raise_applied2}"

instance1 = testClass("Joseph", "Arenas", 5000)
instance2 = testClass("John", "Doe", 10000)
instance3 = testClass("Jude", "Simmons", 3000)
instance4 = testClass("Walter", "White", 500)

#There are two ways to access and utilize class
#variables and the two last methods inside 
#testClass() showcases this. The first methodology 
#is by declaring the class name itself followed by 
# the name of the variable. As you can see, it can
#be observed that regardless of the instance, the
#class variable's value is inherited althroughout
#instances. Even if one sets the class variable
#of an instance, that instance cannot override
#if the class variable is accessed via the class
#itself. Hence, the same values of instance1.applyRaise_instance()
#despite the decalaration of 

print(instance1.raise_value)
print(instance2.raise_value)
print(instance1.applyRaise_class())
print(instance2.applyRaise_class())

instance1.raise_value = 2
print(instance1.raise_value)
print(instance1.applyRaise_class())

#The second methodology accesses the class variable through
# an instance. As observed, when the instance sets the value
# of the class variable, it is inherited on the applyRaise_instance()
# method due to the fact that the value for the class
# variable gotten was from the instance and not the default value
# set on the class variable.

print("\n\n")
print(instance3.raise_value)
print(instance4.raise_value)
print(instance3.applyRaise_instance())
print(instance4.applyRaise_instance())

instance3.raise_value = 4
instance4.raise_value = 3
print(instance3.raise_value)
print(instance3.applyRaise_instance())

print(instance4.raise_value)
print(instance4.applyRaise_instance())