class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 边界情况，当numRows == 1时，loop_num为0会出错
        if numRows == 1: return s

        loop_num = 2 * numRows - 2  #loop_num是一个循环

        # 初始化矩阵，每个列表作为一行
        matrix = []
        for i in range(min(numRows, len(s))):
            matrix.append([])

        # 将字符储存在矩阵中
        for i in range(len(s)):
            remainder = i % loop_num
            if remainder <= loop_num / 2:
                matrix[remainder].append(s[i])
            else:
                matrix[loop_num-remainder].append(s[i])

        # 遍历列表得到结果
        convert_string = ""
        for row in matrix:
            for char in row:
                convert_string += char

        return convert_string




if __name__ == '__main__':
    s = "a"
    numRows = 1
    result = Solution().convert(s, numRows)
    print(result)