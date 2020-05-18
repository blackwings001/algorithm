class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 边界情况
        if m == 1 and n == 1:
            return 1

        # 注意初始化矩阵的时候，行和列不要搞反了，先初始化行，一行有一列元素
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]




if __name__ == '__main__':
    m = 3
    n = 7

    res = Solution().uniquePaths(m, n)
    print(res)