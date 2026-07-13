# A Function in Python is a package that contains a set of code to do a certain function when called out. The pass syntax makes a user-defined function exist even no lines of code within it exists. In order to utilize and execute a function, you just call the name of the function with the parenthesis.

def this_Function():
    pass

this_Function()

def hello_Function():
    print("Hello world!")

hello_Function()

#Print Bye world 5 times. This is an application of the coding framework called "DRY" or Don't Repeat Yourself.
def bye_Function():
    for i in range(5):
        print("Bye world!")

bye_Function()

# The return syntax returns a value when called out however it does not "output" that. You must utilize a print() function in order to see what a function has returned
def test_Function():
    return "This is a test."

print(test_Function())

#You can also utilize other functions such as .upper() and such in order to change what a function returns.
print(test_Function().upper())

#The parameters are referenced in a function and its value is then  given to a line of code within the function when it is called out. Given this instance, when the function was called out to execute as a print statement, the string "Joseph" was added as a parameter. In the user defined function, the parameter is defined as "name." When name_Function() was executed, the string "Joseph" was saved as a value in the parameter name. When name was called out inside the retrurn statement, the value for name was appended in the return statement.

def name_Function(name):
    return f"Hello! My name is {name}"

print(name_Function("Joseph"))

#The parameters inside a function can also be set up initially.

def name_FunctionTwo(name, greeting = "Good day!"):
    return f"{greeting} My name is {name}!"

print(name_FunctionTwo("Gab"))

# Vowel Counter problem

def vowel_Counter(word):
    vowels = 0
    for i in word.upper():
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            vowels += 1

    return vowels

print(vowel_Counter("Joseph"))

#Problem 2
store_inventory = {
    "apple": 1.50,
    "milk": 3.00,
    "bread": 2.50,
    "coffee": 5.00
}

# Notice the glitchy numbers mixed in!
customer_cart = ["apple", "bread", 404, "milk", "orange", 10] 

# This ends the part of the instructions.

def process_checkout(cart, inventory):
    total_cost = 0
    for i in cart:
        try:
            cartElement = int(i)
        except ValueError:
            if i not in inventory:
                print("Invalid key not detected. Skipping...")
                continue
            total_cost += inventory[i]
            continue

        else:
            print("Invalid interger detected. Skipping...")
            continue

    print(f"The total cost of your orders is {total_cost}")

process_checkout(customer_cart, store_inventory)
