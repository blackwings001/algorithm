class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if candidates == []:
            return result

        candidates = sorted(candidates) # 对数组进行排序
        for i in range(len(candidates)):    # 第一重循环，start从0到len(candidates)-1
            self.get_candidate(candidates, target, start=i, sub=[], result=result)

        return result

    def get_candidate(self, candidates, target, start, sub, result):
        ele = candidates[start] # ele是目前可用的最小的元素
        # 递归基
        if ele > target:
            return
        elif ele == target:
            if sub + [ele] not in result:   # 去重
                result.append(sub + [ele])  # 使用sub + [ele]，不能用sub.append(ele), sub.append(ele)没有返回值
            return
        elif ele < target:
            # 第n重循环，新的start是从start到len(candidates)-1
            for i in range(start, len(candidates)):
                if candidates[i] <= target - ele: # 提前终止无效的迭代
                    self.get_candidate(candidates, target - ele, i, sub + [ele], result)
                else:
                    break


if __name__ == '__main__':
    candidates = [i for i in range(1,31)]
    target = 30
    result = Solution().combinationSum(candidates, target)
    print(result)
    print(len(result))
