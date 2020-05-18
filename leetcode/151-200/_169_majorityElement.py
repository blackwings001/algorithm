class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        major = nums[0]
        flag = 0

        for ele in nums:
            if ele == major:
                flag += 1
            else:
                flag -= 1
                if flag < 0:
                    major = ele
                    flag = 1

        return major


if __name__ == '__main__':
    nums = [1,2,2,3,5,1,2,2,2]
    res = Solution().majorityElement(nums)
    print(res)