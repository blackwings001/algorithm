class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        # 现根据区间的首元素进行排序
        intervals.sort()

        # 不断扫描排序后的区间，根据条件改变或添加res的值
        res = [intervals.pop(0)]

        for i in range(len(intervals)):
            cur = res[-1]
            next = intervals[i]
            if cur[1] < next[0]:
                res.append(next)
            elif cur[1] < next[1]:
                res[-1] = [cur[0], next[1]]

        return res

    # def merge_sort(self, intervals):
    #     if len(intervals) == 1:
    #         return intervals
    #
    #     mid = len(intervals) // 2
    #     left = self.merge_sort(intervals[:mid])
    #     right = self.merge_sort(intervals[mid:])
    #
    #     return self.merge_list(left, right)
    #
    # def merge_list(self, left, right):
    #     result = []
    #     while len(left) > 0 and len(right) > 0:
    #         if left[0][0] <= right[0][0]:
    #             result.append(left.pop(0))
    #         else:
    #             result.append(right.pop(0))
    #
    #     result += left
    #     result += right
    #
    #     return result



if __name__ == '__main__':
    S = Solution()
    list1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = S.merge(list1)
    print(res)