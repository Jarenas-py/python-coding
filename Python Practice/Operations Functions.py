def add(a1, a2):
    return a1 + a2

def sub(s1, s2):
    return s1 - s2

def mult(m1, m2):
    return m1 * m2

def round_Off(r):
    return round(r)

def div(d1, d2):
    return d1 / d2

while True:
    print("""\nMENU
          (1) Addition
          (2) Subtraction
          (3) Multiply
          (4) Round Off
          (5) Divide
          (6) Quit Program""")
    choice= int(input("\nWhat is your choice? (1-6): "))
    
    if choice == 1:
        print("\nADDITION")
        a1= int(input("Enter the first number: "))
        a2= int(input("Enter the second number: "))
        print(f"The sum is {add(a1, a2)}")
        
    elif choice == 2:
        print("\nSUBTRACTION")
        s1= int(input("Enter the first number: "))
        s2= int(input("Enter the second number: "))
        print(f"The sum is {sub(s1, s2)}")
        
    elif choice == 3:        
        print("\nMULTIPLICATION")
        m1= int(input("Enter the first number: "))
        m2= int(input("Enter the second number: "))
        print(f"The sum is {mult(m1, m2)}")
        
    elif choice == 4:
        print("\nROUND OFF")
        r= int(input("Enter the number to be rounded off: "))
        print(f"The sum is {round_Off(r)}")
        
    elif choice == 5:
        print("\nDIVISION")
        d1= int(input("Enter the first number: "))
        d2= int(input("Enter the second number: "))
        print(f"The sum is {div(d1, d2)}")
        
    elif choice == 6:
        print("\nThank you for using our program!")
        exit()
        
    else:
        print("\nError: Enter a valid input.")
        
    choiceDos = input("\nDo you want to restart the program? (Y/N): ").upper()
    if choiceDos == 'y':
        continue
    else:
        print("\nThank you for using our program!")
        exit()
exit()