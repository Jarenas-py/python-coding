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

	def appendHead(self, data):
		newNode = Node(data)
		tempNode = self.head
		self.head = newNode
		self.head.next = tempNode
		del tempNode

	def appendMid(self, data, post):
		currentNode = self.head
		currentPost = 0
	
		while True:
			if currentPost == post:
				newNode = Node(data)
				previousNode.next = newNode
				newNode.next = currentNode
				break

			previousNode = currentNode
			currentNode = currentNode.next
			currentPost += 1

	def delEnd(self):
		currentNode = self.head
		while currentNode.next:
			previousNode = currentNode
			currentNode = currentNode.next

		del currentNode
		previousNode.next = None

	def delChoice(self, post):
		currentNode = self.head
		currentPost = 0

		while True:
			if currentPost == post:
				previousNode.next = currentNode.next
				del currentNode
				break
		
			previousNode = currentNode
			currentNode = currentNode.next
			currentPost += 1

	def printingTime(self):
		elems = []
		
		currentNode = self.head
		while currentNode:
			elems.append(currentNode.data)
			currentNode = currentNode.next

		print(elems)

myList = Linkedlist()
myList.appendEnd(1)
myList.appendEnd(3)
myList.appendEnd(4)
myList.printingTime()

myList.appendHead(0)
myList.printingTime()

myList.appendMid(2, 2)
myList.printingTime()

myList.delEnd()
myList.printingTime()

myList.delChoice(3)
myList.printingTime()