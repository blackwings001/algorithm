class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        max_area = 0

        while left_index < right_index:
            left_value = height[left_index]
            right_value = height[right_index]
            cur_area = min(left_value, right_value) * (right_index - left_index)
            if cur_area > max_area:
                max_area = cur_area
            if left_value < right_value:
                left_index += 1
            else:
                right_index -= 1

        return max_area

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    max_area = Solution().maxArea(height)
    print(max_area)
