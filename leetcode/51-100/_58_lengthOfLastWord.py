class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 去掉末尾的空格
        while s and s[-1] == " ":
            s = s[:-1]

        if not s:
            return 0

        # 找到最后一个空格
        for j in range(len(s) - 1, -1, -1):
            if s[j] == " ":
                return len(s) - 1 - j

        return len(s)

if __name__ == '__main__':
    s = ""
    print(Solution().lengthOfLastWord(s))