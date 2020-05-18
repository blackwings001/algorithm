class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0":
            return 0

        res = [1, 1]
        for i in range(1, len(s)):
            c = s[i] # 当前字符
            p = s[i-1] # 上一个字符
            if c == "0":
                if p not in ["1", "2"]:
                    return 0
                res.append(res[-2]) # 选取上上步情况
            elif p == "1" or (p == "2" and c not in ["7", "8", "9"]):
                res.append(res[-1] + res[-2]) # 上步和上上步之和
            else:
                res.append(res[-1]) # 选取上步情况

        return res[-1]

if __name__ == '__main__':
    s = "1223213132141"
    res = Solution().numDecodings(s)
    print(res)
