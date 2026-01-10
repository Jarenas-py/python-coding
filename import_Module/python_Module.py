#a source code in python becomes a "module" when its functions and code itself is utilized in another, separate python code. Take note of the python source code named "my_module.py". In order to access its code, a developer must utilize the "import" syntax in order to access the code from another module.

x = "This is the print statement from this file!"
print(x)

import my_module

#Import module names can also be "nicknamed" in order for the mto be called out much easier later on. Using the "as" after calling out the module in import then appending your desired "nickname" is a great way in order shorten the name of the module.

y = "This is the print statement from this file part 2!"
print(y)

import my_module2 as mm2

#Given a module that has multiple user defined functions and you want to import only that specific function for use in your separate python code base, you can utilize the "from and import" in order to do just that. A developer can also stack the "as" syntax in order to give that specific user-defined function from another module a nickname for easier access.

from my_module import ohms_law as ol

while True:
    print("\nOhm's Law")
    
    while True:

        try:
            print("What variable are you trying to find? (VOLTAGE, CURRENT or RESISTANCE)")
            ohms_choice = input().upper()
            if ohms_choice == "VOLTAGE" or "CURRENT" or "RESISTANCE":
                break
        except input_error:
            print("Invalid input. Only enter VOLTAGE, CURRENT, or  RESISTANCE")

    while True:
        if ohms_choice == "VOLTAGE":
            try:
                val1 = float(input("Enter the resistance in Ohms: "))
                val2 = float(input("Enter the current in Amperes: "))
                break
            except input_error:
                print("Only enter numbers.")
        elif ohms_choice == "CURRENT":
            try:
                val1 = float(input("Enter the voltage in Volts: "))
                val2 = float(input("Enter the resistance in Ohms: "))
            except input_error:
                print("Enter a valid number.")
            try:
                val1 = float(input("Enter the voltage in Volts: "))
                val2 = float(input("Enter the current in Amperes: "))
                break
            except input_error:
                print("Enter a valid number.")

    ol(ohms_choice, val1, val2)

    while True:
        try:
            again_choice = input("Do you want to use again? (Y/N): ").upper()
            if again_choice == "Y" or "N":
                break
        except input_error:
            print("Enter a valid input. Only enter Y or N")

    if again_choice == "N":
        print("Thank you for using the program!")
        break
    else:
        continue

