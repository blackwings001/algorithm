class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 or not version2:
            return 0

        version1 = version1.split(".")
        version2 = version2.split(".")

        for i in range(max(len(version1), len(version2))):
            val1 = 0 if i >= len(version1) else int(version1[i])
            val2 = 0 if i >= len(version2) else int(version2[i])

            if val1 > val2:
                return 1
            if val1 < val2:
                return -1
        return 0


if __name__ == '__main__':
    version1 = "1.001"
    version2 = "1.1"
    print(1)
    print(2)
    res = Solution().compareVersion(version1, version2)
    print(res)
