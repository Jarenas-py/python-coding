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
#The following code shows this.

from random import random as r, seed as s

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

