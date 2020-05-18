# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        # 先找到节点的下一层节点中离自己孩子最近的节点, 默认为None
        p = root.next
        x = None
        while p:
            if p.left:
                x = p.left
                break
            elif p.right:
                x = p.right
                break
            else:
                p = p.next

        # 指定该节点的左右孩子的next
        if root.left:
            root.left.next = root.right if root.right else x
        if root.right:
            root.right.next = x

        # 递归节点的右孩子， 左孩子
        root.right = self.connect(root.right)
        root.left = self.connect(root.left)

        return root

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    root = Solution().connect(root)

    def level(node):
        res = []
        stack = []

        stack.append(node)
        while stack:
            ele = stack.pop(0)
            if ele:
                res.append(ele.val)
                res.append(ele.next)
                if ele.left or ele.right:
                    stack.append(ele.left)
                    stack.append(ele.right)
            else:
                res.append("null")

        print(res)

    level(root)
