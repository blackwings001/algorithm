class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1
        while True:
            if end - start == 1:
                return min(nums[end], nums[start])
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid


if __name__ == '__main__':
    nums = [4, 5, 0, 1, 2]
    res = Solution().findMin(nums)
    print(res)
