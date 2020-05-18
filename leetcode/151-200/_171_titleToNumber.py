class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char_digit = {chars[i]: i + 1 for i in range(26)}

        res = 0
        length = len(s)
        for i in range(length):
            res += char_digit[s[i]] * (26 ** (length - i - 1))

        return res


if __name__ == '__main__':
    print(Solution().titleToNumber("A"))
    print(Solution().titleToNumber("AB"))
    print(Solution().titleToNumber("Z"))
