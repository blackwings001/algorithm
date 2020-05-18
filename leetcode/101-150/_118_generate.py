class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if numRows == 0:
        #     return []

        triangle = [[1 for _ in range(i + 1)] for i in range(numRows)]
        for i in range(1, numRows - 1):
            for j in range(i):
                triangle[i + 1][j + 1] = triangle[i][j] + triangle[i][j + 1]

        print(triangle)
        for k in triangle:
            print(k)

        return triangle


if __name__ == '__main__':
    numRows = 0
    Solution().generate(numRows)
