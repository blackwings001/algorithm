class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0 :
            return False

        col = len(matrix[0])
        if col == 0:
            return False

        i = 0
        j = col - 1
        while True:
            ele = matrix[i][j]
            if ele == target:
                return True
            elif ele < target:
                i += 1
                if i == row:
                    return False
            else:
                j -= 1
                if j == -1:
                    return False

if __name__ == '__main__':
    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    res = Solution().searchMatrix(matrix, 10)
    print(res)