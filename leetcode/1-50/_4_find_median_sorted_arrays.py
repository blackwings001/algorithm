class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 特殊情况
        if len(nums1) == 0 and len(nums2) == 0:
            return None

        # 设置nums1为较短的有序数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        odd = 1 if (n + m) % 2  == 1 else 0  # 判断奇偶性

        # 划分点i从0到n，一共n+1种情况，nums1[:i]一共有i个元素，nums1[i-1]是左边的最大元素
        imin = 0
        imax = n
        while imin <= imax : # 循环结束一定出结果
            # i和j之和是nums1和nums2左边数组的长度和，可能是总长度一半（总长度为偶数时），或者偏少的一半（总长度为奇数时）
            # 这样的划分，导致max_left稍微复杂一点
            i = (imin + imax) // 2
            j = (n + m) // 2 - i
            # 下面确定max_left和min_right，需要考虑边界情况
            if i != 0 and j != 0:
                max_left = max(nums2[j - 1], nums1[i - 1])
            elif i != 0:
                max_left = nums1[i - 1]
            elif j != 0:
                max_left = nums2[j - 1]
            else: # i和j可能同时为0
                max_left = None

            if i != n and j != m:
                min_right = min(nums1[i], nums2[j])
            elif i != n:
                min_right = nums1[i]
            elif j != m:
                min_right =  nums2[j]
            else: # 当两数组不均为空时，min_right不会是None
                min_right = None

            # 进行二分查找
            if max_left == None or max_left <= min_right : # max_left == None, 一定是两个数组一个是空，一个是1个元素，返回min_right即可
                return min_right if odd else (max_left + min_right) / 2
            elif  i != 0 and nums1[i - 1] > nums2[j]: # nums1[i - 1]较大,切分点左移
                imax = i - 1
            elif j != 0 and nums2[j - 1] > nums1[i]:  # nums1[i]较小，切分点右移
                imin = i + 1

if __name__ == '__main__':
    nums1 = []
    nums2 = [3]
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(result)



