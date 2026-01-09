print("This is the print statement from my_module.py!")

def name_call(name):
    return f"Hello world! My name is {name}"

def ohms_law(num1, num2, choice, choice2):
    
    while True:
        print("Ohm's Law!\n")

        while True: 
            try:
                if choice == "VOLTAGE" or "AMPERES" or "RESISTANCE":
                    break
            except word_error:
                print("This is not a valid input")
                continue

        if choice == "VOLTAGE":
            v = num1 * num2
            print(f"The voltage is {v}V")
        elif choice == "AMPERES":
            a = num1 / num2
            print(f"The current in amperes is {a}A")
        else:
            r = num1 / num2
            print(f"The resistance in ohms is {r}ohms")

        while True:
            try:
                if choice2 == "N":
                    print("Thank you for using our program!")
                    break
            except word_error:
                print("This is not a valid input!")
                continue

