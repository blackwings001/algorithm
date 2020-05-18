class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "":
            return b
        if b == "":
            return a
        res = ""

        carry = 0
        length = max(len(a), len(b))

        # 从右到左遍历数组
        for i in range(-1, -length - 1, -1):
            a_v = 0 if -i > len(a) else int(a[i])
            b_v = 0 if -i > len(b) else int(b[i])
            sum = carry + a_v + b_v

            if sum == 0:
                res = "0" + res
                carry = 0
            elif sum == 1:
                res = "1" + res
                carry = 0
            elif sum == 2:
                res = "0" + res
                carry = 1
            elif sum == 3:
                res = "1" + res
                carry = 1

        if carry == 1:
            res = "1" + res

        return res



if __name__ == '__main__':
    a = "10011"
    b = "1011"
    res = Solution().addBinary(a, b)
    print(res)