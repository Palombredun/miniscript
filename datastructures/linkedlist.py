class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		node = Node(data)

		if self.head == None:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node