# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res

        # 递归版本
        def postorderRecursion(node):
            if node == None:
                return

            postorderRecursion(node.left)
            postorderRecursion(node.right)
            res.append(node.val)

        # 迭代版本, 左右根，读取根节点值时，必须保证左右子树都访问完毕
        def postorderIteration(root):
            stack = []
            p = root
            lastvisit = root
            while stack or p:
                while p:
                    stack.append(p)
                    p = p.left
                if stack:
                    p = stack[-1]  # 查看栈顶元素，并不取出
                    if not p.right or lastvisit == p.right:
                        # node的右子树遍历完毕后，存储p的值
                        p = stack.pop()
                        res.append(p.val)
                        lastvisit = p
                        p = None    # 继续访问栈中元素
                    else:
                        # 遍历node的右子树
                        p = p.right

        # 迭代版本，使用莫里斯遍历，需要的辅助空间为O(1)
        def morrisPostorderIteration(root):
            dump = TreeNode(0)
            dump.left = root
            p = dump
            res = []
            while p:
                if p.left:
                    # 找到前驱节点
                    tmp = []
                    precursor = p.left
                    # 找到前驱节点，同时倒序储存节点值
                    tmp.insert(0, precursor.val)
                    while precursor.right and precursor.right != p:
                        precursor = precursor.right
                        tmp.insert(0, precursor.val)
                    # 根据前驱节点的右孩子，选择不同的操作
                    if precursor.right == None:
                        precursor.right = p
                        p = p.left
                    elif precursor.right == p:
                        precursor.right = None
                        res += tmp
                        p = p.right
                else:
                    p = p.right
            return res

        # postorderRecursion(root)
        # postorderIteration(root)
        res = morrisPostorderIteration(root)
        return res






if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    res = Solution().postorderTraversal(root)
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