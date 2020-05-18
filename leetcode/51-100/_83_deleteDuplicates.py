# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dump = ListNode(0)
        dump.next = head

        j = head
        while j != None:
            if j.next == None or j.next.val != j.val:
                j = j.next
            else: # 实际为j.next != None and j.next.val == j.val
                j.next = j.next.next

        return dump.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(5)

    head = Solution().deleteDuplicates(head)

    while head:
        print("{} -> ".format(head.val), end="")
        head = head.next
        if head == None:
            print(head)