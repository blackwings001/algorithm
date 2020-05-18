# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = 0
        if n == 0:
            return res

        def tree(nodes):
            if not nodes or len(nodes) == 1:
                return 1

            tmp = 0
            for i in range(len(nodes)):
                left = tree(nodes[:i])
                right = tree(nodes[i+1:])
                tmp += left * right

            return tmp

        nodes = [TreeNode(i + 1) for i in range(n)]
        res = tree(nodes)

        return res


if __name__ == '__main__':
    n = 19
    res = Solution().numTrees(n)
    print(res)

    # def level(root):
    #     res = []
    #     stack = []
	#
    #     stack.append(root)
    #     while stack:
    #         ele = stack.pop(0)
    #         if ele:
    #             res.append(ele.val)
    #             if ele.left or ele.right:
    #                 stack.append(ele.left)
    #                 stack.append(ele.right)
    #         else:
    #             res.append("null")
	#
    #     print(res)
	#
    # for root in res:
    #     level(root)
