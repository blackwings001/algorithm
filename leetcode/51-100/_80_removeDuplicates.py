class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        i = 0
        two_flag = False

        for j in range(1, len(nums)):
            if nums[j] == nums[i] and two_flag == False:
                i += 1
                nums[i] = nums[j]
                two_flag = True

            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
                two_flag = False

        return i + 1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3]
    res = Solution().removeDuplicates(nums)
    print(res)

