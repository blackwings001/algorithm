class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        j = 0
        for i in range(len(nums)):
            if i == j:  # i和j位于同一位置时，i+=1
                continue
            if nums[j] != nums[i]: # nums[j] != nums[i]时，j += 1 然后nums[j] = nums[i]
                j += 1
                nums[j] = nums[i]
        return j + 1

if __name__ == '__main__':
    nums = [1,1,2,3,4,5]
    result = Solution().removeDuplicates(nums)
    print(result)