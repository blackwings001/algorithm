# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_path(node):
            if not node:
                return 0

            # 取当节点的子路径最大值是负数时，可以不取
            left_max = max(max_path(node.left), 0)
            right_max = max(max_path(node.right), 0)

            cur = node.val + left_max + right_max
            nonlocal max_sum
            if cur > max_sum:
                max_sum = cur

            # 返回以该节点为子节点的路径最大值
            return max(left_max + node.val, right_max + node.val)

        import sys
        max_sum = -sys.maxsize
        max_path(root)

        return max_sum


if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    res = Solution().maxPathSum(root)
    print(res)