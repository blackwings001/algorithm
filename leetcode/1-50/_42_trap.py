#coding=utf-8

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        l = 0
        r = len(height) - 1
        water = 0

        while l < r:
            if height[l] <= height[r]:
                l, sub_water = self.get_water(height, l, direction="left")
            else:
                r, sub_water = self.get_water(height, r, direction="right")
            water += sub_water

        return water

    def get_water(self, height, index, direction):
        next_i = index
        sub_water = 0
        if direction == "left":
            # 找到第一个不矮的柱子
            for i in range(index+1, len(height)):
                if height[i] >= height[index]:
                    next_i = i
                    break
            # 记录雨水
            for i in range(index, next_i):
                sub_water += height[index] - height[i]

        elif direction == "right":
            # 找到第一个不矮的柱子
            for i in range(index-1, -1, -1):
                if height[i] >= height[index]:
                    next_i = i
                    break
            # 记录雨水
            for i in range(index, next_i, -1):
                sub_water += height[index] - height[i]

        return next_i, sub_water

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = Solution().trap(height)
    print(result)


