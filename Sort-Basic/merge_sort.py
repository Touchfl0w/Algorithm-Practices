from sort_helper import test_sort,random_array,nearly_ordered_array
from insert_sort import insert_sort

def __merge(array, left, mid, right):
	print(array)
	temp = array[left:right+1]
	#新数组temp的左中右标记,充当常量
	n = len(temp)
	l = 0
	r = n-1
	m = l + (r -l) // 2
	#左数组标记i,右数组标记j,赋值外部循环标记k
	i = 0
	j = m + 1
	#遍历【0，n)即整个数组长度，每次确定一个下标应该赋值的元素并完成赋值操作
	k = 0 
	while k < n:
		#2、定义判断条件，防越界；循环的次数是由n确定的，不存在i,j同时越界的情况
		if i > m:
			array[k + left] = temp[j]
			j += 1
		elif j > r:
			array[k + left] = temp[i]
			i += 1
		#1、判断两个子数组当前位置的值，并赋值给原数组array的对应位置，此处可能涉及到越界问题,所以循环主体开始之前要判断一下
		elif temp[i] < temp[j]:
			array[k + left] = temp[i]
			i += 1
		else:
			array[k + left] = temp[j]
			j += 1

		k += 1
	print(array)

#错误示范
def __merge1(array, left, mid, right):
	#错误1，开辟数组空间只针对一部分元素，而非整个数组
	temp = array[:]
	#错误2，left应该最后赋值为0，否则后两部相当于减0，无作用
	#错误3：内部端点就应该重新定义为l、r、mid;一旦否则array[k+left]无效果，因为left已变..
	left = 0
	mid = mid - left
	right = right - left
	n = right - left + 1
	i = 0
	j = mid + 1
	k = 0 
	while k < n:
		if i > mid:
			array[k + left] = temp[j]
			j += 1
		elif j > right:
			array[k + left] = temp[i]
			i += 1
		elif temp[i] < temp[j]:
			array[k + left] = temp[i]
			i += 1
		else:
			array[k + left] = temp[j]
			j += 1

		k += 1
	print(array)


#该私有函数需要左右下标
def __merge_sort(array, left, right):
	#3、添加基准条件,左右区间短点，相差1即可，即子数组长度为1
	if right -left <= 0:
		return
	#1、一分为二
	mid = left + (right -left) // 2 
	#2、左右分别归并排序，应该考虑到要添加基准条件了，否则无限递归
	__merge_sort(array, left, mid)
	__merge_sort(array, mid+1, right)
	#4、此时，array两个子数组都已有序，但整个数组却还无序，需要合并
	__merge(array, left, mid, right)

def __merge_sort1(array, left, right):
	if right -left <= 0:
		return
	mid = left + (right -left) // 2 
	__merge_sort1(array, left, mid)
	__merge_sort1(array, mid+1, right)
	if array[mid] > array[mid+1]:
		__merge(array, left, mid, right)

def __merge_sort2(array, left, right):
	if right -left <= 50:
		insert_sort(array, left, right)
		#必须要有return，否则无限递归
		return
	mid = left + (right -left) // 2 
	__merge_sort2(array, left, mid)
	__merge_sort2(array, mid+1, right)
	if array[mid] > array[mid+1]:
		__merge(array, left, mid, right)

def merge_sort(array):
	#作为带外暴露的归并排序函数，不需要左右下标
	__merge_sort(array, 0, len(array)-1)

def merge_sort1(array):
	__merge_sort1(array, 0, len(array)-1)

def merge_sort2(array):
	__merge_sort2(array, 0, len(array)-1)

def merge_sort_BU(array):
	n = len(array)
	sz = 2
	while sz < n + 1:
		
		i = 0 
		while i < n:
			l1 = i
			r1 = i+2*sz-1
			if r1 > n -1:
				r1 = n-1
			m1 = l1 + (r1-l1) //2
			__merge(array, l1, m1, r1)
			i += 2*sz 

		sz *= 2

if __name__ == '__main__':
	# array = random_array()
	# array1 = array[:]
	# array2 = array[:]
	# array3 = nearly_ordered_array(10000, 1)
	# array4 = array3[:]
	# array5 = array3[:]
	# test_sort('merge_sort random_array', merge_sort, array)
	# test_sort('merge_sort1 random_array', merge_sort1, array1)
	# test_sort('merge_sort2 random_array', merge_sort2, array2)
	# test_sort('merge_sort nearly_ordered_array', merge_sort, array3)
	# test_sort('merge_sort1 nearly_ordered_array', merge_sort1, array4)
	# test_sort('merge_sort2 nearly_ordered_array', merge_sort2, array5)
	a = [4,3,56,2]
	merge_sort_BU(a)
	print(a)

