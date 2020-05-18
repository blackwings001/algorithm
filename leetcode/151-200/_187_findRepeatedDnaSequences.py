class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []

        sub_seq_set = set()
        res = set()

        for i in range(len(s) - 9):
            sub_seq = s[i: i+10]
            if sub_seq in sub_seq_set:
                res.add(sub_seq)
            else:
                sub_seq_set.add(sub_seq)

        return list(res)


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    res = Solution().findRepeatedDnaSequences(s)
    print(res)
