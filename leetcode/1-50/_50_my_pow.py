class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 递归基
        if n == 1:
            return x
        if n == 0:
            return 1

        flag = 1 if n > 0 else -1   # 判断n的正负
        n = abs(n)
        result = x
        i = 1

        while 2 * i <= n:
            result *= result
            i *= 2

        if i < n:   # 退出循环时，如果i小于n，进行递归
            result = result * self.myPow(x, n - i)

        return result if flag == 1 else 1 / result

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        e = abs(n)
        tmp = x
        res = 1
        while e != 0:
            if e % 2 == 1:
                res *= tmp
            tmp *= tmp
            e = e // 2
        return float(res) if n > 0 else 1.0 / res

if __name__ == '__main__':
    x = 3
    n = 27
    result = Solution().myPow1(x, n)
    print(result)