#The if-else statements syntax in python is the most basic form for doing conditional statements in Python.

if True:
    print("The statement is True")
else:
    print("The statement is False")


if False:
    print("The statement is True")
else:
    print("The statement is False")

language = "HTML"
if language == "python":
    print("The language is Python!")
elif language is "HTML":
    print("The language is HTML!")
else:
    print("There is no match :(")

#There are other comparison operators that can be utilized instead of "==" but only to a certain extent ">" and etc... through the form of "and", "or",  "is", and "not". The "is" acts like a "=='. The "and" STRICTLY considers both of the values of the compared variables. The "or" only considers either one of the values only to be true and lastly "not" changes the boolean value of a given variable.

user = "Admin"
logged_in = "True"

if user is "Admin" or logged_in:
    print("You have sucessfully logged in!")
else:
    print("Please log in.")

if not logged_in:
    print("You have not logged in.")
else:
    print("You are logged in!")

if user is "Admin" and not logged_in:
    print(f"Hello {user}! Please log in.")
else:
    print(f"Hello {user}! You are currently logged in!")
