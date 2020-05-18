class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """


        length = n + m - 1
        for i in range(length, -1, -1):
            if m == 0 :
                nums1[i] = nums2[n - 1]
                n -= 1
            elif n == 0 :
                nums1[i] = nums1[m - 1]
                m -= 1
            elif nums1[m - 1] > nums2[n - 1]:
                    nums1[i] = nums1[m - 1]
                    m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)