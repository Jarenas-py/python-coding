while True:
    while True:
        try:
            pasok = input("Enter only 1, 2, or 3: ")
            if pasok in ["1", "2", "3"]:
                print("Number inputted is within the specified range")
                break
            else:
                raise ValueError
        except ValueError:
            print(f"Number inputted which is {pasok} is not within specified range.")
            continue

    print("Thank you for using the program!")
    break