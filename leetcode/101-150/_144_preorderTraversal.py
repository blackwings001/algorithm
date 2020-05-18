# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        traversal = []
        stack = []
        p = root
        while p or stack:
            while p:
                traversal.append(p.val)
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                p = p.right

        return traversal


