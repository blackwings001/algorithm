class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        if len(t) == 1:
            if t in s:
                return t
            return ""

        start, left, right, min_width = 0, 0, 0, len(s) + 1

        target = {}
        window = {}
        match = 0  # 比较重要，记录匹配的键值对

        for c in t:
            target[c] = target.get(c, 0) + 1
            window[c] = 0

        while right < len(s):
            if s[right] in target:
                window[s[right]] += 1
                if window[s[right]] == target[s[right]]:
                    match += 1
            right += 1

            # 匹配开始循环，循环到不匹配位置
            while match == len(target):
                if right - left < min_width:
                    start = left
                    min_width = right - left
                if s[left] in target:
                    window[s[left]] -= 1
                    if window[s[left]] < target[s[left]]:
                        match -= 1
                left += 1

        if min_width != len(s) + 1:
            return s[start : start + min_width]

        return ""


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABCC"

    res = Solution().minWindow(S, T)
    print(res)