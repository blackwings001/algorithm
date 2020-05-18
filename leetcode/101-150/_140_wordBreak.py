class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict or not s:
            return []

        word_set = set(wordDict)
        lookup = {}  # 记录每个位置的字符串组成情况，key为该位置到字符串末尾的长度

        def word_break(s):
            if not s:
                lookup[0] = [""]
                return [""]

            cur = []
            for i in range(len(s) + 1):
                if s[:i] in word_set:
                    sub_len = len(s) - i
                    if sub_len not in lookup:
                        word_break(s[i:])
                    if lookup[sub_len]:
                        cur.extend([(s[:i] + " " + sub_str).strip() for sub_str in lookup[sub_len]])

            lookup[len(s)] = cur
            return cur

        return word_break(s)


if __name__ == '__main__':
    s = "applepen"
    wordDict = ["apple", "pen", "app", "le"]

    res = Solution().wordBreak(s, wordDict)
    print(res)
