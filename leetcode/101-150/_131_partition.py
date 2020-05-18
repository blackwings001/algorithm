class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        def get_partition(cur, tmp):
            if not cur:
                res.append(tmp)

            for i in range(1, len(cur) + 1):
                if cur[:i] == cur[:i][::-1]:
                    get_partition(cur[i:], tmp + [cur[:i]])

        res = []
        get_partition(s, [])
        return res


if __name__ == '__main__':
    s = "abba"
    res = Solution().partition(s)
    print(res)
