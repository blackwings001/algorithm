class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        zeros = 0
        factor = 5

        while factor <= n:
            zeros += n // factor
            factor *= 5

        return zeros


if __name__ == '__main__':
    n = 50
    print(Solution().trailingZeroes(n))
