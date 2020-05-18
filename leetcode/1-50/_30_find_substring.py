class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if s == "" or words == []:
            return result

        words_length =len(words) * len(words[0])
        for index in range(len(s)-words_length+1):
            flag = self.match_substring(index, s, words.copy()) # 注意传入的是words的复制，否则words会越来越小
            if flag:
                result.append(index)

        return result

    def match_substring(self, index, s, words):
        if words == []:
            return True

        word_length = len(words[0])
        s_word = s[index: index+word_length]
        if s_word in words:
            words.remove(s_word)
            return self.match_substring(index+word_length, s, words)  # 这里需要加return
        else:
            return False

if __name__ == '__main__':
    s = ""
    words = []
    result = Solution().findSubstring(s, words)
    print(result)