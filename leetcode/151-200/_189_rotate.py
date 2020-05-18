class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums

        n = len(nums)
        k %= n

        # 环形移动，一共移动n次
        def roll():
            count = 0
            for i in range(n):
                if count == n:
                    break
                tmp = (i + k) % n
                while tmp != i:
                    nums[i], nums[tmp] = nums[tmp], nums[i]
                    tmp = (tmp + k) % n
                    count += 1
                count += 1
            return nums

        # 三次翻转
        def reverse():
            interval = n - k
            for i in range(interval // 2):
                nums[i], nums[interval - i - 1] = nums[interval - i - 1], nums[i]

            for i in range(interval, interval + (n - interval) // 2):
                nums[i], nums[n - 1 - (i - interval)] = nums[n - 1 - (i - interval)], nums[i]

            for i in range(n // 2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

            return nums

        nums = roll()
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = Solution().rotate(nums, k)
    print(res)
