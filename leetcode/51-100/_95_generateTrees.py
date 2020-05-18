# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n == 0:
            return res

        def tree(nodes):
            if not nodes:
                return [None]
            elif len(nodes) == 1:
                return nodes

            tmp = []
            for i in range(len(nodes)):
                left = tree(nodes[:i])
                right = tree(nodes[i+1:])
                for l in left:
                    for r in right:
                        root = TreeNode(nodes[i].val)  # 每次使用一个新的节点，不要使用nodes中的节点，nodes中节点会改变
                        root.left = l
                        root.right = r
                        tmp.append(root)

            return tmp

        nodes = [TreeNode(i + 1) for i in range(n)]
        res = tree(nodes)

        return res


if __name__ == '__main__':
    n = 4
    res = Solution().generateTrees(n)
    print(res)

    def level(root):
        res = []
        stack = []

        stack.append(root)
        while stack:
            ele = stack.pop(0)
            if ele:
                res.append(ele.val)
                if ele.left or ele.right:
                    stack.append(ele.left)
                    stack.append(ele.right)
            else:
                res.append("null")

        print(res)

    for root in res:
        level(root)
