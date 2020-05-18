from decimal import *
getcontext().prec = 50

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        max_points = 1
        nums = len(points)

        for i in range(nums):
            cur = points[i]
            cur_points = {"infinite": 1}  # 斜率不存在时的直线
            same_point = 0
            for j in range(i + 1, nums):
                p = points[j]
                if p == cur:
                    same_point += 1
                elif p[0] == cur[0]:
                    cur_points["infinite"] += 1
                else:
                    k = Decimal(p[1] - cur[1]) / Decimal(p[0] - cur[0])
                    cur_points[k] = cur_points.get(k, 1) + 1

            max_points = max(max_points, max(cur_points.values()) + same_point)

        return max_points


if __name__ == '__main__':
    points = [[1, 1], [1, 2], [2, 2], [3, 3], [4, 4]]
    res = Solution().maxPoints(points)
    print(res)
