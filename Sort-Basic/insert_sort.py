from sort_helper import test_sort,random_array

def insert_sort1(array):
	for i in range(len(array)):
		#当前位置i代表可以向左交换位置的次数
		j = i
		while j:
			if array[j]<array[j-1]:
				array[j],array[j-1] = array[j-1],array[j]
				j -= 1
			else:
				break

#技巧性比较强，且range用来遍历比较好，循环的话有固有缺陷，无后缀+/后缀-
def insert_sort2(array):
	#第0个元素选取后就排好序了，所以直接从1开始计数
	for i in range(1,len(array)):
		#注意交换位置时，j最小为1，使用下面的逆序非常合适
		for j in range(i,0,-1):
			if array[j] < array[j-1]:
				array[j],array[j-1] = array[j-1],array[j]

#改进版插入排序
def insert_sort3(array):
	for i in range(len(array)):
		#当前位置i代表可以向左交换位置的次数
		j = i
		temp = array[i]
		while j:
			if temp < array[j-1]:
				array[j] = array[j-1]
				j -= 1
			else:
				break
		array[j] = temp

def insert_sort(array, l, r):
	"""对数组的[l,r]范围进行插入排序"""
	#外层遍历[l+1,r+1)
	i = l+1
	while i < r+1:
		#内层遍历【i,l）
		j = i
		temp = array[i]
		while j > l:
			if temp < array[j-1]:
				array[j] = array[j-1]
				j = j-1
			else:
				break
		array[j] = temp
			
		i += 1


if __name__ == '__main__':
	array1 = random_array(10000, 1, 10000)
	array2 = array1[:]
	array3 = array1[:]
	test_sort('insert_sort1', insert_sort1, array1)
	test_sort('insert_sort2', insert_sort2, array2)
	test_sort('insert_sort3', insert_sort3, array3)
