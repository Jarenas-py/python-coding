print("This is the print statement from my_module.py!")

def name_call(name):
    return f"Hello world! My name is {name}"

def ohms_law(choice, num1, num2):
        if choice == "VOLTAGE":
            v = num1 * num2
            print(f"The voltage is {v}V")
        elif choice == "CURRENT":
            a = num1 / num2
            print(f"The current in amperes is {a}A")
        else:
            r = num1 / num2
            print(f"The resistance in ohms is {r}ohms")
