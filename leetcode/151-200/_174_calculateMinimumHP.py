class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return None

        # 从下到上，从右到左依次填写每个位置需要的最小血量， 其中需要最小血量来自每个位置右边位置和下边位置，需要的最小血量至少为1
        import sys
        row = len(dungeon)
        col = len(dungeon[0])
        dp = [sys.maxsize for _ in range(col + 1)]
        dp[-2] = 1 if dungeon[row - 1][col - 1] >= 0 else -dungeon[row - 1][col - 1] + 1  # 终点所需要的血量

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if i == row - 1 and j == col - 1:
                    continue
                dp[j] = 1 if min(dp[j], dp[j + 1]) - dungeon[i][j] <= 0 else min(dp[j], dp[j + 1]) - dungeon[i][j]

        return dp[0]


if __name__ == '__main__':
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]
    res = Solution().calculateMinimumHP(dungeon)
    print(res)
