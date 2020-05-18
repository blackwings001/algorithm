class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == [] or board == [[]]:
            return False

        def find(board, i, j, k):

            if 0 <= i < row and 0 <= j < col and board[i][j] == word[k]:
                k += 1
                if k == len(word):
                    return True
                else:
                    board[i][j] = 0
                    if find(board, i + 1, j, k) or find(board, i - 1, j, k) or \
                            find(board, i, j + 1, k) or find(board, i, j - 1, k):
                        return True
                    # 回溯法的关键
                    k -= 1
                    board[i][j] = word[k]

        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                k = 0
                res = find(board, i, j, k)
                if res:
                    return res

        return False




if __name__ == '__main__':
    board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
    word = "SEE"
    res = Solution().exist(board, word)

    print(res)



