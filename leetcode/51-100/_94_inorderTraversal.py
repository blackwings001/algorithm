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
        def inorder(node):
            if node == None:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        # inorder(root)


        # 迭代版本，使用栈结构，左孩子依次入栈，出栈时，访问右孩子，然后左孩子依次入栈...，递归版本时间复杂度的常系数较小。
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right

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