"""
KMP 算法
"""
def kmp(str, sub):
    next = get_next(sub)

    i = 0
    j = 0

    while i < len(str) and j < len(sub):
        if str[i] == sub[j] or j == -1:
            # j == -1 说明在str的i位置匹配失败
            i += 1
            j += 1
        else:
            j = next[j]

    if j < len(sub):
        return -1
    else:
        return i - len(sub)


def get_next(sub):
    next = dict()

    next[0] = -1
    next[1] = 0

    j = 1  # 后一段的最后匹配位置
    k = 0  # 前一段的最后匹配位置

    while j + 1 < len(sub):
        if sub[j] == sub[k] or k == -1:
            # k == -1标明j+1之前没有相等的前缀和后缀
            next[j + 1] = k + 1
            j += 1
            k += 1
        else:
            k = next[k]
    return next


if __name__ == '__main__':
    str = "ababacdabcdababc"
    sub = "ababc"
    start = kmp(str, sub)
    print(start)
