class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 分别验证行，列和方格是否符合数独条件
        for row in board:
            valid = self.is_valid(row)
            if valid == False:
                return False

        # 注意列的列表表达式
        for i in range(len(board)):
            column = [board[row][i] for row in range(9)]
            valid = self.is_valid(column)
            if valid == False:
                return False

        # 注意每个小方格的列表表达式
        for i in range(3):
            for j in range(3):
                sub_board = [board[3*i+n][3*j+m] for n in range(3) for m in range(3)]
                valid = self.is_valid(sub_board)
                if valid == False:
                    return False

        return True

    def is_valid(self, nums):
        num_times = {}
        for num in nums:
            if num != ".":
                if num in num_times:
                    return False
                else:
                    num_times[num] = 1
        return True

if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

    result = Solution().isValidSudoku(board)
    print(result)
