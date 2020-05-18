class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 需要对数组先排序
        nums = sorted(nums)
        three_nums = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]: # 跳过重复的数字
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        three_nums.append([nums[i], nums[l], nums[r]])
                        # 先移动指针
                        l += 1
                        r -= 1
                        # 根据条件，判断是否在移动指针
                        while l < r and nums[l] == nums[l-1]:   # 跳过重复数字
                            l += 1
                        while l < r and nums[r] == nums[r+1]:   # 跳过重复数字
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1

        return three_nums

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    result = Solution().threeSum(nums)
    print(result)
