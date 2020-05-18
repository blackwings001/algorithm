# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        odd_queue = [root]
        even_queue = []

        while odd_queue or even_queue:
            tmp = []
            while odd_queue:
                ele = odd_queue.pop(0)
                if ele:
                    tmp.append(ele.val)
                    even_queue.append(ele.left)
                    even_queue.append(ele.right)
            if tmp:
                res.append(tmp)

            tmp = []
            while even_queue:
                ele = even_queue.pop(0)
                if ele:
                    tmp.append(ele.val)
                    odd_queue.append(ele.left)
                    odd_queue.append(ele.right)
            if tmp:
                res.append(tmp)

        res = [res[i] for i in range(len(res) - 1, -1, -1)]
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().levelOrderBottom(root)
    print(result)
