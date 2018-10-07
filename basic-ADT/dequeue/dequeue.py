
class Dequeue():
	def __init__(self):
		self.items = []

	def addFront(self, item):
		"""右侧为front"""
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		#删除元素要返回
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0) 

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

