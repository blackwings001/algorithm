class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        import sys
        days = len(prices)
        nums = 3

        # 初始化一个三维矩阵, 行为天数（第0天到len(prices)天），列为交易次数（0， 1， 2），高为是否持有股票（0没有股票，1有股票）
        matrix = [[[-sys.maxsize for _ in {0, 1}] for _ in range(nums)] for _ in range(days + 1)]
        # 填写边界情况
        matrix[0][0][0] = 0

        for i in range(1, days + 1):
            for j in range(nums):
                if j == 0:
                    matrix[i][j][0] = 0
                else:
                    matrix[i][j][0] = max(matrix[i - 1][j][0], matrix[i - 1][j][1] + prices[i - 1])
                    matrix[i][j][1] = max(matrix[i - 1][j][1], matrix[i - 1][j - 1][0] - prices[i - 1])

        # for i in range(1, days + 1):
        #     for j in range(nums):
        #         print(matrix[i][j][1])

        # 最后一天，没有股票的收益最高, 可能交易了1次或者2次
        profit = max([matrix[days][i][0] for i in range(nums)])
        return profit

    def maxProfitStatus(self, prices):
        if len(prices) <= 1:
            return 0

        import sys
        s1 = -prices[0]  # 第一次买入
        s2 = -sys.maxsize   # 第一次卖出
        s3 = -sys.maxsize   # 第二次买入
        s4 = -sys.maxsize   # 第二次卖出

        for i in range(1, len(prices)):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])

        return max(0, s4)


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    res = Solution().maxProfitStatus(prices)
    print(res)
