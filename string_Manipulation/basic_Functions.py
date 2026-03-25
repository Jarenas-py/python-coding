message = "He's got the whole world, in His hands."
print(message.upper()) #Changes the message value to all capital letters.
print(message.lower()) #Changes the message value to all lower case letters.
print(message.count("Hello")) #Finds the string "Hello". If none, it prints 0. If there is, it prints the interger of how many that string is is in the value of the variable message.
print(message.find("world")) #Finds the string world and finds the its index in the value of the variable message.

message = message.replace("He's got the whole world, in His hands.", "Hello world!") #Replaces the whole value of message. It takes 2 positional arguments. The first argument is the initial argument while the second argumnt is the argument for replacing the initial value.
print(message)
