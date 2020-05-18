class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0

        max_v = max(nums)
        min_v = min(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        interval = (max_v - min_v) // (len(nums)) + 1

        for ele in nums:
            index = (ele - min_v) // interval
            bucket[index].append(ele)

        pre_min = max(bucket[0])
        max_gap = 0

        for i in range(1, len(bucket)):
            if bucket[i]:
                gap = min(bucket[i]) - pre_min
                max_gap = max(gap, max_gap)
                pre_min = max(bucket[i])

        return max_gap


if __name__ == '__main__':
    nums = [3,6,9,1]

    res = Solution().maximumGap(nums)
    print(res)
