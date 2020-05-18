class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        rooms = len(nums)

        if rooms == 1:
            return nums[0]

        res = [0 for _ in range(rooms)]
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])

        return res[-1]


if __name__ == '__main__':
    nums = [2, 1, 1, 2]
    res = Solution().rob(nums)
    print(res)