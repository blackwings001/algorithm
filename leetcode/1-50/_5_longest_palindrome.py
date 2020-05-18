class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 处理特殊情况
        if s == "": return s

        longest_palindrome = ""

        for i in range(len(s)):
            one_char_longest_palindrome = self.get_char_longest_palindrome(i, i, s)
            if len(one_char_longest_palindrome) > len(longest_palindrome):
                longest_palindrome = one_char_longest_palindrome
            two_char_longest_palindrome = self.get_char_longest_palindrome(i, i+1, s)
            if len(two_char_longest_palindrome) > len(longest_palindrome):
                longest_palindrome = two_char_longest_palindrome

        return longest_palindrome


    def get_char_longest_palindrome(self, i, j, s):
        """
        找到以i, j中点为中心的最长回文子串
        以某个字符为中心，则i，j相同
        以某两个相邻字符为中心，则j=i+1
        :param i: 中心点左边的索引
        :param j: 中心点右边的索引. 3
        :param s: 字符串
        :return: 以i, j中点为中心的最长回文子串
        """
        char_longest_palindrome = ""
        imin = i
        imax = j
        while imin >=0 and imax < len(s):
            if s[imin] == s[imax]:
                char_longest_palindrome = s[imin:imax+1]
                imin -= 1
                imax += 1
            else:
                break
        return char_longest_palindrome

if __name__ == '__main__':
    s = "agfdaghalkiwnanasdffdsa"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)



