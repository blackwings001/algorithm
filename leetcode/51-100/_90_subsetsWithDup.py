class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]

        # 排序好跳过重复元素
        nums.sort()
        res = []
        tmp = []

        def subsets(start, tmp):
            res.append(tmp)

            for i in range(start, len(nums)):
                # 跳过重复元素，好好体会, 我们要跳过的重复元素指的是未遍历数组中的重复元素，第一个元素不跳过
                if i > start and nums[i] == nums[i-1]:
                    continue
                # 递归，自己长度加1
                subsets(i + 1, tmp + [nums[i]])

        subsets(0, tmp)
        return res

if __name__ == '__main__':
    nums = list(range(10)) + [1 for _ in range(100)]
    res = Solution().subsetsWithDup(nums)
    print(res)
    print(len(res))

    res = 1
    for i in range(1, 11):
        res *= i

    print(res)

