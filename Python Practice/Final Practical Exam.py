class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None

	def appendEnd(self, data):
		newNode = Node(data)

		if not self.head:
			self.head = newNode
			return

		currentNode = self.head
		while currentNode.next:
			currentNode = currentNode.next

		currentNode.next = newNode
  
    
  
myList = Linkedlist()
stacks = 
  
#Main Program Flow
listahan = []
print("Probelm: IMPLEMENT\n")
inputString = input("Enter a string: ")
parseString = list(inputString)
myList.appendEnd(parseString)