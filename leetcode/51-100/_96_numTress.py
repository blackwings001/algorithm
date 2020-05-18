class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        res = 1
        for i in range(1, n):
            res = 2 * (2 * i + 1) / (i + 2) * res

        return int(res)

if __name__ == '__main__':
    n = 7
    res = Solution().numTrees(n)
    print(res)