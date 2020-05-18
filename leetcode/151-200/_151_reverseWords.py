class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s = " ".join([s[i] for i in range(len(s) - 1, -1, -1) if s[i]])
        return s


if __name__ == '__main__':
    s = "hello  world@ "
    res = Solution().reverseWords(s)
    print(res)
