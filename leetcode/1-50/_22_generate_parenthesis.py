class Solution:
    def generateParenthesis(self, n):
        result = []
        ans = ""
        l = 0
        r = 0
        self.parenthesis(n, l, r, ans, result)
        return result

    def parenthesis(self, n, l, r, ans, result):
        """
        :param n: 一共几对括号
        :param l: ans中左括号的数量
        :param r: ans中右括号的数量
        :param ans: 当前的括号组合
        :param result: 符合条件的括号组合
        :return:
        """
        if l == n and r == n:
            result.append(ans)
            return
        else:
            # 有两种情况可以添加括号，一种是l<n时，添加左括号，另一种是r<l时，添加右括号
            if l < n:
                self.parenthesis(n, l+1, r, ans+"(", result)
            if r < l:
                self.parenthesis(n, l, r+1, ans+")", result)








if __name__ == '__main__':
    n = 4
    result = Solution().generateParenthesis(n)
    print(result)