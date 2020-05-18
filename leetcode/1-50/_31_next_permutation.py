class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return

        # 先检查nums是否为最大字典序
        max_flag = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                max_flag = False
                break
        if max_flag:
            for i in range(len(nums)//2):
                reverse_index = len(nums) - 1 - i
                nums[i], nums[reverse_index] = nums[reverse_index], nums[i]
            return

        # 找到一般情况下的下一个字典序
        # 1.从右至左找到第一个左邻比右邻小的数
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                # 2.从右至左找到第一个比nums[i-1]大的数
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        # 3.交换nums[i-1]和nums[j]
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        # 4.对nums[i-1]后面的数，从小到大排序
                        for k in range(i, len(nums)):
                            for m in range(i, len(nums) - (k - i) -1):
                                if nums[m] > nums[m+1]:
                                    nums[m], nums[m+1] = nums[m+1], nums[m]
                        return

if __name__ == '__main__':
    # nums = [4,1,5,2,3]
    nums = [1,3,2]
    Solution().nextPermutation(nums)
    print(nums)

