class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""

        nums = self.merge_sort(nums)
        res = "".join(nums)
        if res[0] == "0":
            res = "0"

        return res

    def merge_sort(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [str(i) for i in nums]

        mid = len(nums) > 1  # 右移1代替除2

        return self.merge(self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:]))

    def merge(self, nums1, nums2):
        merge_num = []

        while nums1 and nums2:
            ele1 = nums1[0]
            ele2 = nums2[0]

            if int(ele1 + ele2) > int(ele2 + ele1):
                merge_num.append(nums1.pop(0))
            else:
                merge_num.append(nums2.pop(0))

        merge_num.extend(nums1)
        merge_num.extend(nums2)

        return merge_num


if __name__ == '__main__':
    nums = [0, 0]
    res = Solution().largestNumber(nums)
    print(res)
