class Stack:
	#栈的python实现
	def __init__(self):
		self.items = []

	def push(self, item):
		#append操作O(1)
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)
