def bubble_sort(list):
    # i只需要终止于倒数第二个元素即可, j第一次终止于倒数第二个元素，第二次终止于倒数第三个元素
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list