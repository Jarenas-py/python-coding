courses = ["OOP", "DSA", "Embedded Systems"]

#Accessing strings are similar to string slicing.
print(courses[0])

#Placing -1 as the argument will return the last element in the string.
print(courses[-1])

#Apply other slicing methodologies in order to access a list.
print(courses[:2])
print(courses[2:])

#Utilize the .append() to add elements at the end of the list.
courses.append("Networking")
print(courses)

#The .insert() function provides an argument to place elements in a custom manners using the index as the argument to be utilized.
courses.insert(2, "Logic Programs")
print(courses)

#One can also utilize the .insert() function in order to insert a list within a list.
courses_Two = ["course1", "course2"]
courses.insert(0, courses_Two)
print(courses)

#The .extend() function takes another list's elements and appends them to another list given the argument on what index to extend it from.
fruits_One = ["Apple", "Banana", "Mango"]
fruits_Two = ["Dragon Fruit", "Grapes"]
fruits_One.extend(fruits_Two)
print(fruits_One)

#The .remove() method removes an element in the list provided that the argument the developer has set is indeed inside the list.
fruits_One.remove("Apple")
print(fruits_One)

#The .pop() method removes the last element in a list.
popped = fruits_One.pop()
print(fruits_One)

#The .pop() method returns the last element that was removed.
print(popped)

#===================================================================================================

print("""=====================================
      Here is a simple algorithm that reverses a list using what has been discussed so far.
      The list contains the following elements: A B C D""")

alphabet = ["A", "B", "C", "D"]
alphabet_Reverse = []
tracker = 0

while True:
    popped = alphabet.pop()
    alphabet_Reverse.append(popped)
    tracker += 1

    if tracker == 4:
        print(alphabet_Reverse)
        break

#Another method to reverse the order of the elements given a list is using the .reverse() method.
colors = ["red", "blue", "green"]
colors.reverse()
print(colors)

#The .sort() method sorts a string list alphabetically or intergers and floating point numbers in ascending order.
sort_Fruits = ["bananas", "dragon fruit", "grapes", "apples"]
sort_Fruits.sort()
print(sort_Fruits)

numeral = [91, 5, 455, 203, 784, 65, 45]
numeral.sort()
print(numeral)

#In order to reverse a list using the .sort() method, one can input a "reverse=True" argument inside the method.
numeral.sort(reverse= True)
print(numeral)
