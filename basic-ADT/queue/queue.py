class Queue():
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		#左边为rear,右边为front;即右边为队首
		#insert(0)操作为O（n)
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)
