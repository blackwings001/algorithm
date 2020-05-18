class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 先放入")"和0，避免边界情况
        s_stack = [")"]
        n_stack = [0]

        for parentheses in s:
            if parentheses == ")" and s_stack[-1] == "(": # 只有这种情况会特殊处理
                s_stack.pop()
                # valid_num记录的是此位置后面有多长的有效括号，当此位置也是有效括号的一部分时，将valid_num + 2 加到前一位置。
                valid_num = n_stack.pop()
                n_stack[-1] += valid_num + 2
            else:
                s_stack.append(parentheses)
                n_stack.append(0)

        return max(n_stack)

if __name__ == '__main__':
    s = ""
    result = Solution().longestValidParentheses(s)
    print(result)