class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t:
            return 0

        n = len(s)
        m = len(t)
        matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    matrix[i][j] = 1
                elif j == 0:
                    matrix[i][j] = 0
                else:
                    if s[j - 1] == t[i - 1]:
                        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j-1]
                    else:
                        matrix[i][j] = matrix[i][j-1]

        # for row in matrix:
        #     print(row)

        return matrix[m][n]


if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    res = Solution().numDistinct(s, t)
    print(res)
