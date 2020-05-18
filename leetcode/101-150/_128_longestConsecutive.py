class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # 使用哈希表让查找的速度缩短为O(1)
        nums = set(nums)
        longest_len = 0

        # 遍历哈希表中的每一个元素，注意只有连续序列的首元素才会进行第二轮遍历
        # 也就是说貌似是一个双重遍历，但实际上每个元素最多被遍历两次，总体的时间复杂度是O(n)
        for ele in nums:
            if ele - 1 not in nums:
                cur_len = 0
                while ele in nums:
                    cur_len += 1
                    ele += 1
                longest_len = max(longest_len, cur_len)

        return longest_len


if __name__ == '__main__':
    nums = [200, 4, 100, 1, 3, 2]
    res = Solution().longestConsecutive(nums)
    print(res)
