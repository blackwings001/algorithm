class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return None

        chars = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        remainder_char = {i: chars[i] for i in range(26)}

        res = ""
        while n:
            quotient = n // 26
            remainder = n % 26
            # 余数0对应的字符为Z，此时商应该减一
            if remainder == 0:
                quotient -= 1

            res = remainder_char[remainder] + res
            n = quotient

        return res


if __name__ == '__main__':
    print(Solution().convertToTitle(1))
    print(Solution().convertToTitle(10))
    print(Solution().convertToTitle(100))
    print(Solution().convertToTitle(26))
