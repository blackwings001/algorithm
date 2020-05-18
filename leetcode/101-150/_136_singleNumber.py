class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        for i in range(len(nums) - 1):
            nums[i + 1] = nums[i] ^ nums[i + 1]

        return nums[-1]


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    res = Solution().singleNumber(nums)
    print(res)
