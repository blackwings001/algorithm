# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        import sys
        dump = ListNode(-sys.maxsize)
        dump.next = head

        cur = head
        while cur.next:
            p = cur.next
            if p.val < cur.val:
                cur.next = p.next

                first = dump
                while True:
                    if first.next.val > p.val:
                        tmp = first.next
                        first.next = p
                        p.next = tmp
                        break
                    else:
                        first = first.next
            else:
                cur = cur.next

        return dump.next


if __name__ == '__main__':
    head1 = ListNode(5)
    head2 = ListNode(2)
    head3 = ListNode(3)
    head4 = ListNode(1)
    head1.next = head2
    head2.next = head3
    head3.next = head4
    head = Solution().insertionSortList(head1)

    while head:
        print(head.val)
        head = head.next

