# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow = head
        fast = head
        while True:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if not fast:
                return False
            slow = slow.next
            if fast == slow:
                return True
