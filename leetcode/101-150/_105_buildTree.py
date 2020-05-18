# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder and not inorder:
            return None

        node_val = preorder[0]
        node = TreeNode(node_val)

        node_index = inorder.index(node_val)
        l_preorder = preorder[1: 1 + node_index]
        l_inorder = inorder[:node_index]
        r_preorder = preorder[1 + node_index:]
        r_inorder = inorder[node_index + 1:]

        node.left = self.buildTree(l_preorder, l_inorder)
        node.right = self.buildTree(r_preorder, r_inorder)

        return node


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    i = inorder.index(3)
    print(i)

    root = Solution().buildTree(preorder, inorder)

    def level(node):
        res = []
        stack = []

        stack.append(node)
        while stack:
            ele = stack.pop(0)
            if ele:
                res.append(ele.val)
                if ele.left or ele.right:
                    stack.append(ele.left)
                    stack.append(ele.right)
            else:
                res.append("null")

        print(res)

    level(root)
