while True:
    print("\nEVEN-ODD EVALUATOR\n")
    inputNumber = int(input("Enter an interger: "))
    modCalc = inputNumber % 2

    if modCalc == 0:
        print(f"The number {inputNumber} is even!")
    else:
        print(f"The number is {inputNumber} is odd!")

    decInput = input("Do you want to evaluate another number? (Y/N):")
    decInput = decInput.upper()
    if decInput == "Y":
        continue
    else:
        print("Thank you for using our program!")
        break