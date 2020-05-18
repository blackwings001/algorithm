from partition import partition_sort
from merge import merge_sort
from bubble import bubble_sort
from select_ import select_sort
from insert import insert_sort
from shell import shell_sort
from heap import heap_sort

def get_list():
    list1 = []
    list2 = [2]
    list3 = [3, 1, 5, 2, 2, 4]
    return list1, list2, list3

if __name__ == '__main__':
    # 快速排序
    list1, list2, list3 = get_list()
    partition_sorted_list1 = partition_sort(list1)
    partition_sorted_list2 = partition_sort(list2)
    partition_sorted_list3 = partition_sort(list3)
    print("partition_sorted_list1: " + str(partition_sorted_list1))
    print("partition_sorted_list2: " + str(partition_sorted_list2))
    print("partition_sorted_list3: " + str(partition_sorted_list3))

    # 归并排序
    list1, list2, list3 = get_list()
    merge_sorted_list1 = merge_sort(list1)
    merge_sorted_list2 = merge_sort(list2)
    merge_sorted_list3 = merge_sort(list3)
    print("merge_sorted_list1: " + str(merge_sorted_list1))
    print("merge_sorted_list2: " + str(merge_sorted_list2))
    print("merge_sorted_list3: " + str(merge_sorted_list3))

    # 冒泡排序
    list1, list2, list3 = get_list()
    bubble_sorted_list1 = bubble_sort(list1)
    bubble_sorted_list2 = bubble_sort(list2)
    bubble_sorted_list3 = bubble_sort(list3)
    print("bubble_sorted_list1: " + str(bubble_sorted_list1))
    print("bubble_sorted_list2: " + str(bubble_sorted_list2))
    print("bubble_sorted_list3: " + str(bubble_sorted_list3))

    # 选择排序
    list1, list2, list3 = get_list()
    select_sorted_list1 = select_sort(list1)
    select_sorted_list2 = select_sort(list2)
    select_sorted_list3 = select_sort(list3)
    print("select_sorted_list1: " + str(select_sorted_list1))
    print("select_sorted_list2: " + str(select_sorted_list2))
    print("select_sorted_list3: " + str(select_sorted_list3))

    # 插入排序
    list1, list2, list3 = get_list()
    insert_sorted_list1 = insert_sort(list1)
    insert_sorted_list2 = insert_sort(list2)
    insert_sorted_list3 = insert_sort(list3)
    print("insert_sorted_list1: " + str(insert_sorted_list1))
    print("insert_sorted_list2: " + str(insert_sorted_list2))
    print("insert_sorted_list3: " + str(insert_sorted_list3))

    # 希尔排序
    list1, list2, list3 = get_list()
    shell_sorted_list1 = shell_sort(list1)
    shell_sorted_list2 = shell_sort(list2)
    shell_sorted_list3 = shell_sort(list3)
    print("shell_sorted_list1: " + str(shell_sorted_list1))
    print("shell_sorted_list2: " + str(shell_sorted_list2))
    print("shell_sorted_list3: " + str(shell_sorted_list3))

    # 堆排序
    list1, list2, list3 = get_list()
    heap_sorted_list1 = heap_sort(list1)
    heap_sorted_list2 = heap_sort(list2)
    heap_sorted_list3 = heap_sort(list3)
    print("heap_sorted_list1: " + str(heap_sorted_list1))
    print("heap_sorted_list2: " + str(heap_sorted_list2))
    print("heap_sorted_list3: " + str(heap_sorted_list3))


