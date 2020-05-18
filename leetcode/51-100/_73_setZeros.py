class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for m in range(row):
                        matrix[m][j] = "x" if matrix[m][j] != 0 else 0
                    for n in range(col):
                        matrix[i][n] = "x" if matrix[i][n] != 0 else 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [
  [0]
]
    Solution().setZeroes(matrix)

    print(matrix)

