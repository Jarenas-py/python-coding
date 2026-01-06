#The for loop statement iterates given a data store. In this specific instance, "num" is the variable that trackes each iteration of the loop and stops if there is no more to iterate anymore.

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

print("=================================================\n")

# The break statement breaks the loop no matter the condition.

for num in nums:
    print(num)
    if num == 3:
        print(f"The number {num} has been found!")
        break

print("============================================\n")

#The continue statement continues the loop.
for num in nums:
    print(num)
    if num == 3:
        print(f"The number {num} has been found!")
        continue

    elif num == 5:
        print(f"The number {num} has been found!")
        break

print("==========================================\n")

#Nested for loops are possible 

for num in nums:
    for letters in "abcd":
        print(num, letters)

print("=========================================\n")

#The function range() can be utilized in a for loop in order to limit the iterations in a for loop.

for numbers in range(1, 11):
    print(numbers)
