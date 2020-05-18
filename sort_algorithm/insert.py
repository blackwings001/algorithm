def insert_sort(list):
    # 两种方式
    # 1.list[pre_index + 1]相当于空, 最后将current赋值于list[pre_index + 1]，这点和快速排序有点像
    # for i in range(len(list)):
    #     pre_index = i - 1
    #     current = list[i]
    #     while pre_index >= 0 and list[pre_index] > current:
    #         list[pre_index + 1] = list[pre_index]
    #         pre_index -= 1
    #     list[pre_index + 1] = current
    # 2.不断交换, 这种时间复杂度稍高一些
    for i in range(len(list)):
        while i > 0 and list[i-1] > list[i]:
            list[i], list[i-1] = list[i-1], list[i]
            i -= 1
    return list