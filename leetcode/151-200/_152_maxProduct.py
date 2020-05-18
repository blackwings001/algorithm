class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        import sys
        overall_max = -sys.maxsize
        local_max = 1
        local_min = 1

        for ele in nums:
            if ele >= 0:
                local_max = max(local_max * ele, ele)
                local_min = min(local_min * ele, ele)
            else:
                # 使用临时变量保存之前的local_min， local_max，防止更新时出错
                tmp1, tmp2 = local_max, local_min
                local_max = max(tmp2 * ele, ele)
                local_min = min(tmp1 * ele, ele)
            overall_max = max(overall_max, local_max)

        return overall_max


if __name__ == '__main__':
    nums = [-2, -3, -4]
    res = Solution().maxProduct(nums)
    print(res)