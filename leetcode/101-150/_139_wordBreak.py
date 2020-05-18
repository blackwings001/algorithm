class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False

        word_set = set(wordDict)
        max_lenth = max([len(word) for word in word_set])

        fail_point = set()

        def word_break(s):
            if not s:
                return True

            for i in range(max_lenth + 1):
                if s[:i] in word_set:
                    if i not in fail_point:
                        if word_break(s[i:]):
                            return True
                        fail_point.add(i)
            return False

        return word_break(s)


if __name__ == '__main__':
    s = "applepen"
    wordDict = ["apple", "pen"]

    res = Solution().wordBreak(s, wordDict)
    print(res)
