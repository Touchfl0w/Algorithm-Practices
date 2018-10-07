from random import randint
from time import time

def random_array(n=10000, left=1, right=10000):
	return [randint(left,right) for _ in range(n)]

def nearly_ordered_array(n,switch_num):
	myarr = list(range(n))
	for _ in range(switch_num):
		a = randint(0, n-1)
		b = randint(0, n-1)
		myarr[a],myarr[b] = myarr[b],myarr[a]
	return myarr

def is_sorted(array):
	sorted = True
	for i in range(len(array)-1):
		if array[i] > array[i+1]:
			sorted = False
			break
	return sorted

def test_sort(sort_name, sort,array):
	temp_array = array[:]
	start = time()
	sort(array)
	spend = time() - start
	#不正确时会抛出异常
	try:
		assert(is_sorted(array))
	except AssertionError:
		print('the ordinary array is : ',temp_array)
		print('the result of array is : ',array)

	print(sort_name + ' : '+ str(spend) + ' seconds')
