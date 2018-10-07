from random import randint
import sys
import os
sys.path.append(os.path.abspath(os.path.pardir))
from decorator.decorator import decorator

#解法1：需要多消耗n个元素的空间
def search_min(array):
    """查找列表中的最小数"""
    min_index = 0
    min_num = array[0]
    for i in range(len(array)):
        if array[i] < min_num:
            min_index = i
            min_num = array[i]
    array.pop(min_index)
    return min_num
@decorator
def selection_sort(array):
    """选择排序"""
    #缺点：需要多开辟一块n个元素的空间
    ordered_array = []
    for i in range(len(array)):
        min_num = search_min(array)
        ordered_array.append(min_num)
    return ordered_array

if __name__ == "__main__":
    array = [randint(0, 10000) for i in range(0,10000)]
    ordered_array = selection_sort(array)




