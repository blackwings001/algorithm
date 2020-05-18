class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1 or k <= 0:
            return 0

        days = len(prices)
        max_profit = 0

        # 当k过大时，使用贪婪算法得到结果
        if k > days // 2:
            for d in range(days - 1):
                if prices[d + 1] > prices[d]:
                    max_profit += prices[d + 1] - prices[d]
            return max_profit

        # 初始化有股票和无股票的动态规划列表，每个位置的含义是第i天第k次交易有无股票时的最大利润，定义出售股票为一次交易
        no_stock = [0 for _ in range(days)]
        own_stock = [-prices[0]]
        for d in range(1, days):
            own_stock.append(max(own_stock[-1], -prices[d]))

        # 依次填写每次交易时的有无股票的动态规划表
        for i in range(k):
            for d in range(i + 1, days):
                no_stock[d] = max(own_stock[d - 1] + prices[d], no_stock[d - 1])
            for d in range(i + 2, days):
                own_stock[d] = max(no_stock[d - 1] - prices[d], own_stock[d - 1])
            max_profit = max(max_profit, no_stock[-1])

        return max_profit


if __name__ == '__main__':
    k = 2
    prices = [0,8,5,7,4,7]
    res = Solution().maxProfit(k, prices)
    print(res)

