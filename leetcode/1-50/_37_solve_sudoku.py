class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        start = self.get_start(board)   # 获得第一个"."位置
        next = self.get_next(board) # 下一个"."位置，是一个位置关系字典

        self.solve(board, loc=start, next=next) # 回溯法


    def solve(self, board, loc, next):
        for num in range(1, 10):
            board[loc[0]][loc[1]] = str(num)
            if self.is_valid(board, loc):   # 检查num填入loc是否有效
                if loc in next.keys():      # 有效的情况下，loc在next.keys()中，填充下一位置。
                    next_loc = next[loc]
                    if self.solve(board, next_loc, next):
                        return board
                    else:
                        board[next_loc[0]][next_loc[1]] = "."   # 这步很重要，下一位置所有数字均无效，则重置为"."，返回上级
                else:   # 有效的情况下，loc不在next.keys()中，说明loc是最后一个"."位置，数独完成。
                    return True
        return False


    def is_valid(self, board, loc):
        row_num_dict = {}
        for row_num in board[loc[0]]:
            if row_num != ".":
                if row_num in row_num_dict:
                    return False
                else:
                    row_num_dict[row_num] = True

        column_num_dict = {}
        for column_num in [board[j][loc[1]] for j in range(9)]:
            if column_num != ".":
                if column_num in column_num_dict:
                    return False
                else:
                    column_num_dict[column_num] = True

        sub_board_num_dict = {}
        sub_board_i = loc[0] // 3
        sub_board_j = loc[1] // 3
        for sub_board_num in [board[sub_board_i * 3 + n][sub_board_j * 3 + m] for n in range(3) for m in range(3)]:
            if sub_board_num != ".":
                if sub_board_num in sub_board_num_dict:
                    return False
                else:
                    sub_board_num_dict[sub_board_num] = True
        return True

    def get_start(self, board):
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    return (row, column)

    def get_next(self, board):
        next = {}
        pre_loc = ""
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    cur_loc = (row, column)
                    if pre_loc:
                        next[pre_loc] = cur_loc
                    pre_loc = cur_loc
        return next

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
    Solution().solveSudoku(board)
    print(board)