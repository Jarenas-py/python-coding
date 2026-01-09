#a source code in python becomes a "module" when its functions and code itself is utilized in another, separate python code. Take note of the python source code named "my_module.py". In order to access its code, a developer must utilize the "import" syntax in order to access the code from another module.

x = "This is the print statement from this file!"
print(x)

import my_module

#Import module names can also be "nicknamed" in order for the mto be called out much easier later on. Using the "as" after calling out the module in import then appending your desired "nickname" is a great way in order shorten the name of the module.

y = "This is the print statement from this file part 2!"
print(y)

import my_module2 as mm2
