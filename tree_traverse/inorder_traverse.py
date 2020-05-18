# coding:utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res

        # 递归版本
        def inorderRecursion(node):
            if node == None:
                return

            inorderRecursion(node.left)
            res.append(node.val)
            inorderRecursion(node.right)

        # 迭代版本，使用栈结构，出栈时访问节点值
        def inorderIteration(root):
            stack = []
            p = root
            while stack or p:
                while p:
                    stack.append(p)
                    p = p.left
                if stack:
                    p = stack.pop()  # p的左子树已经遍历完毕
                    res.append(p.val)  # 保存p的值
                    p = p.right  # 开始遍历p的右子树


        # 迭代版本，使用莫里斯遍历，需要的辅助空间为O(1)
        def morrisInorderIteration(root):
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
                        p = p.left
                    elif precursor.right == p:
                        precursor.right = None
                        res.append(p.val)
                        p = p.right
                else:
                    res.append(p.val)
                    p = p.right


        # inorderRecursion(root)
        # inorderIteration(root)
        morrisInorderIteration(root)
        return res






if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    res = Solution().inorderTraversal(root)
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