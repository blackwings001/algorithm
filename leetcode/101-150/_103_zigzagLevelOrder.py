# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        odd_stack = [root]
        even_stack = []

        while odd_stack or even_stack:
            tmp = []
            while odd_stack:
                ele = odd_stack.pop()
                if ele:
                    tmp.append(ele.val)
                    even_stack.append(ele.left)
                    even_stack.append(ele.right)
            if tmp:
                res.append(tmp)

            tmp = []
            while even_stack:
                ele = even_stack.pop()
                if ele:
                    tmp.append(ele.val)
                    odd_stack.append(ele.right)
                    odd_stack.append(ele.left)
            if tmp:
                res.append(tmp)

        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().zigzagLevelOrder(root)
    print(result)