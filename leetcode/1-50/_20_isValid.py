class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        right_left = {")":"(", "}":"{", "]":"["}

        for index in range(len(s)):
            ele = s[index]
            if ele in right_left.values():
                stack.append(ele)
            elif ele in right_left.keys():
                if stack != [] and stack[-1] == right_left[ele]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False

        if stack == []:
            return True

        return False

if __name__ == '__main__':
    s = "(()()(())()()()(())()()()())"




