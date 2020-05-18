class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1 and k == 1:
            return "1"

        res = ""
        digits = [i for i in range(1, n + 1)]

        n_factorial = 1
        for i in range(1, n + 1):
            n_factorial *= i

        while len(digits) > 0:
            digit, k, digits, n_factorial= self.getNum(k, digits, n_factorial)
            res += str(digit)

        return res

    def getNum(self, k, digits, n_factorial):
        n_factorial /= len(digits)
        position = int((k-1) // n_factorial)
        digit = digits[position]
        digits.pop(position)
        k -= n_factorial * position
        return digit, k, digits, n_factorial

if __name__ == '__main__':
    n = 8
    k = 321
    res = Solution().getPermutation(n, k)
    print(res)