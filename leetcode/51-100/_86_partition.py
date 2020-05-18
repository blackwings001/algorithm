# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None

        # l是最后一个小于x的节点
        dump = ListNode(0)
        dump.next = head
        l = dump

        while head.next != None:
            if head.val < x:
                l = head
                head = head.next
            elif head.next.val >= x:
                    head = head.next
            else: # 出现了逆序，前一个大于等于x，后一个小于x
                tmp = head.next
                head.next = tmp.next
                tmp.next = l.next
                l.next = tmp
                l = l.next

        return dump.next






if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2.5)

    head = Solution().partition(head, 3)

    while head:
        print("{} -> ".format(head.val), end="")
        head = head.next
        if head == None:
            print(head)
