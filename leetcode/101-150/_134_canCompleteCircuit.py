class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or (len(gas) != len(cost)) or sum(gas) < sum(cost):
            return -1

        start = 0
        end = 0
        cur = 0
        while end < len(gas):
            cur += (gas[end] - cost[end])
            if cur < 0:
                start = end + 1
                end = start
                cur = 0
            else:
                end += 1

        if start < len(gas):
            return start
        return -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    result = Solution().canCompleteCircuit(gas, cost)
    print(result)
