class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        # 先判断dividend和divisor是否同号，结果1先按两个正数来做，如果两者异号，结果为（-结果1 - 1）(LEETCODE的结果不一样，他认为结果为-结果1)
        negative = dividend ^ divisor < 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        # 主循环，找到diviend大于等于divisor右移最大的位数，此时说明diviend至少包含1 << i个divisor， 则dividend -= divisor << i和result += 1 << i
        result = 0
        while dividend >= divisor:
            for i in range(31, -1, -1):
                if dividend >> i >= divisor:
                    result += 1 << i
                    dividend -= divisor << i
                    break

        # 判断result范围
        if (result >= 1 << 31 and not negative) or (result > 1 << 31 + 1 and negative):
            return (1 << 31) - 1

        return -result if negative else result


if __name__ == '__main__':
    dividend = -2147483648
    divisor = -1

    result = Solution().divide(dividend, divisor)
    print(dividend//divisor)
    print(result)