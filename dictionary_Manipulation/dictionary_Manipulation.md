#Dictionaries come in key-pair values meaning that within a dictionary lies a key (like a variable) and its value. You can have multiple key and values inside a dictionary. You can also have a list as a value in a key inside a dictionary.

student = {"Name" : "Nathan", "Age" : 23, "Courses" : ["Networking", "Assembly", "Data Structures and Algorithms"]}
print(student)

print(f"The student's name is {student["Name"]}")
print(f"Nathan is {student["Age"]} years old.")

courses = ", ".join(student["Courses"])
print(f"Nathan is currently taking up {courses}")

#Given a key that does not exist, if you utilize the usual method for accessing a value given a key in a dictionary, you will get a traceback error. In order to prevent this, one can use the .get() method in order to return "None" if a key does not exist in a given dictionary.

print(f"{student.get("Address")}")

#You can also change the default value that a .get() method returns when key is False.
print(student.get("Address", "Key does not exist."))

#You can also update the value of a given key.
student["Name"] = "Joseph"
print(student)

#The .update({}) method anables you to add and update multiple key and value pairs inside an existing dictionary.
student.update({"Name" : "Choy", "Age" : "19", "Phone" : "1223-123-1121"})
print(student)

#The del function deletes a key with its value inside the argument.
del student["Phone"]
print(student)

#You can also utilize .pop() method in order to remove a key and value pair depending on the argument. If it is wrapped on a variable, just like the original .pop() method, you can access the value(strictly) that was popped.

name = student.pop("Name")
print(student)
print(name)

#The .keys() method only shows the keys given a dictionary variable and the .values() method specifically shows the values of each key in the dictionary referenced. The .items() method returns the key, value pairs but each pair is inside a list.
print(student.keys())
print(student.values())
print(student.items())

#====================================================
#The Problem: Smartphone Inventory
#Start by creating a dictionary named phone with the keys "Brand" ("TechPhone"), "Model" ("X-100"), "Price" (900), and "Apps" (a list containing "Camera", "Maps", and "Calculator"). Once created, use an f-string to print the sentence "The TechPhone X-100 costs $900" by accessing the specific keys. Next, create a variable that uses .join() on the "Apps" list to separate them with a comma and space, and print the result as "Installed apps: Camera, Maps, Calculator".

#After displaying the current data, attempt to access a key named "Warranty" using the .get() method; configure it so that if the key does not exist, it prints "No Warranty Found" instead of None. Then, use the .update() method to simultaneously change the "Price" to 850 and add a new key "Color" with the value "Black", and print the dictionary to see the changes. Finally, use the .pop() method to remove the "Apps" key, saving the popped list into a variable named removed_apps (print this variable), and end the program by printing only the remaining keys of the dictionary.

phone = {
    "Brand": "TechPhone", 
    "Model": "X-100", 
    "Price": 900, 
    "Apps": ["Camera", "Maps", "Calculator"]
}

print(f"The {phone["Brand"]} {phone["Model"]} costs ${phone["Price"]}")

app_list = ", ".join(phone["Apps"])
print(f"Installed apps: {app_list}")

warranty_Check = phone.get("Warranty", "No Warranty Found")
print(warranty_Check)

phone.update({"Price" : 850, "Color" : "Black"})
print(phone)

removed_apps = phone.pop("Apps")
print(removed_apps)

print(phone.keys())
