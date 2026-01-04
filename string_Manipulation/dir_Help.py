#dir shows all of the methods that are available given the variable you have referenced dir with.
message = "This is a string."
print(dir(message))

#The help function (with the argument being a data type inside) shows detailed information on what methods you can utilized with respect to the argument (data type) the developer has inputted inside the help function. 

#print(help(str))

#You can also add a method top the data type in order to ascertain and output the function of a specific basic function

print(help(str.upper))
