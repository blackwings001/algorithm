def partition_sort(list):
    if len(list) <= 1:
        return list
    low = 0
    high = len(list) - 1
    pivot = list[0]
    while low < high:
        while low < high and list[high] > pivot:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] <= pivot:
            low += 1
        list[high] = list[low]
    # 跳出循环后list[:low]和list[low+1:]已经根据轴点分为两部分list[low]的值不确定，可以赋值为pivot

    list = partition_sort(list[:low]) + [pivot] + partition_sort(list[low+1:])

    return list