from selectionsort1 import selectionsort1
from insert_sort import insert_sort2,insert_sort3
from sort_helper import test_sort,random_array,nearly_ordered_array

if __name__ == '__main__':
	array = nearly_ordered_array(10000, 10000)
	array1 = array[:]
	array2 = array[:]
	test_sort('selectionsort', selectionsort1, array)
	test_sort('insertsort', insert_sort2, array1)
	test_sort('advanced insertsort', insert_sort3, array2)