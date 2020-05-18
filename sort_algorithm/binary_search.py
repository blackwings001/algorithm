class Solution:
    def binary_search(self, nums, target):
        """
        返回nums中值为target的最左元素的索引
        :param nums:
        :param target:
        :return:
        """
        if nums == []:
            return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] == target:
            return l
        else:
            return -1


if __name__ == '__main__':
    nums = [1,2,3,3,3,3,5,21,21,4]
    target = 21
    result = Solution().binary_search(nums, target)
    print(result)