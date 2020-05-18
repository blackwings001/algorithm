# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        def is_balance(node):
            """
            :param node: node平衡时，返回节点的树深，不平衡时，返回-1
            """
            if not node:
                return 0

            node_l = is_balance(node.left)
            node_r = is_balance(node.right)

            if node_l != -1 and node_r != -1 and -1 <= node_l - node_r <= 1:
                # 只有上面一种不返回-1的情况
                return max(node_l, node_r) + 1

            return -1

        result = is_balance(root)
        return False if result == -1 else True

    # def isBalanced(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return False
    #
    #     def is_balance(node):
    #         """
    #         :param node: node平衡时，node.val记录的是节点的树深，不平衡时，node.val为-1
    #         """
    #         if not node.left and not node.right:
    #             node.val = 1
    #         elif not node.left:
    #             is_balance(node.right)
    #             node.val = 2 if node.right.val == 1 else -1
    #         elif not node.right:
    #             is_balance(node.left)
    #             node.val = 2 if node.left.val == 1 else -1
    #         else:
    #             is_balance(node.right)
    #             is_balance(node.left)
    #             if node.left.val == -1 or node.right.val == -1:
    #                 node.val = -1
    #             elif -1 <= node.left.val - node.right.val <= 1:
    #                 node.val = max(node.left.val, node.right.val) + 1
    #             else:
    #                 node.val = -1
    #
    #     is_balance(root)
    #     return False if root.val == -1 else True


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    res = Solution().isBalanced(root)
    print(res)
