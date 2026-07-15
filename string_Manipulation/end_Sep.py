#The end is a print keyword argument wherein given
#multiple print statements, the print statement with
#the end keyword argument would have its value printed
#before the next print statement.

# Example 1: 
print("Hello! I am", end = " ")
print("John")
#Output: "Hello! I am John."

# Example 2: 
print("The quick brown ", end = "fox ")
print("jumps over the lazy", end = " dog")
print(".")
#Output: "The quick brown fox jumps over the lazy dog."

#The sep keyword argument for print statements
#applies given a print statement with multiple
# string arguments. The sep keyword argument takes
# whatever value it has and inputs it in between
# each string argument in the print statement.

# Example 1:
print("My", "name", "is", "John", sep = " ")

# Example 2:
print("My", "name", "is", "John", sep = "-")

# Example with both sep and end keyword argument:
print("Programming","Essentials","in", sep = "***", end = "...")
print("Python")

#Output: Programming***Essentials***in...Python
