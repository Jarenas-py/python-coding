#Tuples are immutable data structures meaning that elements cannot be added nor removed after initial screening. Although data inside a tuple can be accessed as usual, anything that related to data being manipulated are not possible. Please check "list_Manipulation.py" for functions that can be utlized that are non-mutable for reference on manipulating tuples. Do also take note that a tuple is unordered. Every execution, order of elements inside a tuple changes.

message = {"This", "is", "a", "tuple."}
print(message)

message_Two = " ".join(message)
print(message_Two)
