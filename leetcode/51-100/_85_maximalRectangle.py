class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        max_area = 0
        heights = [0 for _ in range(len(matrix[0]))]

        def get_area(heights):
            if len(heights) == 0:
                return 0

            area = 0
            stack = [-1] # 存储索引

            for i, h in enumerate(heights + [-1]):
                # 小心数组越界
                if i == len(heights) or h < heights[stack[-1]]:
                    while stack[-1] != -1 and h < heights[stack[-1]]:
                        area = max(area, heights[stack[-1]] * (i - stack[-2] - 1))
                        stack.pop()
                stack.append(i)

            return area


        for i in range(row):
            # 计算该行的柱子高度
            for j in range(col):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0

            # 计算该行的最大面积
            max_area = max(max_area, get_area(heights))

        return max_area

if __name__ == '__main__':
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

    res = Solution().maximalRectangle(matrix)
    print(res)
