class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        min_cut = list(range(n))  # min_cut[i]表示s[:i + 1]位置最少需要切几次

        matrix = [[False] * n for _ in range(n)]
        # matrix[i][j], 表示s[i:j+1]是不是回文串, 由于matrix[i][j]的判断需要matrix[i + 1][j -1]也就是左下方的元素
        # 所以我们填写矩阵时，要从左到右，从上到下
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or matrix[i + 1][j - 1]):
                    matrix[i][j] = True
                    if i == 0:
                        min_cut[j] = 0
                    else:
                        min_cut[j] = min(min_cut[j], min_cut[i - 1] + 1)
        for i in matrix:
            print(i)
        print(min_cut)

        return min_cut[-1]


if __name__ == '__main__':
    s = "abcddcbe"
    res = Solution().minCut(s)
    print(res)


