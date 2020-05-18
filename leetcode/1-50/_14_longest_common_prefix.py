class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_common_prefix = ""
        # 边界条件
        if strs == [] or strs[0] == "":
            return longest_common_prefix

        for index in range(len(strs[0])):
            target = strs[0][index]
            # 扫描strs中的每一个元素
            for string in strs:
                if index >= len(string) or string[index] != target:
                    return longest_common_prefix
            longest_common_prefix += target
        return longest_common_prefix

if __name__ == '__main__':
    strs = ["a"]
    result = Solution().longestCommonPrefix(strs)
    print(result)



