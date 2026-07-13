citizen = {"Name" : "null", "Age" : 0, "University" : "null"}


while True:
    try:
        pangalan = input("Enter First Name: ")
        if not isinstance(pangalan, str):
            raise ValueError
        else:
            break
    except ValueError:
        print("Error: Input contains non-string characters.")
        continue

while True:
    try:
        gulang = input()
