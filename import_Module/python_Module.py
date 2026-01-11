#a source code in python becomes a "module" when its functions and code itself is utilized in another, separate python code. Take note of the python source code named "my_module.py". In order to access its code, a developer must utilize the "import" syntax in order to access the code from another module.

x = "This is the print statement from this file!"
print(x)

import my_module

#Import module names can also be "nicknamed" in order for the mto be called out much easier later on. Using the "as" after calling out the module in import then appending your desired "nickname" is a great way in order shorten the name of the module.

y = "This is the print statement from this file part 2!"
print(y)

import my_module2 as mm2

#Given a module that has multiple user defined functions and you want to import only that specific function for use in your separate python code base, you can utilize the "from and import" in order to do just that. A developer can also stack the "as" syntax in order to give that specific user-defined function from another module a nickname for easier access. (Please check the my_module.py in order to ascertain the functionality of the ohms_law function from the module my_module) 

from my_module import ohms_law as ol

while True:
    print("\nOhm's Law")
    
    while True:
        try:
            print("What variable are you trying to find? (VOLTAGE, CURRENT or RESISTANCE)")
            ohms_choice = input().upper()
            if ohms_choice in ["VOLTAGE", "CURRENT", "RESISTANCE"]:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Only enter VOLTAGE, CURRENT, or  RESISTANCE")

    while True:
        if ohms_choice == "VOLTAGE":
            try:
                val1 = float(input("Enter the resistance in Ohms: "))
                val2 = float(input("Enter the current in Amperes: "))
                break
            except ValueError:
                print("Only enter numbers.")
        elif ohms_choice == "CURRENT":
            try:
                val1 = float(input("Enter the voltage in Volts: "))
                val2 = float(input("Enter the resistance in Ohms: "))
                break
            except ValueError:
                print("Enter a valid number.")
        elif ohms_choice == "RESISTANCE":
            try:
                val1 = float(input("Enter the voltage in Volts: "))
                val2 = float(input("Enter the current in Amperes: "))
                break
            except ValueError:
                print("Enter a valid number.")

    ol(ohms_choice, val1, val2)

    while True:
        try:
            again_choice = input("Do you want to use again? (Y/N): ").upper()
            if again_choice in ["Y", "N"]:
                break
            else: 
                raise ValueError
        except ValueError:
            print("Enter a valid input. Only enter Y or N")

    if again_choice == "N":
        print("Thank you for using the program!")
        break
    elif again_choice == "Y":
        continue

#A developer can also import numerous functions from a module in one line statement. Check the my_module3.py in order to follow the functionality of the user-defined functions there.
from my_module3 import output1, output2
out1 = output1()
out2 = output2()
print(out1)
print(out2)

#A developer can also import all user-defined functions from a module using the "*". Please check the my_module4.py in order to ascertain its functionality.

from my_module4 import *
uno = func1()
dos = func2()
tres = func3()
quatro = func4()

print(uno)
print(dos)
print(tres)
print(quatro)

#When printing sys.path, it shows the different file paths the python accesses for its modules. The standard module of python (when downloaded, has different modules to start with that a developer can immediately utilize and import into their own source code). In an instance that you are working with a module and you want to ascertain the file path of which it is located, you could utilize the .__file__ syntax and print its file path. This goes for both standard library modules and user-defined modules.

import os
print("\n",os.__file__)

#Explore the standard library of python in order to get a hold of all the standard library modules that python has for cleaner and shorter code.
