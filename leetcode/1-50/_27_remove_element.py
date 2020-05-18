class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0

        for j in range(len(nums)):
            if nums[j] != val:
                continue
            for i in range(j+1, len(nums)):
                if nums[i] != val:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
                if i == len(nums) - 1: # 当i到达nums最后一个元素，且nums[i]==val时，返回j
                    return j

        # 退出上面循环时，判断nums的最后一个元素与val的关系
        if nums[-1] != val:
            return len(nums)
        else:
            return len(nums) - 1

if __name__ == '__main__':
    nums = [3,2,2,3]
    result = Solution().removeElement(nums, 3)
    print(result)