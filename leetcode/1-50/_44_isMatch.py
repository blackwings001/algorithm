class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # 先处理边界情况, s或者p为空的情况
        if s == "":
            if p == "" or p == "*":
                return True
            return False

        if p == "":
            if s != "":
                return False

        s_l = len(s)
        p_l = len(p)
        matrix = [[0 for _ in range(s_l + 1)] for _ in range(p_l + 1)]   # 构建[p_l + 1, s_l + 1]的一个矩阵
        matrix[0][0] = 1    # 含义是p和s的头部空字符是匹配的

        # 从第二行开始，从左向右，从上到下依次填写matrix
        for i in range(1, p_l + 1):
            for j in range(0, s_l + 1):
                p_char = p[i-1]
                # 分别处理p_char为?, *, "a-z"的情况
                if p_char == "?":
                    if j > 0 and matrix[i-1][j-1] == 1:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
                elif p_char == "*":
                    if matrix[i-1][j] == 1 or (j > 0 and (matrix[i-1][j-1] == 1 or matrix[i][j-1] == 1)):
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
                else:
                    if j > 0 and matrix[i-1][j-1] == 1 and p[i-1] == s[j-1]:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0

        return bool(matrix[p_l][s_l])

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        i, j = 0, 0 # 两个指针分别扫描s，p
        star, i_index =  -1, 0  # 记录最新的"*"出现在位置，以及对应的s的位置

        # 先遍历完s
        while i < s_len:
            if j < p_len and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star = j
                j += 1
                i_index = i
            # j==p_len或者 p[j]!=s[i], 需要返回到最新的一个"*"位置继续匹配
            elif star != -1:
                j = star + 1
                i_index += 1
                i = i_index
            else:
                return False

        # 如果p[j]后面存在非"*"字符，结果为False
        while j < p_len and p[j] == '*':
            j += 1

        return j == p_len



if __name__ == '__main__':
    s = "abcdeb"
    p = "a*?b"
    result = Solution().isMatch(s, p)
    result2 = Solution().isMatch2(s, p)
    print(result)
    print(result2)



