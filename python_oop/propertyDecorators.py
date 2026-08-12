# Property Decorators helps methods in python
# to be utilized as plain attirubtes when trying 
# to call said methods.

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullName(self):
        return f"{self.first} {self.last}"

student1 = Student("Joseph", "Arenas")
print(student1.fullName)