class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums

        nums.sort()
        print(nums)

        # 注意插入和pop的顺序 ！！
        nums.insert(0, 2)
        nums.insert(0, 1)
        nums.insert(0, 0)

        i, j, k = 0, 1, 2 # 分别记录0，1，2的首位置
        for m in range(3, len(nums)):
            if nums[m] == 0:
                nums[j] = 0
                j += 1
                nums[k] = 1
                k += 1
            elif nums[m] == 1:
                nums[k] = 1
                k += 1
            nums[m] = 2

        nums.pop(k)
        nums.pop(j)
        nums.pop(i)

if __name__ == '__main__':
    nums = [2,0,1]
    Solution().sortColors(nums)
    print(nums)