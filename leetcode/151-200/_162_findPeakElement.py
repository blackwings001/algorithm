class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        import sys
        nums.append(-sys.maxsize)
        nums = [-sys.maxsize] + nums

        start = 0
        end = len(nums) - 1

        while True:
            mid = (start + end) // 2
            ele = nums[mid]
            ele_l = nums[mid - 1]
            ele_r = nums[mid + 1]

            if ele_l > ele:
                end = mid
            elif ele_r > ele:
                start = mid
            else:
                return mid - 1


if __name__ == '__main__':
    nums = [1, 2, 1]
    res = Solution().findPeakElement(nums)
    print(res)