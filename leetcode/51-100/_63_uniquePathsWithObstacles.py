class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 边界情况
        if obstacleGrid[0][0] == 1:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        # 注意初始化矩阵的时候，行和列不要搞反了，先初始化行，一行有一列元素
        matrix = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                elif i == 0 and j == 0:
                    matrix[i][j] = 1
                elif i == 0:
                    matrix[i][j] = matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[row - 1][col - 1]

if __name__ == '__main__':
    ob = [[0,0,0],[0,1,0],[0,0,0]]
    res = Solution().uniquePathsWithObstacles(ob)
    print(res)