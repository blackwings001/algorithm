class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]

        res = []
        for k in range(len(nums) + 1):
            cur_set = []
            self.subset(res, k, cur_set, nums)

        return res

    def subset(self, res, k, cur_set, nums):
        if len(cur_set) == k:
            res.append(cur_set)
            return

        if k - len(cur_set) > len(nums):
            return

        for i in range(len(nums)):
            self.subset(res, k, cur_set + [nums[i]], nums[i + 1 :] if i < len(nums) - 1 else [])

if __name__ == '__main__':
    nums = [1,5,2,8,9]
    res = Solution().subsets(nums)
    print(res)
