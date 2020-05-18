#coding=utf-8

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if length <= 1:
            return matrix

        loop = length // 2    # loop是需要顺时针转动的圈数，length和loop的关系是，2：1，3：1，4：2，5：2...（中心为一个元素的不需要移动）

        for i in range(loop):
            # 对于每一圈进行顺时针转动
            # 找好四个对应点的位置，这是最难的地方，需要画图, 先找好定点位置的坐标表示，然后判断j应该怎么放到坐标中去表示这一部分元素
            # 刻画顶点需要两个数值，我们使用min和max表示，min是坐标中出现的最小值，max是坐标中出现的最大值
            min = i
            max = length - i - 1
            for j in range(max-min):
                tmp = matrix[min][min+j]
                matrix[min][min+j] = matrix[max-j][min]
                matrix[max-j][min] = matrix[max][max-j]
                matrix[max][max-j] = matrix[min+j][max]
                matrix[min+j][max] = tmp




if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    Solution().rotate(matrix)
    print(matrix)