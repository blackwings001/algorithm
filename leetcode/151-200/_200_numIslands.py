class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        index = 0  # 记录第几座岛屿
        pos_grid = {}  # 记录每个位置属于哪个岛屿

        row = len(grid)
        col = len(grid[0])

        def find_gred(pos, index):
            if pos in pos_grid:
                return

            x = pos[0]
            y = pos[1]
            if x >= row or x <= -1 or y >= col or y <= -1:
                return

            if grid[x][y] == "1":
                pos_grid[pos] = index
                find_gred((x + 1, y), index)
                find_gred((x - 1, y), index)
                find_gred((x, y + 1), index)
                find_gred((x, y - 1), index)

        for i in range(row):
            for j in range(col):
                pos = (i, j)
                if grid[i][j] == "0" or pos in pos_grid:
                    continue
                index += 1
                find_gred(pos, index)

        return index


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    res = Solution().numIslands(grid)
    print(res)
