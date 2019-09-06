
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class CircularQueue:
	"""Exemple of implementation : round robin in a tournament"""
	def __init__(self):
		self.tail = None
		
