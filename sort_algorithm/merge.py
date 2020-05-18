def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = int(len(list)/2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    list = merge(left, right)
    return list

def merge(left, right):
    list = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # i和j都不越界的情况下进行比较
        if left[i] <= right[j]:
            list.append(left[i])
            i += 1
        elif left[i] > right[j]:
            list.append(right[j])
            j += 1

    list.extend(left[i:])
    list.extend(right[j:])

    return list