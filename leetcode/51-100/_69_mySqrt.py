class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        if x == 1:
            return 1

        res = self.binarySearch(0, x, x)
        return res

    def binarySearch(self, left, right, x):
        if right - left == 1:
            return left
        mid = (left + right) // 2
        mid_square = mid * mid
        if mid_square == x:
            return mid
        elif mid_square > x:
            return self.binarySearch(left, mid, x)
        else:
            return self.binarySearch(mid, right, x)



if __name__ == '__main__':
    n = 5
    res = Solution().mySqrt(n)
    print(res)