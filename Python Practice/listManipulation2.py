numerals = [1, 2, 3]
numerals.reverse()
print(numerals)

numerals2 = [2, 5, 7, 20, 98, 31, 7,]
numerals2.sort()
print(numerals2)

numerals2.sort(reverse = True)
print(numerals2)

print(f"The least value in numerals2 is {min(numerals2)}")
print(f"The maximum value in numerals2 is {max(numerals2)}")
print(f"The sum of all numbers inside the list numerals2 is: {sum(numerals2)}")
print(f"Is 98 inside the list numerals2? {98 in numerals2}")

for i in numerals2:
    print(i)

for i, j in enumerate(numerals2, start = 1):
    print(i, j)

fruits = ["banana", "apple", "mango"]
fruits_join = ", ".join(fruits)
print(fruits_join)

fruits_split = fruits_join.split(", ")
print(fruits_split)
print("=======================\n")

#The Scenario:
#You have been hired as a data analyst for a local tech shop. The store manager handed you some raw data about their current inventory and prices, and they need you to process it into a clean report.

#Your Starting Variables:
#Copy and paste these exact variables at the top of your code to begin:

raw_inventory_string = "Webcam,Monitor,Keyboard,Mouse,Headset"
prices = [45, 120, 35, 20, 85, 10, 250]

inventory = raw_inventory_string.split(",")
inventory.sort()
prices.reverse()




print(inventory)
print(prices)