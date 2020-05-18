class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 一行解法
        # return int(bin(n)[2:].zfill(32)[::-1], 2)

        res = 0
        for _ in range(32):
            res <<= 1
            res += n & 1    # 检测最后一位是1还是0
            n >>= 1
        return res


if __name__ == '__main__':
    n = 43261596
    res = Solution().reverseBits(n)
    print(res)
