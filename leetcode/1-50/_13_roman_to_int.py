class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
                     "C": 100, "XC": 90, "L": 50, "XL": 40,
                     "X": 10, "IX": 9, "V": 5, "IV": 4,
                     "I": 1}
        num = 0
        index = 0
        while index < len(s):
            one_char = s[index]
            if index == len(s) - 1:  # 边界情况，two_char可能不存在
                return num + roman_int[one_char]
            two_char = s[index:index+2]
            # 先检查two_char
            if two_char in roman_int:
                index += 2
                num += roman_int[two_char]
            elif one_char in roman_int:
                index += 1
                num += roman_int[one_char]
            else:
                print("roman is false!")
                return 0
        return num
