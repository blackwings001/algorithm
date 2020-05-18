class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        start = 0   # 跳跃位置
        old_one_step = 0    # 用于过滤曾经考虑过的第一步位置
        res = 0 # 记录跳跃步数

        if length == 1:
            return res

        while True:
            step = nums[start]
            # 先判断一步是否可以到达终点
            if start + step >= length - 1:
                return res + 1

            # 在寻找两步之后能到达的最远位置
            two_max = start + step + nums[start + step]  # two_max记录两步之后的最远位置
            next = start + step
            for i in range(old_one_step + 1, start + step):
                if two_max >= length - 1:
                    return res + 2
                if i + nums[i] > two_max:
                    two_max = i + nums[i]
                    next = i

            old_one_step = start + step
            start = next
            res += 1


if __name__ == '__main__':
    nums = [2,3,0,1,4]
    result = Solution().jump(nums)
    print(result)


