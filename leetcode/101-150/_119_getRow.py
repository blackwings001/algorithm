class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        cur = [1, 1]

        for j in range(3, rowIndex + 2):
            next = [1 for _ in range(j)]
            for i in range(len(cur) - 1):
                next[i + 1] = cur[i] + cur[i + 1]
            cur = next

        return cur


if __name__ == '__main__':
    rowIndex = 3
    res = Solution().getRow(rowIndex)
    print(res)
