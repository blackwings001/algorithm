class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        max_length = 0
        char_index = {}

        while j < len(s):
            # 只有在以下条件满足时会移动i，注意条件顺序不要更改
            if j != i and s[j] in char_index and char_index[s[j]] >= i:
                i = char_index[s[j]] + 1
            # 储存/更新s[j]
            char_index[s[j]] = j
            # 计算i，j子字符串的长度
            cur_length = j - i + 1
            if cur_length > max_length:
                max_length = cur_length
            # j += 1
            j += 1
        return max_length

if __name__ == '__main__':
    solution = Solution()
    s = "pwwkewdsafafasdfghjkl"
    result = solution.lengthOfLongestSubstring(s)
    print(result)