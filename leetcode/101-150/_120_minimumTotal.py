class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]

        pre = [0]

        for col in triangle:
            cur = [0 for _ in col]
            for i in range(len(col)):
                if i == 0:
                    cur[i] = col[i] + pre[i]
                elif i == len(col) - 1:
                    cur[i] = col[i] + pre[i - 1]
                else:
                    cur[i] = min(pre[i - 1], pre[i]) + col[i]
            pre = cur
            # print(pre)

        return min(cur)


if __name__ == '__main__':
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    res = Solution().minimumTotal(triangle)
    print(res)
