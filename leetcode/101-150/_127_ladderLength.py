class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        charSet = set("abcdefghijklmnopqrstuvwxyz")

        def get_next(target_word, used_words):
            # 得到所有可能的下一个单词，要求如下：
            # 1. 与target_word的编辑距离为1
            # 2. 在wordSet中，且不再在uesd_words中
            next_words = []
            for i in range(len(target_word)):
                tmp_char_set = charSet.copy()
                tmp_char_set.remove(target_word[i])
                for c in tmp_char_set:
                    candidate = target_word[:i] + c + target_word[i + 1:]
                    if candidate in wordSet and candidate not in used_words:
                        next_words.append(candidate)
            return next_words

        forward = {beginWord}
        backword = {endWord}

        used_words = set()
        len_ = 2

        while forward:
            if len(forward) > len(backword):
                # 优先遍历较短的BFS
                forward, backword = backword, forward

            tmp = set()  # 用于更新forward
            used_words.update(forward)

            for end_word in forward:
                next_words = get_next(end_word, used_words)

                for next_word in next_words:
                    if next_word in backword:
                        return len_
                tmp.update(set(next_words))

            len_ += 1
            forward = tmp

        return 0


if __name__ == '__main__':
    beginWord = "dog"
    endWord = "hot"
    wordList = ["dog", "hot"]

    res = Solution().ladderLength(beginWord, endWord, wordList)
    print(res)
