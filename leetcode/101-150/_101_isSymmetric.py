# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def recursion(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and (node1.val == node2.val):
                return recursion(node1.left, node2.right) and recursion(node1.right, node2.left)
            else:
                return False

        def iteration(node):

            def level_traverse(sub_node, diction):
                traverse = []
                queue = [sub_node]

                while queue:
                    ele = queue.pop(0)
                    if ele:
                        traverse.append(ele.val)
                        if diction == "left":
                            queue.append(ele.left)
                            queue.append(ele.right)
                        else:
                            queue.append(ele.right)
                            queue.append(ele.left)
                    else:
                        traverse.append(None)

                return traverse

            left_level_traverse = level_traverse(node.left, "left")
            right_level_traverse = level_traverse(node.right, "right")

            if left_level_traverse == right_level_traverse:
                return True
            return False

        result = recursion(root.left, root.right)
        result = iteration(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    res = Solution().isSymmetric(root)
    print(res)