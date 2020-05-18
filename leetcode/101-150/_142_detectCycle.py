# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow = head
        fast = head
        while True:
            for _ in range(2):
                fast = fast.next
                if not fast:
                    return None
            slow = slow.next
            if slow == fast:
                new_slow = head
                while True:
                    if new_slow == slow:
                        return slow
                    slow = slow.next
                    new_slow = new_slow.next
