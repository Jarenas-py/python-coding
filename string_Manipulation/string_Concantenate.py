message = "Hello"
messageTwo = "I'm Joseph!"
messageThree = "I'm stoked to see you!"

real_Message = message + ", " + messageTwo
print(real_Message) 

#with formatted string in application.

real_Message = "{}, {} Nice to meet you!".format(message, messageTwo)
print(real_Message)

#Using F-Strings
realMessage_Two = f"{message}, {messageTwo} I'm happy to see you."
print(realMessage_Two)

#Using F-Strings with basic functions
realMessage_Three = f"{message}, {messageTwo} {messageThree.upper()}"
realMessage_Four = f"{message.lower()}, {messageTwo.lower()} {messageThree.lower()}"
print(realMessage_Three)
print(realMessage_Four)
