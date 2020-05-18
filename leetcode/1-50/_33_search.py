class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # 先查找旋转点
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                break
            elif nums[l] <= nums[mid]:
            # 注意这里的条件是nums[l] <= nums[mid]有一个=号，当l=mid时，说明l和r是相邻的，此时有两种情况，
            # 一种nums[l]<nums[r]此时之前的判断已经找到l是轴点，另一种nums[r]>nums[r]此时r为轴点，那么令l=l+1
                l = mid + 1
            else:
                r = mid

        # 进行二分查找
        pivor = l
        index_l = self.binary_search(nums[:pivor], target)
        if index_l >= 0:
            return index_l
        index_r = self.binary_search(nums[pivor:], target)
        if index_r >= 0:
            return index_r + pivor
        return -1

    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1



if __name__ == '__main__':
    nums = [1,3]
    target = 1
    index = Solution().search(nums, target)
    print(index)
