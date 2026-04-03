#The Scenario:
#You are writing the software for an automated turnstile at a theme park. 
# The program needs to check a visitor's status and whether they signed the safety waiver before letting them in.

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

print("\nWELCOME TO PHONE REPAIRS 404\n")
print("""Welcome to PHONE REPAIRS 404
If you have problems with technicals, press 1.
If you have problems with Billings and Payments, press 2.
If you have problems with Store Hours and Location, press 3.
If you want to talk with a customer representative, press 9.\n""")

user_Input = int(input("Press a number: "))

while True:
    match user_Input:
        case 1:
            print("Routing you to Technical Support...")
            break
        case 2:
            print("Routing you to Billing and Payments...")
            break
        case 3:
            print("Routing you to Store Hours and Location...")
            break
        case 9:
            print("Connecting you to a human representative...")
            break
        case _:
            print("Invalid entry. Please try again.")
            break