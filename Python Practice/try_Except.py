#The Scenario:
#You are programming the safety kiosk for a high-speed rollercoaster. 
# The ride has strict age requirements, and the kiosk needs to be crash-proof against bad user input.

#The Rules:
#Write a program that uses a while True: loop to continually ask the user for their age until
#they provide a valid one. Inside the loop, you must use a try-except block that enforces the following rules:
#The Input: Ask the user: "Enter your age in years: " and attempt to convert it into an int().
#The Manual Raise: If the user enters a number less than 0 (e.g., -5), explicitly raise a 
# ValueError with the message: "Age cannot be negative!"
#The Success Logic: * If the age is 12 or older, print: "You are old enough! Enjoy the ride!" 
# and break the loop.
#If the age is between 0 and 11, print: "Sorry, you must be at least 12 years old to ride." and break the loop.
#The Exception Catch: Your except ValueError block needs to catch both the error from someone typing letters 
# (like "ten") AND the negative number error you manually raised. When it catches the error, print: 
# "Invalid input. Please enter a valid positive number." and let the loop restart.

while True:
    print("\nSAFETY KIOSK ROLLERCOASTER")
    while True:
        try:
            age_Input = int(input("Enter you age in years: "))
            if age_Input >= 12:
                print("You are old enough! Enjoy the ride!")
                break
            else:
                raise ValueError
        except ValueError:
            if age_Input <= -1 or age_Input == str:
                print("Invalid input. Please enter a valid positive number.")
            elif age_Input >= 0 and age_Input <= 11:
                print("Sorry, you must be at least 12 years old to ride.")

    while True:
        try:
            next_Decision = input("Next? (Y/N): ").upper()
            if next_Decision in ["Y", "N"]:
                break
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid input (Y/N)")

    match next_Decision:
        case "N":
            print("Thank you for using the program!")
            break
        case "Y":
            continue