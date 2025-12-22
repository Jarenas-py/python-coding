print("\nWord Finder\n")
txt= input("Enter a block if text, sentence or phrase: ")
wordFind= input("\nEnter the word you want to find: ")

if wordFind in txt:
	print(f"\nYes, the word '{wordFind}'' is present.")
else:
	print(f"\nThe word '{wordFind}'' is not present.")