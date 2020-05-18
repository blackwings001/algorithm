class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False

        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        exp = "e"
        pos_neg = ["+", "-"]
        point = "."

        if len(s) == 1:
            if s[0] not in digits:
                return False
            return True

        # s长度大于等于2的情况
        if s[0] not in digits and s[0] not in pos_neg and s[0] != point:
            return False

        point_exit = False # 记录是否出现过.， 遇到e重置
        if s[0] == point:
            point_exit = True

        for i in range(1, len(s)):
            cur_char = s[i]
            pre_char = s[i-1]
            if cur_char not in digits and cur_char not in pos_neg and cur_char != exp and cur_char != point:
                return False
            if cur_char in pos_neg:
                return False
            if cur_char in digits:
                continue
            if cur_char == exp:
                if pre_char in pos_neg or pre_char == exp:
                    return False
                if pre_char == point:
                    if i == 1 or s[i - 2] not in digits:
                        return False
                if i == len(s) - 1:
                    return False
                point_exit = False
            if cur_char == point:
                if pre_char == point or pre_char == exp or point_exit:
                    return False
                if pre_char in pos_neg and i == len(s) - 1:
                    return False
                point_exit = True

        return True




if __name__ == '__main__':
    s = ".1."
    res = Solution().isNumber(s)
    print(res)