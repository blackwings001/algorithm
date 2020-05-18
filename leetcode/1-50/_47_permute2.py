class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 需要使用递归的方法进行全排列的查找
        if len(nums) <= 1:
            return [nums]

        res = []
        sub = []
        nums = sorted(nums) # 进行排序，用于后面的跳过操作

        self.get_permute(nums, sub, res)

        return res

    def get_permute(self, nums, sub, res):
        # 递归基
        if nums == []:
            res.append(sub)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:      # 跳过的条件，注意没有比较全排列一样的数字，跳过即可
                continue
            self.get_permute(nums[:i] + nums[i + 1:], sub + [nums[i]], res)

if __name__ == '__main__':
    nums = [1]
    result = Solution().permuteUnique(nums)
    print(result)