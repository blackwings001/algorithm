# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        p = root
        while p:
            # p的左孩子为空，没有前驱结点，那么访问p的右孩子
            if not p.left:
                p = p.right
            # p的左孩子不为空，找到p的前驱节点，然后将p的右孩子变为前驱结点的右孩子，p的右孩子变为空
            else:
                pre = p.left
                while pre.right:
                    pre = pre.right

                pre.right = p.right
                p.right = None
                p = p.left

        # 下面将树变为右侧树
        p = root
        while p:
            if p.left:
                p.right = p.left
                p.left = None
            p = p.right


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    Solution().flatten(root)

    def level(node):
        res = []
        stack = []

        stack.append(node)
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

    level(root)
