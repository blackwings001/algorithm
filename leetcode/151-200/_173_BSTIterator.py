# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.p = root
        self.stack = []

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.p:
            self.stack.append(self.p)
            self.p = self.p.left

        min_p = self.stack.pop()
        self.p = min_p.right
        return min_p.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.p or len(self.stack) > 0:
            return True
        return False


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node3.left = node1
    node3.right = node4
    node1.right = node2

    obj = BSTIterator(node3)
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())

