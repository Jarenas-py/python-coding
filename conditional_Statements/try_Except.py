#The try-except conditional takes in a line of code with potential error and moves that line of code to the except case in order to handle the error that was in the try block.

try:
    num_test = int(input("Enter a number to divide: "))
    quotient = num_test / 0
    print(f"The quotient is: {quotient}")
except ZeroDivisionError:
    print("This is not a valid output.")

