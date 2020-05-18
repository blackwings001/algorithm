class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 生成矩阵是一个双层循环
        if n == 1:
            return [[1]]

        res = [[0 for _ in range(n)] for _ in range(n)]
        value = 1
        
        for i in range((n + 1) // 2): # 外圈大循环
            start = i
            end = n - i - 1

            if start == end: # 矩阵中心是一个值的情况
                res[start][end] = value
            
            # 依次完成四条边
            for col in range(start, end):
                row = start
                res[row][col] = value
                value += 1
            
            for row in range(start, end):
                col = end
                res[row][col] = value
                value += 1
                
            for col in range(end, start, -1):
                row = end
                res[row][col] = value
                value += 1
            
            for row in range(end, start, -1):
                col = start
                res[row][col] = value
                value += 1

        return res


if __name__ == '__main__':
    n = 10
    res = Solution().generateMatrix(n)
    print(res)