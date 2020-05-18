class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None

        stack = []
        signs = {"+", "-", "*", "/"}
        for ele in tokens:
            if ele in signs:
                ele2 = int(stack.pop())
                ele1 = int(stack.pop())
                if ele == "+":
                    stack.append(ele1 + ele2)
                elif ele == "-":
                    stack.append(ele1 - ele2)
                elif ele == "*":
                    stack.append(ele1 * ele2)
                elif ele == "/":
                    stack.append(ele1 / ele2)
            else:
                stack.append(ele)

        return int(stack.pop())


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    res = Solution().evalRPN(tokens)
    print(res)
