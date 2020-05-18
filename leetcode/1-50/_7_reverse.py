class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_x = self.reverse_positive(x) if x >= 0 else - self.reverse_positive(x)
        return reverse_x

    def reverse_positive(self, x):

        positive = 1 if x >= 0 else 0
        x = x if x >= 0 else - x
        reverse_x = 0

        while x != 0:
            reverse_x = 10 * reverse_x + x % 10
            x = x // 10
            # 判断是否越界
            if (positive == 0 and -reverse_x <= - 2 ** 31) or  (positive == 1 and reverse_x >= 2 ** 31 - 1):
                return 0

        return reverse_x


if __name__ == '__main__':
    num = -123
    reverse_num = Solution().reverse(num)
    print(reverse_num)