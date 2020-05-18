# coding:utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraverse(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res

        # 递归版本, 根左右
        def preorderRecursion(node):
            if node == None:
                return

            res.append(node.val)
            preorderRecursion(node.left)
            preorderRecursion(node.right)

        # 迭代版本，可以只有右孩子入栈，也可以都入栈
        def preorderIteration(root):
            stack = []
            p = root
            # p是访问节点，循环条件时访问节点和栈都空
            while stack or p:
                while p:
                    res.append(p.val)  # 先访问节点值
                    stack.append(p)
                    p = p.left
                if stack:
                    p = stack.pop()
                    p = p.right  # p节点的左子树都访问过，开始访问右子树

        # 迭代版本，使用莫里斯遍历，需要的辅助空间为O(1)
        def morrisPreorderIteration(root):
            p = root
            while p:
                if p.left:
                    # 找到前驱节点
                    precursor = p.left
                    while precursor.right and precursor.right != p:
                        precursor = precursor.right
                    # 根据前驱节点的右孩子，选择不同的操作
                    if precursor.right == None:
                        precursor.right = p
                        res.append(p.val)
                        p = p.left
                    elif precursor.right == p:
                        precursor.right = None
                        p = p.right
                else:
                    res.append(p.val)
                    p = p.right

        # preorderRecursion(root)
        # preorderIteration(root)
        morrisPreorderIteration(root)
        return res






if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res = Solution().preorderTraverse(root)
    print(res)


    def level(root):
        res = []
        stack = []

        stack.append(root)
        while stack:
            ele = stack.pop(0)
            if ele:
                res.append(ele.val)
                stack.append(ele.left)
                stack.append(ele.right)

        print(res)

    level(root)