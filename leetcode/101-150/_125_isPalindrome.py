class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        wrong_model = re.compile("[^a-z0-9]")
        s = s.lower().replace(" ", "")
        s = re.sub(wrong_model, "", s)

        for i in range(len(s)):
            j = len(s) - 1 - i
            if i <= j:
                if s[i] != s[j]:
                    return False
            else:
                return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s)
    print(res)