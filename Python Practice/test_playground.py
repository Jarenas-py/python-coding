class testClass():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"

    def out(self):
        return f"\n{self.email} Pay: {self.pay}"
    
firstInstance = testClass("Joseph", "Arenas", 20000)
print(firstInstance.out())