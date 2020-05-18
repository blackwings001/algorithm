"""
从m个数中，选取2个n维的数，两者距离最近
"""
class Solution:
    def min_distance(self, nums, dim):
        """
        :param nums: m长数组
        :param dim: 维度n
        :return: min_distance
        """
        import sys
        import numpy as np

        if len(nums) // 2 < dim:
            return sys.maxsize

        # 储存边的值
        distance = {}
        for i in range(len(nums) - 1):
            distance[i + 1] = (nums[i + 1] - nums[i]) ** 2

        # 矩阵的维度为(n + 1, len(nums)), 行表示维度，从0到n， 列表式边的选取，nums为[1, 3, 6, 8, 9]的情况下
        # 一共有4条边，1边表示选取1，3对，2边表示3，6对，...， 注意2边的选取与1边有关，1边选取时，无法选择2边
        # 所以我们要用两个动态规划矩阵，一个表示选择某边时的最小值，一个表示不选取某边时的最小值
        matrix = [[[sys.maxsize for _ in {0, 1}] for _ in range(len(nums))] for _ in range(dim + 1)]
        # 矩阵初始化使用最大值
        # matrix[i][j][0]表示在第i个维度不选取j边的最小值，matrix[i][j][1]表示在第i个维度选取j边的最小值

        # 依次填写矩阵，对于不合理的位置跳过，例如matrix[0][1][1], 选取了1边，维度不可能为0（至少是1）
        # 状态转移方程为
        for i in range(dim + 1):
            for j in range(len(nums)):
                if i == 0:
                    matrix[i][j][0] = 0
                elif j != 0:
                    matrix[i][j][0] = min(matrix[i][j - 1][0], matrix[i][j - 1][1])
                    matrix[i][j][1] = matrix[i - 1][j - 1][0] + distance[j]

        min_dis = min(matrix[dim][len(nums) - 1][0], matrix[dim][len(nums) - 1][1])

        return np.sqrt(min_dis)


if __name__ == '__main__':
    nums = [1, 3, 6, 8, 9]
    dim = 2

    #  从面的组合最小应该为(1, 8), (3, 9)
    res = Solution().min_distance(nums, dim)
    print(res)

