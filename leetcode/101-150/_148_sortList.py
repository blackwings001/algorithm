# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 找到中间点
        length = 0
        p = head
        while p:
            p = p.next
            length += 1

        mid = head
        length = length // 2 - 1
        while length > 0:
            mid = mid.next
            length -= 1
        tmp = mid
        mid = mid.next
        tmp.next = None

        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1

        dump = ListNode(0)
        p = dump
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next

        if head1:
            p.next = head1
        elif head2:
            p.next = head2

        return dump.next


if __name__ == '__main__':
    head1 = ListNode(5)
    head2 = ListNode(3)
    head3 = ListNode(1)
    head4 = ListNode(2)
    head5 = ListNode(4)

    head1.next = head2
    head2.next = head3
    head3.next = head4
    head4.next = head5

    head = Solution().sortList(head1)
    while head:
        print(head.val)
        head = head.next