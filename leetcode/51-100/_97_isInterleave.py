class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False

        # 进行动态规划
        matrix = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        matrix[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                length = i + j
                # 一共有两种情况，matrix[i][j]的值可以为True，
                if (i != 0 and s1[i - 1] == s3[length - 1] and matrix[i - 1][j] == True) or (j != 0 and s2[j - 1] == s3[length - 1] and matrix[i][j -  1] == True):
                    matrix[i][j] = True

        return matrix[n][m]

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    res = Solution().isInterleave(s1, s2, s3)
    print(res)