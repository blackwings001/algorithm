class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []:
            return 0

        # 这道题的本质是，如何在O(1)的时间内，找到每个元素的以该元素为最低点的左右边界
        stack  = []
        stack.append(-1) # 记录左边界索引

        max_area = 0

        # 将heights元素依次放入栈中， 如果遇到逆序，则将前面的元素弹出，栈中每个元素的上一个元素都是其左边第一个比他矮的元素，也就是左边界
        for i, height in enumerate(heights + [-1]):
            if height <= heights[stack[-1]] or i == len(heights):
                # 以heights[stack[-1]]为最低点的矩形， i是右边界，stack[-2]是左边界
                while stack[-1] != -1 and height < heights[stack[-1]]:
                    max_area = max(heights[stack[-1]] * (i - stack[-2] - 1), max_area)
                    stack.pop()
            stack.append(i)

        return max_area


if __name__ == '__main__':
    heights = [2,1,5,6,3,2]
    res = Solution().largestRectangleArea(heights)
    print(res)
