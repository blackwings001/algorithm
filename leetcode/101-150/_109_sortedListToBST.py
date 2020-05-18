# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 将链表转化为数组，这样就回到了108题
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        if not nums:
            return None

        def sortedArrayToBST(nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            if not nums:
                return None

            mid = len(nums) // 2

            node = TreeNode(nums[mid])
            node.left = sortedArrayToBST(nums[:mid])
            node.right = sortedArrayToBST(nums[mid + 1:])

            return node

        root = sortedArrayToBST(nums)
        return root
