fruit= ["apples", "oranges", "bananas"]
vegetables= ["lettuce", "cabbage", "carrots"]
fruit.extend(vegetables)
fruitsAndVegetables= fruit
print(fruitsAndVegetables)
confirmationUno= input("Do you want to delete all vegetables? (y/n): ")

if confirmationUno == 'y':
	del fruitsAndVegetables[3:]
else:
	print("Alright! Vegetables will not be deleted.")
print(fruitsAndVegetables)

confirmationDos= input("Do you want to clear all fruits? (y/n): ")

if confirmationDos== 'y':
	fruit.clear()
	print(fruitsAndVegetables)
	newFruits= input("Input three new fruits: ")
	fruit.append(newFruits)
	print(fruitsAndVegetables)
else:
	print("Alright! Nothing has been changed!")
	print(fruitsAndVegetables)