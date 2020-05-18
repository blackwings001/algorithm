# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        traversal = []
        stack = []
        p = root
        last_node = p

        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                ele = stack[-1]
                if not ele.right or ele.right == last_node:
                    ele = stack.pop()
                    traversal.append(ele.val)
                    last_node = ele
                else:
                    p = ele.right

        return traversal


