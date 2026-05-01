courses = ["OOP", "DSA", "Embedded Systems"]
people = ["nigga", "jew", "netanyahu"]

print(courses[0])
print(courses[2:])
courses.append("mobile app")
print(courses)
courses.insert(0,"networking")
print(courses)
courses.extend(people)
print(courses)
courses.remove("jew")
print(courses)
courses.pop()
print(courses)

courses.sort()
print(courses)

tickets = ["Printer Jam", "Password Reset", "Network Down"]
transferred_tickers = ["Email Sync Issue", "Update OS"]
new_tickets = []

tickets = tickets[:2]
print(tickets)

tickets.append("Blue Screen")
print (tickets)

tickets.insert(0, "CEO Laptop")
print(tickets)

tickets.remove("Password Reset")
print(tickets)

tickets.pop()
print(tickets)