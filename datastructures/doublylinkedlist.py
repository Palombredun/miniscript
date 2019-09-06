class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		node = Node(data)

		if not self.head:
			self.head = node
		