class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        row = len(board)
        col = len(board[0])

        row_range = set(range(row))
        col_range = set(range(col))

        def check(postion, res):
            cur_row = postion[0]
            cur_col = postion[1]

            if cur_row not in row_range or cur_col not in col_range:
                return

            if board[cur_row][cur_col] == "O" and postion not in res:
                res.add(postion)
                check((cur_row + 1, cur_col), res)
                check((cur_row - 1, cur_col), res)
                check((cur_row, cur_col + 1), res)
                check((cur_row, cur_col - 1), res)

        res = set()
        # 先扫描一遍边缘元素
        for i in range(row):
            for j in range(col):
                if (i in {0, row - 1} or j in {0, col - 1}) and board[i][j] == "O":
                    check((i, j), res)

        # 只保留res中的O元素，其余改写为X
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in res:
                    board[i][j] = "X"


if __name__ == '__main__':
    board = [
             ['X', 'X', 'O', 'X'],
             ['X', 'X', 'O', 'O'],
             ['X', 'O', 'X', 'X'],
             ['X', 'X', 'X', 'X']
             ]

    Solution().solve(board)
    for i in board:
        print(i)
