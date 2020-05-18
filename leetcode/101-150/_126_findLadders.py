class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

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

        forward = {beginWord: [[beginWord]]}
        backword = {endWord: [[endWord]]}

        used_words = set()
        res = []

        while forward:
            if len(forward) > len(backword):
                # 优先遍历较短的BFS
                forward, backword = backword, forward

            tmp = {}  # 用于更新forward
            used_words.update(forward.keys())

            for end_word, path in forward.items():
                next_words = get_next(end_word, used_words)

                for next_word in next_words:
                    if next_word in backword:
                        # 前向后向BFS对接
                        if path[0][0] == beginWord:
                            res.extend([f_p + [b_p[i] for i in range(len(b_p) - 1, -1, -1)] for f_p in path for b_p in backword[next_word]])
                        elif path[0][0] == endWord:
                            res.extend([f_p + [b_p[i] for i in range(len(b_p) - 1, -1, -1)] for b_p in path for f_p in backword[next_word]])

                    tmp[next_word] = tmp.get(next_word, []) + [p + [next_word] for p in path]

            if res:
                return res

            forward = tmp


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    res = Solution().findLadders(beginWord, endWord, wordList)
    print(res)
