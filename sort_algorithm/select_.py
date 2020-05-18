def select_sort(list):
    for i in range(len(list) - 1): # i终止于倒数第二个元素
        min_index = i
        for j in range(i+1, len(list)): # j起始于i+1，终止于最后一个元素
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
    return list
