# A Function in Python is a package that contains a set of code to do a certain function when called out. The pass syntax makes a user-defined function exist even no lines of code within it exists. In order to utilize and execute a function, you just call the name of the function with the parenthesis.

def this_Function():
    pass

this_Function()

def hello_Function():
    print("Hello world!")

hello_Function()

#Print Bye world 5 times. This is an application of the coding framework called "DRY" or Don't Repeat Yourself.
def bye_Function():
    tracker = 4
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
