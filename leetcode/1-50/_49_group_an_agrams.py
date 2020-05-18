class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == []:
            return [[]]

        d = {}

        for str in strs:
            # 对str进行排序
            ss = "".join(sorted(str))
            d[ss] = d.get(ss, []) + [str]   # 把str放入d[ss]

        return list(d.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)