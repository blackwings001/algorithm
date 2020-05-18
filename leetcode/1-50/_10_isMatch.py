import numpy as np

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "" and p == "":
            return True

        dynamic_matrix = np.zeros(shape=(len(s)+1, len(p)+1))
        dynamic_matrix[0][0] = 1

        # 填写矩阵的第0行
        for j in range(1, len(p)+1):
            if p[j-1] == "*" and dynamic_matrix[0][j-2] == 1:
                dynamic_matrix[0][j] = 1
            else:
                dynamic_matrix[0][j] = 0

        # 填写矩阵的第0列
        for i in range(1, len(s)+1):
            dynamic_matrix[i][0] = 0

        # 填写内部矩阵
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == "*":
                    # dynamic_matrix[i][j-2]是*将前一个字符重复0次，dynamic_matrix[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == ".")是*将前一个字符重复1至多次，
                    # 问题是.*可以匹配任何字符，属于题中的一个漏洞，解决办法是当dynamic_matrix[i][j-2]为0，dynamic_matrix[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == ".")为1时，让p[j-2]的值为s[i-1]
                    dynamic_matrix[i][j] = dynamic_matrix[i][j-2] or (dynamic_matrix[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
                else:
                    dynamic_matrix[i][j] = dynamic_matrix[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
        return True if dynamic_matrix[len(s)][len(p)] else False


if __name__ == '__main__':
    s = "misafklajfkljkwlnvz"
    p = "m.*"
    result = Solution().isMatch(s, p)
    print(result)


