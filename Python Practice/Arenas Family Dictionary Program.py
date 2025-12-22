arenas_Family= {
  "Father" : {
  "Name" : "Joey Arenas",
  "Location" : "United States"
  }, 
  "Mother" : {
  "Name" : "Marizza Arenas",
  "Location" : "Philippines",
  },
  "Male Child" : {
  "Name" : "Joseph Arenas",
  "Location" : "Philippines"
  },
  "Female Child" : {
  "Name" : "Marianne Arenas",
  "Location" : "Philippines"
  }
}
pamilya= arenas_Family.items()
for x in pamilya:
  print(x)
  
print(f"{arenas_Family["Father"]["Name"]} is currently residing in the {arenas_Family["Father"]["Location"]}.")