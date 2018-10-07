from random import randint,choice
from timeit import Timer
from timeit import timeit

class Student():
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __lt__(self,other):
		#小于的定义：年龄相同时还要比较首字母大小；年龄不同时以年龄为准
		return self.name < other.name if self.age == other.age else self.age < other.age

	def __eq__(self,other):
		return self.age == other.age

def selectionsort1(myarr):
	for i in range(len(myarr)):
		#求子数组[i,n)中的最小值对应的index
		min_index = i
		for j in range(i,len(myarr)):
			if myarr[j] < myarr[min_index]:
				min_index = j
		#交换list[i]与list[min_index]
		myarr[i], myarr[min_index] = myarr[min_index],myarr[i]
	
	return myarr

if __name__ == "__main__":
	array = [randint(0, 1000) for i in range(0,1000)]
	timer = Timer('selectionsort1(array)','from __main__ import selectionsort1,array')
	print(timer.timeit(number=1))
	print('*'*50)
	name_bank = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	array = [Student(choice(name_bank),randint(1,100)) for _ in range(1000)]
	timer = Timer('selectionsort1(array)','from __main__ import selectionsort1,array')
	print(timer.timeit(number=1))
