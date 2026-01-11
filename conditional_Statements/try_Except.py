#The try-except conditional takes in a line of code with potential error and moves that line of code to the except case in order to handle the error that was in the try block.

try:
    num_test = int(input("Enter a number to divide: "))
    quotient = num_test / 0
    print(f"The quotient is: {quotient}")
except ZeroDivisionError:
    print("This is not a valid output.")

#A developer can utilize a raise in order to raise a ValueError in concjunction with if else statements in order for a developer to tailor their exception catching.

while True:
    print("Hello World!")

    while True:
        try:
            choice = input("Do you want to loop again (Y/N): ").upper()
            if choice in ["Y", "N"]:
                break
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid input of only Y or N.")

    if choice == "Y":
        continue
    else:
        print("Thank you for using our program!")
        break
