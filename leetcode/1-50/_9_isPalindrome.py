class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse_x = 0
        tmp = x

        while tmp != 0:
            reverse_x = reverse_x * 10 + tmp % 10
            tmp = tmp // 10

        return True if reverse_x == x else False

if __name__ == '__main__':
    result = Solution().isPalindrome(1)
    print(result)