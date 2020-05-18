class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 4:
            return result

        nums = sorted(nums)
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    combine = [nums[i], nums[j], nums[l], nums[r]]
                    if s == target:
                        if combine not in result:
                            result.append(combine)
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return result


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    result = Solution().fourSum(nums, target)
    print(result)
