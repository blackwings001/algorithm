class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        transform_int = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        transform_roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for index in range(len(transform_int)):
            # 下面是一个循环，跳出循环后，index会自动+1
            while num >= transform_int[index]:
                num -= transform_int[index]
                roman += transform_roman[index]

        return roman

if __name__ == '__main__':
    num = 3
    roman = Solution().intToRoman(num)
    print(roman)