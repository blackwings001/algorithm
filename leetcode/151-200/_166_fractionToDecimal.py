class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0 or denominator == 0:
            return "0"

        res = ""
        if numerator * denominator < 0:
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator // denominator
        remainder = numerator % denominator

        res += str(quotient) + "."
        remainder_index = len(res)
        remainder_dict = {remainder: remainder_index}

        while remainder != 0:
            remainder_index += 1
            quotient = remainder * 10 // denominator
            remainder = remainder * 10 % denominator
            res += str(quotient)

            if remainder in remainder_dict:
                break
            remainder_dict[remainder] = remainder_index

        if remainder == 0:
            if res[-1] == ".":
                res = res[:-1]
            return res
        else:
            start = remainder_dict[remainder]
            res = res[:start] + "(" + res[start:] + ")"
            return res


if __name__ == '__main__':
    print(Solution().fractionToDecimal(1, 7))
    print(Solution().fractionToDecimal(0, 7))
    print(Solution().fractionToDecimal(4, 10))
    print(Solution().fractionToDecimal(10, 2))
    print(Solution().fractionToDecimal(10, 7))
