class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        画画图，更好理解
        """
        # 先考虑边界情况,  intervals为空，newInterval位于intervals的右边界和左边界
        if intervals == []:
            intervals = [newInterval]
            return intervals

        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        # 左边界其实可以去掉
        if newInterval[1] < intervals[0][0]:
            intervals = [newInterval] + intervals
            return intervals

        # 一般情况, newInterval和cur一共有6种情况
        for i in range(len(intervals)):
            cur = intervals[i]

            if newInterval[0] > cur[1]:
                continue

            if newInterval[1] < cur[0]:
                intervals.insert(i, newInterval)

            elif newInterval[0] <= cur[0] and newInterval[1] <= cur[1]:
                intervals[i] = [newInterval[0], cur[1]]

            elif newInterval[0] > cur[0] and newInterval[1] <= cur[1]:
                intervals[i] = cur

            elif newInterval[1] > cur[1]: # 包含两种情况
                final_i = [min(newInterval[0], cur[0])] # 找到起点
                intervals.pop(i)
                while len(intervals) > i:
                    cur = intervals[i]
                    if cur[1] <= newInterval[1]:
                        intervals.pop(i)
                    elif cur[0] <= newInterval[1] and cur[1] > newInterval[1]:
                        final_i.append(cur[1])
                        intervals[i] = final_i
                        break
                    else: # cur[0] > newIntervals[1]
                        final_i.append(newInterval[1])
                        intervals.insert(i, final_i)
                        break
                if len(intervals) == i:
                    final_i.append(newInterval[1])
                    intervals.append(final_i)
            return intervals



if __name__ == '__main__':
    intervals = [[1, 5]]
    newInterval = [2, 7]
    res = Solution().insert(intervals, newInterval)
    print(res)


