# Inheritance is a methodology in python to create a
# subclass (child class) that inherits all of the
# methods of the parent class. 

class Ford:
    def __init__(self, model, color, year, value):
        self.model = model
        self.color = color
        self.year = year
        self.value = value

    def fullReturn(self):
        return f"{self.model} {self.color} {self.year} {self.value}"

class Mitsubishi(Ford):
    pass

car1 = Ford("Everest", "Black", "2007", "400000")
car2 = Mitsubishi("Supra", "White", "2001", "1000000")

print(car1.fullReturn())
print(car2.fullReturn())

# When trying to create a subclass and making its
# own __init__ method by inheriting the parent
# class' __init__ method and adding another
# argument on the subclass __init__ method, the
# following code would be the exact methodology 
# to achieve that. "super().__init__(model, color, year, value)"
# simply tells the parent class that the following
# arguments stated inside the parenthesis are to
# be initialized by the __init__ method of the
# parent class.

class Subaru(Ford):
    def __init__(self, model, color, year, value, milleage):
        super().__init__(model, color, year, value)
        self.milleage = milleage

    def subaruReturn(self):
        return f"{self.model} {self.color} {self.year} {self.value} {self.milleage}"

car3 = Subaru("Impreza", "Blue", "1999", "800000", "500000")
print(car3.subaruReturn())

