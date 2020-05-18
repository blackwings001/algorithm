class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        res = [0, 1]

        for i in range(1, n):
            length = len(res) # 当前列表的长度
            for j in range(length):
                res.append(length + res[length - j - 1])

        return res




if __name__ == '__main__':
    n = 3
    res = Solution().grayCode(n)
    print(res)