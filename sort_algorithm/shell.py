def shell_sort(list):
    # 这是一种改进的插入排序方法
    lenth = len(list)
    gap = len(list)

    while gap > 1:
        # 最后一次循环的gap为1
        gap = int(gap / 3) + 1
        # 下面是以gap为间隔的插入排序， 也可以使用交换法
        for i in range(gap, lenth):
            pre_index = i - gap
            current = list[i]
            while pre_index >= 0 and list[pre_index] > current:
                list[pre_index + gap] = list[pre_index]
                pre_index -= gap
            list[pre_index + gap] = current

    return list