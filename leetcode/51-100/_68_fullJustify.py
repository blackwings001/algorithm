class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []

        if len(words) == 0:
            return res


        line = "" # 记录每一行元素
        for word in words:
            if line == "":
                line += word
            elif len(line) + len(word) + 1 <= maxWidth:
                line += " " + word
            else:
                line = self.reshape(line, maxWidth)
                res.append(line)
                line = word

        if line != "":
            res.append(line + " " * (maxWidth - len(line)))

        return res

    def reshape(self, line, maxWidth):
        # 重新排列line
        if len(line) == maxWidth:
            return line

        more_spaces = maxWidth - len(line)
        line_words = line.split()
        if len(line_words) == 1:
            return line + " " * (maxWidth - len(line))

        # 将多余的空格从左到右依次分配给单词之间的空格位置，可能存在循环
        spaces = [1 for _ in range(len(line_words) - 1)]
        for i in range(more_spaces):
            spaces[i % len(spaces)] += 1

        res = ""
        for i in range(len(line_words) - 1):
            res += line_words[i] + " " * spaces[i]
        res += line_words[-1]

        return res



if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16

    res = Solution().fullJustify(words, maxWidth)
    print(res)