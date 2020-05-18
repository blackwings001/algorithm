class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        max = nums[i]
        cur = nums[i]
        if len(nums) == 1:
            return max

        for j in range(len(nums)):
            if i != j:
                cur += nums[j]
            if cur > max:
                max = cur
            if cur < 0:
                i = j + 1
                cur = nums[i]

        return max