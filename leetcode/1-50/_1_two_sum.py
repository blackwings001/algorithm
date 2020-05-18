class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}
        for i in range(len(nums)):
            x = nums[i]
            target_x = target - x

            if target_x in num_index.keys():
                return [num_index[target_x], i]
            num_index[x] = i

        return []



if __name__ == '__main__':
    solution = Solution()
