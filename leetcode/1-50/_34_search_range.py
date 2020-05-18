class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.search_start(nums, target)
        end = self.search_end(nums, target)
        return [start, end]

    def search_start(self, nums, target):
        # 找到最左边的target
        if nums == []:
            return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            return l
        return -1

    def search_end(self, nums, target):
        # 找到最右边的target
        if nums == []:
            return -1
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r + 1) >> 1    # 注意这里是(l + r + 1) >> 1保证mid取到中间靠右的位置
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        return -1


if __name__ == '__main__':
    nums = [1,2,3,3,3,5]
    target = 3
    result = Solution().searchRange(nums, target)
    print(result)
