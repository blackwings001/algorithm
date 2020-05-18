# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 使用哑结点，一般还需要一个cur与之配合
        dumb = ListNode(0)
        cur = dumb

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
            return dumb.next
        if l2:
            cur.next = l2
            return dumb.next


if __name__ == '__main__':

    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)

    result = Solution().mergeTwoLists(l1,l2)

    while result != None:
        print(result.val)
        result = result.next


