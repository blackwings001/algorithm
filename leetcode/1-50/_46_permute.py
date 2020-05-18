class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 需要使用递归的方法进行全排列的查找
        result = []
        sub = []

        for i in nums:
            self.get_permute(nums, sub+[i], result)

        return result

    def get_permute(self, nums, sub, result):
        # 递归基
        if len(sub) == len(nums):
            result.append(sub)
            return

        for i in nums:
            if i not in sub:
                self.get_permute(nums, sub+[i], result)

if __name__ == '__main__':
    nums = [1, 2,3,4]
    result = Solution().permute(nums)
    print(result)