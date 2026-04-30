#Your Coding Challenge: The Smart Vending Machine
#The Scenario:
#You are programming the main interface for a new, 
# digital vending machine. It needs a main menu, 
# a way to accept money safely, and a purchasing 
#system that checks if the user has enough funds.

#Your Variables:
#Start your program with a single variable to track the user's money:
#balance = 0

#The Rules:
#1. The Main Menu (match-case)
#Wrap your entire program in a while True: loop. Inside 
# the loop, ask the user to enter a number for the main menu. 
# Use a match-case block to handle their choice:
#Case 1 (Insert Money): Trigger the money insertion logic.
#Case 2 (Buy Item): Trigger the purchasing logic.
#Case 3 (Power Off): Print "Shutting down..." and break the main loop.
#Catch-All (_): Print "Invalid menu choice."

#2. Inserting Money (try-except & raise)
#If they choose Case 1, use a smaller while True: loop and a try-except 
# block to ask: "How much money would you like to insert? $"
#Attempt to convert their input to an integer (int()).
#If they enter a negative amount (e.g., -5), manually raise a ValueError with a custom message.
#If successful, add the inserted amount to their balance, print their new total, and break back to the main menu.
#Your except ValueError: block must catch both letters (like "five") and your manual negative 
# number error, printing "Please enter a valid positive amount." before letting them try again.

#3. Buying an Item (if-elif-else & logical operators)
#If they choose Case 2, ask them what they want to buy. The machine only has three items:
#Soda ($2)
#Chips ($3)
#Candy ($1)

#Use if, elif, and else combined with the and operator to enforce these conditions:

#If they select a valid item AND their balance is greater than or equal to the price,
#  print "Dispensing [Item]...", subtract the cost from their balance, print their 
# new balance, and return to the main menu.

#If they select a valid item but do not have enough money, print "Insufficient funds. 
# Please insert more money."

#If they type an item that doesn't exist, print "Item not found."

balance = 0
soda = 10
chips = 10
candy = 20

while True:
    print("""\nWELCOME TO THE DIGITAL VENDING MACHINE!
          
Instructions: Enter a number to use the system.
1. Deposit Money
2. Buy Product
3. Power Off\n""")
    decision_one = input("Enter input (1, 2, 3): ")

    match decision_one:
        case "1":
            while True:
                try:
                    balance = int(input("How much money would you like to insert in PHP?: "))
                    if balance >= 0:
                        print(f"""\nYour money has been deposited and your balance updated!
Your current balance is: {balance}$""")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid positive amount.")

        case "2":
            while True:
                try:
                    print(f"""What will be your order?
1. Soda: 2$ | {soda} left.
2. Chips: 3$ | {chips} left.
3. Candy: 1$ | {candy} left.""")
                    food_decision = input("Option (1, 2, or 3): ")

                    match food_decision:
                        case "1":
                            if balance >= 2:
                                balance -= 2
                                soda -= 1
                                print(f"""Dispensing Soda...
Current Balance: {balance}$
Soda left: {soda}""")
                                break
                            else:
                                print("Insufficient funds. Deposit new balance.")
                                break

                        case "2":
                            if balance >= 3:
                                balance -= 3
                                chips -= 1
                                print(f"""Dispensing Chips...
Current Balance: {balance}$
Chips left: {chips}""")
                                break
                            else:
                                print("Insufficient funds. Deposit new balance.")
                                break

                        case "3":
                            if balance >= 1:
                                balance -= 1
                                soda -= 1
                                print(f"""Dispensing Candy...
Current Balance: {balance}$
Candy left: {candy}""")
                                break
                            else:
                                print("Insufficient funds. Deposit new balance.")
                                break

                        case _:
                            raise ValueError
                except ValueError:
                    print("Error: Invalid menu choice. Pick within 1, 2, or 3 only!")
                    continue

        case "3":
            print("""Thank you for using the Digital Vending Machine!
Powering Off...""")
            break

        case _:
            print("\nInvalid menu choice")
            continue