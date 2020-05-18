class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []

        res = []

        def meet(s):
            if s == "" or len(s) > 3 or (len(s) != 1 and s[0] == "0") or int(s) > 255:
                return False
            return True

        ## 因为最多只有12位数字，使用三层循环即可，时间复杂度也不会很高
        for i in range(1, len(s) - 2):
            ip1 = s[: i]
            if not meet(ip1):
                break
            for j in range(i + 1, len(s) - 1):
                ip2 = s[i: j]
                if not meet(ip2):
                    break
                for k in range(j + 1, len(s)):
                    ip3 = s[j: k]
                    if not meet(ip3):
                        break
                    if meet(s[k:]):
                        ip = ip1 + "." + ip2 + "." + ip3 + "." + s[k:]
                        res.append(ip)

        return res

if __name__ == '__main__':
	s = "25525511135"
	res = Solution().restoreIpAddresses(s)
	print(res)