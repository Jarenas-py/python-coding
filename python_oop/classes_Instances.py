#Classes in python are a versatile way in order to group lines of code and user-defined functions that can also be reused. In the context of a python class, a method is a user-defined function. Just like a user-defined function, in order for a class to exist whilst having no attributes nor methods within it, a developer can use the "pass" syntax in order for that to happen.

class testClass:
    pass

#Do take note that a class and an "Instance of a Class" are different. An instance of a class is a class at run time. Running two instances of the same classes are not the same at run time. In this example,m the class "testClass" are stored in two instances name first_class and second_class. When printing those instances, it shows two different memory addresses which proves the point that given a same class, when stored on separate variables and ran on execution, they are two different instances with their respective "world" so to speak.

first_class = testClass()
second_class = testClass()
print(first_class)
print(second_class)

#An attribute in python classes are akin to variables with values but in the context of a class. 

first_class.first = "Joseph"
first_class.last = "Arenas"
first_class.age = "21"

second_class.first = "John"
second_class.last = "Adams"
second_class.age = "32"

print(f"\nName: {first_class.first} {first_class.last} Age: {first_class.age}")
print(f"Name: {second_class.first} {second_class.last} Age: {second_class.age}")
