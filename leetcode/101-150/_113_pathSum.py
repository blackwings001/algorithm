# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        cur = []

        def paths(node, sum_, cur_, res_):
            if not node.left and not node.right:
                if sum_ - node.val == 0:
                    res_.append(cur_ + [node.val])
                return

            if node.left:
                paths(node.left, sum_ - node.val, cur_ + [node.val], res_)
            if node.right:
                paths(node.right, sum_ - node.val, cur_ + [node.val], res_)

        paths(root, sum, cur, res)

        return res


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    root.right.right.left = TreeNode(5)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    result = Solution().pathSum(root, 22)
    print(result)
