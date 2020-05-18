# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node


if __name__ == '__main__':
    nums = [-20, -10, -3, 0, 5, 9, 10]
    root = Solution().sortedArrayToBST(nums)

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