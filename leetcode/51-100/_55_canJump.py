class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False

        last_index = len(nums) - 1
        nearest_true = last_index  # 记录值为True的索引最小的位置

        for i in range(len(nums) - 1, -1, -1):
            jump = nums[i]
            # 如果nearest_true在i的跳跃范围内，那么i能到达终点
            if i + jump >= nearest_true:
                nearest_true = i

        return True if nearest_true == 0 else False


