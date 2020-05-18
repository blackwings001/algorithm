# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res

        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res = Solution().levelTraversal(root)
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