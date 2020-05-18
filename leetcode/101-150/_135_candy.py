class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        import sys
        ratings.append(sys.maxsize)  # 右边界

        start = 0
        end = 1

        candy_num = {-1: 0}  # 方便处理边界问题

        while end < len(ratings):
            if ratings[end] >= ratings[end - 1]:
                length = end - start
                # 确定length子段中左边界的值
                if start != 0 and ratings[start] > ratings[start - 1]:
                    candy_num[start] = max(candy_num[start - 1] + 1, length)
                else:
                    candy_num[start] = length
                # length子段中其余的值
                for i in range(1, length):
                    candy_num[start + i] = length - i
                start = end
            end += 1

        # print(candy_num)
        return sum(candy_num.values())


if __name__ == '__main__':
    ratings = [1, 2, 2]
    res = Solution().candy(ratings)
    print(res)
