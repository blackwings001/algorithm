class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        b1 = 0  # 某个位置为1是，说明该位置出现了一次1
        b2 = 0  # 某个位置为1是，说明该位置出现了两次1
        for n in nums:
            b1 = (b1 ^ n) & ~b2
            b2 = (b2 ^ n) & ~b1

        return b1


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2, 1, 2]
    res = Solution().singleNumber(nums)
    print(res)
