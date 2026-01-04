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

print("""=====================================
      Here is a simple algorithm that reverses a list using what has been discussed so far.""")
print("The list is")
