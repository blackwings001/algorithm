class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry
            digits[i] = digit % 10
            carry = digit // 10

        if carry == 1:
            digits.insert(0, 1)

        return digits



if __name__ == '__main__':
    digits = [0]
    res = Solution().plusOne(digits)
    print(res)