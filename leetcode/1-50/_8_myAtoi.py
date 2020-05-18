class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0

        num = 0
        symnol = 0   # 符号位
        pre_0 = 0    # 前一个字符是否为0
        char_num = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        char_symbol = ["+", "-"]

        index = 0
        length = len(str)

        # 先寻找第一个符合条件的字符
        while index < length:
            char = str[index]

            if pre_0 == 0:      # 前一个字符不为"0"的情况下
                if char == " ":
                    index += 1
                    continue
                if char == "0":
                    pre_0 = 1
                    index += 1
                    continue
                if char not in char_num and char not in char_symbol:
                    return num
                if char == "+":
                    symnol = 1
                if char == "-":
                    symnol = -1
                if char in char_num:
                    symnol = 1
                    num = char_num[char]
                index += 1
                break
            else:
                if char not in char_num:
                    return num
                elif char == "0":
                    index += 1
                    continue
                else:
                    symnol = 1
                    num = char_num[char]
                index += 1
                break

        # 连接后后续的数字字符
        while index < length:
            char = str[index]
            if char not in char_num:
                break
            num = num * 10 + char_num[char]
            index += 1

        # 输出最后的结果，需要判断范围
        high = 2 ** 31 - 1
        low = - 2 ** 31
        if symnol * num > high:
            result = high
        elif symnol * num < low:
            result = low
        else:
            result = symnol * num

        return result


if __name__ == '__main__':
    result = Solution().myAtoi(" -42")
    print(result)