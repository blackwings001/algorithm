class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        row = len(word1)
        col = len(word2)

        if row == 0:
            return col
        if col == 0:
            return row

        # 构建一个矩阵
        matrix = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        # 填写矩阵的上边和左边
        for i in range(row + 1):
            matrix[i][0] = i
        for j in range(col + 1):
            matrix[0][j] = j

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                # matrix[i-1][j] + 1对应删除word1， matrix[i][j-1] + 1对应插入word2， matrix[i-1][j-1] + 1对应着替换，如果字符相等则加0
                matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + (1 if word1[i - 1] != word2[j - 1] else 0))
        return matrix[row][col]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    res = Solution().minDistance(word1, word2)
    print(res)