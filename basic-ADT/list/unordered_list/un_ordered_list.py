
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

class UnOrderedList():
	"""无序列表的实现"""
	def __init__(self):
		"""
		构造函数创建一个空list
		空的单链表等价于头部为空；根据头部可以遍历出所有所有链表信息
		故list只存储头部节点即可
		"""
		#头部节点初始为None
		self.head = None

	def add(self, item):
		"""在链表head添加元素"""
		temp_node = Node(item)
		temp_node.set_next(self.head)
		self.head = temp_node

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

	def search(self, item):
		found = False
		current = self.head
		while current != None and not found:
			if current.get_data() == item:
				#found相当于指示器，相当于break
				found = True
			else:
				current = current.get_next()
		return found

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

	def append(self, item):
		"""追加操作，链表首都append需要分类讨论"""
		current = self.head
		if current == None:
			self.head = Node(item)
		else:
			current = self.head
			#寻找链表最后一个元素
			while current.get_next() is not None:
				current = current.get_next() 
			current.set_next(Node(item))

	def insert(self, pos, item):
		"""插入操作，链表首都append需要分类讨论"""
		if pos == 0:
			inserted_node = Node(item)
			inserted_node.set_next(self.head)
			self.head = inserted_node
		elif 0 < pos <=self.size() :
			#找到pos位置对应的当前元素current与前置元素previous
			current = self.head
			previous = None
			count = 0
			while count < pos:
				previous = current
				current = current.get_next()
				count += 1
			inserted_node = Node(item)
			inserted_node.set_next(current)
			previous.set_next(inserted_node)

	def index(self, item):
		myindex = 0
		current = self.head
		if self.size():
			#非空执行操作，空list不做任何操作
			count = 0
			while current.get_data() != item:
				count += 1
				current = current.get_next()
			return count

	def pop(self, pos=None):
		"""pop操作，链表首都pop需要分类讨论"""
		#对于缺省值的处理
		if pos is None:
			pos = self.size() - 1 
		if pos == 0:
			self.head = self.head.get_next()
			return self.head
		elif 0 < pos < self.size():
			current = self.head
			previous = None
			count = 0
			while count != pos:
				previous = current
				current = current.get_next()
				count += 1
			previous.set_next(current.get_next())
			return current



if __name__ == '__main__':
	mylist = UnOrderedList()

	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)

	print(mylist.size())
	print(mylist.search(93))
	print(mylist.search(100))
	mylist.add(100)
	print(mylist.search(100))
	print(mylist.size())
	print('*'*50)
	mylist.remove(54)
	print(mylist.size())
	mylist.remove(93)
	print(mylist.size())
	mylist.remove(31)
	print(mylist.size())
	mylist.remove(11)
	print(mylist.size())
	print(mylist.search(93))

	print(mylist.append(66))
	print(mylist.size())
	print(mylist.pop(0))
	print(mylist.pop())
	print(mylist.index(17))
	print(mylist.insert(0, 333))
	print(mylist.insert(1, 444))
	print(mylist.index(333))
	print(mylist.index(444))