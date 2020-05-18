class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = []
        if n <= 0:
            return None

        # 构建长度为n的nums，最后的输出结果为nums[-1]
        nums.append("1")
        for i in range(n-1):
            nums.append(self.say(nums[-1]))

        return nums[-1]

    def say(self, num):
        say_num = ""

        # 读num, 一次读取连续相同的数字字符
        pre_char = ""
        count = 0
        for char in num:
            if pre_char == "" or char == pre_char:
                count += 1
            else:
                say_num += str(count) + pre_char
                count = 1
            pre_char = char

        say_num += str(count) + pre_char  # 写入最后一串相同数字
        return say_num

if __name__ == '__main__':
    # for n in range(1, 100):
    result = Solution().countAndSay(50)
    print(len(result))

