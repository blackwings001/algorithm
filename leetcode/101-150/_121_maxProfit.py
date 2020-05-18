class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        x = prices[0]  # 买入价格
        y = 0  # 最大利润

        for i in prices:
            if i > x:
                y = max(y, i - x)
            elif i == x:
                continue
            elif i < x:
                x = i

        return y


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    res = Solution().maxProfit(prices)
    print(res)