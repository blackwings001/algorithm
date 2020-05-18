class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        string_list = []

        if digits == None:
            return string_list

        digits = str(digits)
        while digits != "":
            if digits[0] not in num_letter:
                return None
            string_list = self.get_letter_combinations(digits[0], string_list, num_letter)
            digits = digits[1:] if len(digits) > 1 else ""
        return string_list


    def get_letter_combinations(self, digit, string_list, num_letter):
        digit_string = num_letter[digit]
        string_list = [i for i in digit_string] if string_list == [] else [j + i for j in string_list for i in digit_string]
        return string_list

class SolutionRecuision(object):
    def __init__(self):
        self.num_letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        index = 0 # 索引指针，从前向后移动

        if not digits:
            return result

        self.get_letter_combinations(digits, index, "", result)


        return result


    def get_letter_combinations(self, digits,index, s, result):
        # 递归基
        if index == len(digits):
            result.append(s)
            return

        num = digits[index]
        if num in self.num_letter:
            letters = self.num_letter[num]
            for letter in letters:
                self.get_letter_combinations(digits, index+1, s+letter, result)
        else:
            self.get_letter_combinations(digits, index+1, s, result)




if __name__ == '__main__':
    digits = "23547"
    result = SolutionRecuision().letterCombinations(digits)
    print(result)
