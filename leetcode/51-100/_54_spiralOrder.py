class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if matrix == []:
            return result

        i = 0 # 第几圈,每圈的起点是matrix[i][i]
        cur_row = len(matrix)  # 第i圈的行数
        cur_col = len(matrix[0])  # 第i圈的列数

        while True:
            # 定位该圈四个点的横纵坐标, 只需要对角两个点的坐标即可
            row1 = i
            row2 = i + cur_row - 1
            col1 = i
            col2 = i + cur_col - 1

            if cur_row >= 2 and cur_col >= 2:
                result.extend([matrix[row1][j] for j in range(col1, col2)])     # 使用列表表达式添加元素，matrix[row1:row2][col1]这种方式是错的
                result.extend([matrix[i][col2] for i in range(row1, row2)])
                result.extend([matrix[row2][j] for j in range(col2, col1, -1)])
                result.extend([matrix[i][col1] for i in range(row2, row1, -1)])
                cur_row -= 2
                cur_col -= 2
                i += 1
                continue

            elif cur_col == 0 or cur_row == 0:
                return result

            elif cur_row == 1:
                # 只有一行的情况
                result.extend([matrix[row1][j] for j in range(col1, col2 + 1)])

            elif cur_col == 1:
                # 只有一列的情况
                result.extend([matrix[i][col2] for i in range(row1, row2 + 1)])

            return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.spiralOrder([[3],[2]])
    print(result)