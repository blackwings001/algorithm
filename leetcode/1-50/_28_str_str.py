class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):  #
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:  # haystack[i+j] != needle[j]结束内循环
                    break
                elif j == len(needle) - 1:      # haystack[i+j] == needle[j]并且j是needle的最后一位时，返回i
                    return i

        return -1

