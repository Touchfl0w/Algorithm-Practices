from stack import Stack
import timeit
from timeit import Timer

def reverse_list1(mylist):
	reversed(mylist)

def reverse_list2(mylist):
	s = Stack()
	result = []
	for i in mylist:
		s.push(i)
	for i in range(s.size()):
		mylist[i] = s.pop()

if __name__ == '__main__':
	a = list(range(10000))
	t1 = Timer('reverse_list1(a)', 'from __main__ import reverse_list1,a')
	print(t1.timeit(number=100))
	t2 = Timer('reverse_list2(a)', 'from __main__ import reverse_list2,a')
	print(t2.timeit(number=100))
