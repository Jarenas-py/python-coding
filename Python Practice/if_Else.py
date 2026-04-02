# GEMINI PROBLEM    
#The Scenario:
#You are writing the software for an automated turnstile at a theme park. The program needs to check a 
# visitor's status and whether they signed the safety waiver before letting them in.

#Your Variables:
#Set up two variables at the top of your code to test with:
#visitor_type: A string that can be "VIP", "Regular", or "Employee".
#signed_waiver: A boolean that can be True or False.

#The Rules (Conditions):
#Write an if-else block that enforces the following rules:
#Rule 1: If the visitor_type is "Employee", they should always be allowed in, whether they signed the waiver or not. Print: "Welcome to work!"
#Rule 2: If the visitor has not signed the waiver, they cannot enter (unless they are an employee). Print: "Access Denied. Please sign the waiver."
#Rule 3: If the visitor_type is "VIP" and they have signed the waiver, print: "Welcome to the VIP fast lane!"
#Rule 4: If the visitor_type is "Regular" and they have signed the waiver, print: "Welcome to the park! Please enter the main line."
#Rule 5: If the system doesn't recognize the visitor_type at all, print: "Error: Invalid visitor type."

print("\nWELCOME TO ENCHANTED KINGDOM!\n")
visitor_type = ["VIP", "REGULAR", "EMPLOYEE"]

while True:
    visitor_input = str(input("Enter your visitor type: "))
    visitor_input = visitor_input.upper()
    if visitor_input in visitor_type:
        break
    else:
        print("Error: Invalid visitor type.")
        continue

if visitor_input == "VIP" or visitor_input == "REGULAR":
    while True:
        waiver_input = str(input("Did you sign the waiver? (Y/N): "))
        waiver_input = waiver_input.upper()
        if waiver_input == "Y" or "N":
            break
        else:
            print("Enter a valid input (Y/N))")
            continue

    while True:
        if waiver_input == "Y" and visitor_input == "VIP":
            print("Welcome to the VIP Fast Lane!")
            break
        elif waiver_input == "Y" and visitor_input == "REGULAR":
            print("Welcome to the park! Please enter the main line.")
            break
        elif waiver_input == "N" and visitor_input == "VIP" or visitor_input == "REGULAR":
            print("Access Denied. Please sign the waiver.")
            break

else:
    print("Welcome to work!")

#Gemini Results and Corrections:
#1. Line 16
#2. Line 22- Redundant Loop
#3. Redundant str casting.