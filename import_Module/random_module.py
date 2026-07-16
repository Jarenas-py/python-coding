#The random module in python focuses on entities and 
# functions that randomizes a group of numbers. 

#Common functions of the random python module is the random
# and seed functions. Simply put, given an input, random 
# just returns a random number inbetween 0 and 1.0. 
# seed(), in conjunction with random() shows what seems like 
# a random set of numbers but when executed multiple times 
#given a value in seed, it would return the same string of 
#numbers. Think of python having infinite number of pages
# full of determined numbers on each page. Those pages are 
# the seeds. This means that if seed(1), and you execute
#random() with it, it would return the same string of numbers.
#randint() simply takes two arguments. The starting number,
#and the ending number. It will simply return a random
# value that is lowest number <= x >= highest number.
# randrange() can take 3 arguments but can take even 1 or two.
# At 1 argument, it takes in the limit numeral and returns
# a random interger that cannot exceed the specified argument.
# At 2 arguments, it simply acts as randint. At 3 arguments,
# the third argument acts as the step or the interval just
# like in the method range() in python.
#Lastly, choice() takes in a list and outputs a random
#element within it while sample() takes in another 
#argument that dictates how many elements inside
# the list will it randomly return.

#The following code shows this.

from random import random as r, seed as s, randrange as rR, randint as rI, choice as c, sample as sA
globalList = [1243,2346,245745,3124563457,1252346,15234,1232346,456]

class randomizer():
    def __init__(self, x):
        self.x = x

    def random(self):
        for i in range(3):
            print(r())

    def seed(self):
        s(self.x)
        for j in range(3):
            print(r())

    def randint(self):
        print("\nFIRST INSTANCE\nRANDINT OUTPUT: ")
        for i in range(4):
            print(rI(55, 109))

    def randrange(self):
        print("\nSECOND INSTANCE\nRANDRANGE OUTPUT: ")
        for i in range(4):
            print(rR(10, 100, 10))
    
    def choice(self):
        chosen = c(globalList)
        return chosen
    
    def sample(self):
        sampleOutput = sA(globalList, 3)
        return sampleOutput

firstInstance = randomizer(3)
counter = 0
while True:
    print(f"\nFIRST INSTANCE\nRandom Output: ")
    firstInstance.random()
    print(f"\nSeed Random Output: ")
    firstInstance.seed()
    counter += 1

    if counter == 2:
        break

secondInstance = randomizer(1234123)
counter = 0
while True:
    print(f"\nSECOND INSTANCE\nRandom Output: ")
    secondInstance.random()
    print(f"\nSeed Random Output: ")
    secondInstance.seed()
    counter += 1

    if counter == 2:
        break

firstInstance.randint()
secondInstance.randrange()

print(firstInstance.choice())
print(secondInstance.sample())