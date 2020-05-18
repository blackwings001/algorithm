#coding=utf-8

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1

        # 第一遍遍历数组，将值位于(0,length]之间的正整数放到对应位置
        length = len(nums)
        for i in range(length):
            self.correct(nums, i, length)

        # 第二遍遍历数组，如果num[i] != i+1, 返回i+1， 如果都符合，返回length+1
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1

        return length + 1

    def correct(self, nums, i, length):
        if nums[i] <= 0 or nums[i] > length:
            pass
        else:
            tmp = nums[nums[i] - 1]  # nums[i] - 1是nums[i]应该放置的位置
            if tmp != nums[i]:      # 如果nums[i] - 1位置的值tmp和nums[i]不相等，则进行交换，并再次在此位置调用correct
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
                self.correct(nums, i, length)



if __name__ == '__main__':
    nums = [3,4,-1,1]
    result = Solution().firstMissingPositive(nums)
    print(result)