#The match-case is the switch-case equivalent of Python.
print("We are going to print number 10")
number = 10

match number:
    case 1:
        print("This is not number 10")
    case 13:
        print("This is number 13")
    case 10:
        print("This is number 10! We found it!")
