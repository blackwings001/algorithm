def build_max_heap(list, heap_length):
    for i in range(int(heap_length/2), -1 , -1):
        heapify(list, i, heap_length)

def heapify(list, i, heap_length):
    left = 2 * i + 1
    right = 2 * i + 2
    largest_index = i
    if left < heap_length and list[left] > list[i]:
        largest_index = left
    if right < heap_length and list[right] > list[largest_index]:
        largest_index = right

    if largest_index != i:
        list[i], list[largest_index] = list[largest_index], list[i]
        heapify(list, largest_index, heap_length)

def heap_sort(list):
    heap_lenth = len(list)
    # 1.构建大顶堆
    build_max_heap(list, heap_lenth)
    # 2.每次堆顶和堆尾(heap_lenth-1)交换，heap_length减一，调用heapify(list, 0, heap_length)
    while heap_lenth > 1:
        list[0], list[heap_lenth-1] = list[heap_lenth-1], list[0]
        heap_lenth -= 1
        heapify(list, 0, heap_lenth)
    return list
