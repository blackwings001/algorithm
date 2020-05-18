class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        in_ = prices[0]
        out_ = 0
        profit = 0

        for p in prices:
            if out_ == 0:
                # 找到卖出价
                if p < in_:
                    in_ = p
                elif p > in_:
                    out_ = p
                else:
                    continue
            else:
                if p > out_:
                    out_ = p
                elif p < out_:
                    profit += out_ - in_
                    in_ = p
                    out_ = 0
                else:
                    continue

        if out_ != 0:
            profit += out_ - in_

        return profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    res = Solution().maxProfit(prices)
    print(res)