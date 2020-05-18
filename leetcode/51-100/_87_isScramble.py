class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        # 提前终止循环
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):  # 从1开始，否则会出现死循环
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False

if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    res = Solution().isScramble(s1, s2)
    print(res)