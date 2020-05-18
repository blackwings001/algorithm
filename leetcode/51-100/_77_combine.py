class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return [[]]

        res = []
        for i in range(1, n + 1):
            self.combine_(n, k, [i], res)

        return res

    def combine_(self, n, k, cur, res):
        if len(cur) == k:
            res.append(cur)
            return

        if cur[-1] == n:
            return

        for i in range(cur[-1] + 1, n + 1):
            # 注意这里传入的是cur + [1]一个新的列表， 不改变cur的值
            self.combine_(n, k, cur + [i], res)

if __name__ == '__main__':
    n = 10
    k = 2

    res = Solution().combine(n, k)
    print(res)