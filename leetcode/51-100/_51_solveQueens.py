class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n == 0:
            return result
        matrix = ["." * n] * n
        row = 0
        self.arrangeQueens(result, row, matrix)
        return len(result)


    def arrangeQueens(self, result, row, matrix):
        n = len(matrix)
        for col in range(n):
            matrix[row] = "." * col + "Q" + "." * (n - col - 1)
            if self.is_valid(matrix, row, col):
                if row == n - 1:
                    # matrix会变化，保存matrix.copy()在result中
                    result.append(matrix.copy())
                else:
                    self.arrangeQueens(result, row+1, matrix)
            else:
                matrix[row] = "." * n


    def is_valid(self, matrix, row, col):
        # 首先，每行一定只有一个"Q",不需要检查
        # 检查之前的每一列
        for i in range(row):
            if matrix[i][col] == "Q":
                return False

        # 检查主对角线, 只需要检查上半部分即可，下半部分还没有填入元素
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if matrix[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 检查次对角线，也只需要检查上半部分
        i = row - 1
        j = col + 1
        while i >= 0 and j <= len(matrix) - 1:
            if matrix[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

if __name__ == '__main__':
    solution = Solution()
    result = solution.totalNQueens(4)
    print(result)





