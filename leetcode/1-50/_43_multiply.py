#coding=utf-8

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = "0"
        if num1 == "0" or num2 == "0":
            return result

        # 获得num1和num2的数字表示
        num1 = self.string2num(num1)
        num2 = self.string2num(num2)
        multiply = num1 * num2

        result = self.num2string(multiply)
        return result

    def string2num(self, string):
        # 字符变为数字
        num = 0
        for char in string:
            num = num * 10 + ord(char) - ord("0")
        return num

    def num2string(self, num):
        # 数字变为字符
        string = ""
        while num != 0:
            char = chr(num % 10 + ord("0"))
            string = char + string
            num //= 10
        return string

if __name__ == '__main__':
    num1 = "0"
    num2 = "456"
    result = Solution().multiply(num1, num2)
    print(result)
    print(0*456)

