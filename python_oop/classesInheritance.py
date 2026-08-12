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