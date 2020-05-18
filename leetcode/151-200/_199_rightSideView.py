# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 思路是：右视图为层次遍历中每层的最后一个元素组成的列表
        if not root:
            return []

        res = []
        queue1 = [root]
        queue2 = []

        while queue1 or queue2:
            if queue1:
                res.append(queue1[-1].val)
            while queue1:
                p = queue1.pop(0)
                if p.left:
                    queue2.append(p.left)
                if p.right:
                    queue2.append(p.right)

            if queue2:
                res.append(queue2[-1].val)
            while queue2:
                p = queue2.pop(0)
                if p.left:
                    queue1.append(p.left)
                if p.right:
                    queue1.append(p.right)

        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node2.right = node4
    node1.right = node3
    node3.right = node5
    node4.right = TreeNode(7)

    res = Solution().rightSideView(node1)
    print(res)
