# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder and not inorder:
            return None

        node_val = postorder[-1]
        node = TreeNode(node_val)

        node_index = inorder.index(node_val)
        l_inorder = inorder[: node_index]
        l_postorder = postorder[: node_index]
        r_inorder = inorder[1 + node_index:]
        r_postorder = postorder[node_index: -1]

        node.left = self.buildTree(l_inorder, l_postorder)
        node.right = self.buildTree(r_inorder, r_postorder)

        return node


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    root = Solution().buildTree(inorder, postorder)

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

