class Node():
	"""链表中的节点，包括数据域和指针域；使用单链表实现"""
	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

	def set_next(self, next_node):
		#python内变量为引用类型，可视作指针
		self.next = next_node

	def get_next(self):
		return self.next


class OrderedList():
	"""有序列表"""
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def size(self):
		#排除特殊情况
		count = 0
		node = self.head
		while node != None:
			count += 1
			node = node.get_next()
		return count

	def remove(self, item):
		"""
		1、找到则删除，未找到不做任何操作
		2、删除节点关键是定位相邻节点；左节点可以用previous表示，右节点用current.get_next()表示
		3、所以两个变量previous与current至关重要
		4、删除头结点要分类讨论
		"""
		found = False
		current = self.head
		previous = None
		while current != None and not found:
			if current.get_data() == item:
				#found相当于指示器，相当于break
				found = True
				#previous为None:删除头结点
				if previous == None:
					self.head = current.get_next()
				else:
					previous.set_next(current.get_next())
			else:
				previous = current
				current = current.get_next()

	def search(self, item):
		current = self.head
		#trigger1
		found = False 
		#trigger2
		stop = False
		#current is not None既表示当前列表非空，也是判断条件：遍历到了list末尾；双关
		while current is not None and not found and not stop:
			if item == current.get_data():
				#找到目标值，触发trigger1,退出循环
				found = True
			else:
				if item < current.get_data():
					#由于list顺序排列，一旦当前考察值大于目标值，触发trigger2,退出循环
					stop = False
				else:	
					#自增项;只有当前值小于目标值才自增
					current = current.get_next()
		return found

	def add(self, item):
		#1、找到合适位置，记录在current、previous中
		current = self.head
		previous = None
		stop = False
		while current is not None and not stop:
			if current.get_data() > item:
				stop = True
			else:
				#只有trigger:stop未触发情况下才自增
				previous = current
				current = current.get_next()
		temp_node = Node(item)
		if current == self.head:
			temp_node.set_next(current)
			self.head = temp_node
		else:
			temp_node.set_next(current)
			previous.set_next(temp_node)


if __name__ == '__main__':
	mylist = OrderedList()
	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)

	print(mylist.size())
	print(mylist.search(93))
	print(mylist.search(100))
