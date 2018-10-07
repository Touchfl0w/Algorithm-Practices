from sort_helper import test_sort,random_array,nearly_ordered_array

def bubble_sort(array):
	"""冒泡排序的经典实现"""
	n = len(array)
	#子过程运行闭区间的右端点标记定义为i,范围[n-1,1],转换为适合while惯用区间为[n-1,0)
	i = n-1
	while i > 0:
		#子过程交换位置标记定义为j，范围为[0,i-1]，转换为适合while惯用区间为[0，i)
		#子过程运行区间为[0,i]
		j = 0
		while j < i:
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
			j += 1
		i -= 1
	return array

#性能改进
def bubble_sort1(array):
	"""冒泡排序的经典实现"""
	n = len(array)
	#子过程运行闭区间的右端点标记定义为i,范围[n-1,1],转换为适合while惯用区间为[n-1,0)
	i = n-1
	while i > 0:
		stop = True

		#子过程交换位置标记定义为j，范围为[0,i-1]，转换为适合while惯用区间为[0，i)
		#子过程运行区间为[0,i]
		j = 0
		while j < i:
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
				stop = False
			j += 1

		if stop:
			break
		i -= 1
	return array
#代码改进
def bubble_sort2(array):
	"""冒泡排序的经典实现"""
	n = len(array)
	stop = False
	#子过程运行闭区间的右端点标记定义为i,范围[n-1,1],转换为适合while惯用区间为[n-1,0)
	i = n-1
	while i > 0 and not stop:
		stop = True

		#子过程交换位置标记定义为j，范围为[0,i-1]，转换为适合while惯用区间为[0，i)
		#子过程运行区间为[0,i]
		j = 0
		while j < i:
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
				stop = False
			j += 1

		i -= 1
	return array

if __name__ == '__main__':
	array1 = random_array()
	array2 = array1[:]
	array3 = nearly_ordered_array(10000, 1)
	array4 = array3[:]
	array5 = random_array(10000,0,1)
	array6 = array3[:]
	test_sort('bubble_sort random_array', bubble_sort, array1)
	test_sort('bubble_sort1 random_array', bubble_sort1, array2)
	test_sort('bubble_sort nearly_ordered_array', bubble_sort, array3)
	test_sort('bubble_sort1 nearly_ordered_array', bubble_sort1, array4)
	print('大量重复元素')
	test_sort('bubble_sort ', bubble_sort, array5)
	test_sort('bubble_sort1 ', bubble_sort1, array6)
