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

#The code above can be avoided by utilizing methods. Methods, in the context of classes in Python, are basically user-defined functions within a class. An essential method in a given classes would be the __init__(self): method. In this exapmle, "name1" and "name2" become separate instances for "secondClass." The self attribute acts as the catcher for the instance that links it to other attributes within the class. Given name1, parameters of name1 are taken by the secondClass and is instantly transfered to the parameters of the __init__. The goal of init is to initialize and save all of the parameters from the instance. With that __init__ now has Cory, Kenshin and 31 as the parameters for first, last and age. The self catches name1 and since self == name1, according to the __init__ method, self.first or name1.first and so on are equal to the parameters the instance has set. By printing those attributes, you get the values set derived from the parameters. Do take note that these are called instance variables because these variables are tied to their class instances.

class secondClass():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.fullInfo = f"Name: {first} {last} Age: {age}"

name1 = secondClass("Cory", "Kenshin", "31")
name2 = secondClass("James", "Smith", "40")

print("\n",name1.first)
print(name1.last)
print(name1.fullInfo)

print("\n",name2.first)
print(name2.last)
print(name2.fullInfo)

#The following code below demonstrates how you could utilize attributes set on the __init__ method on another method within the same class. Do take note that when executing a method through an instance, do not forget including a "()" on the end.

class thirdClass():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullName(self):
        return f"{self.first} {self.last}"

    def fullName2(self):
        print(f"{self.first} {self.last}")

name3 = thirdClass("Dane", "Johnson")
name4 = thirdClass("Megan", "Watson")
name5 = thirdClass("Test", "Function")

print("\n",name3.fullName())
print(name4.fullName())
name5.fullName2()

#You could also utilize the name of the class and referring to the instance of the class as its parameter in order to do the same functionality (printing the full name). 

name6 = thirdClass("Test", "User")
thirdClass.fullName2(name6)
