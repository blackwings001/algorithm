class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return []

        start = 0
        end = len(numbers) - 1

        while end > start:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start + 1, end + 1]

        return []


if __name__ == '__main__':
    numbers = [2, 7, 9, 11]
    target = 9
    res = Solution().twoSum(numbers, target)
    print(res)
