class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None

        nums = sorted(nums) # nums进行排序
        closest_sum = nums[0] + nums[1] + nums[2] # 初始化cloest_sum
        for i in range(0, len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s-target) < abs(closest_sum-target):
                    closest_sum = s
                if s > target:
                    r -= 1
                elif s == target:
                    return s
                else:
                    l += 1
        return closest_sum

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    result = Solution().threeSumClosest(nums, 1)
    print(result)