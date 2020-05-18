class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        return grid[row - 1][col - 1]



if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    res = Solution().minPathSum(grid)
    print(res)