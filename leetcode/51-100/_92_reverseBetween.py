# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dump = ListNode(0)
        dump.next = head


        # 两次循环，先找到起始反转位置
        reverse_l = dump
        reverse_r = head
        i = 1
        while i != m:
            reverse_l = head
            head = head.next
            reverse_r = head
            i += 1

        # 对于进行循环反转
        l = head
        r = head.next
        while i != n and r != None:
            tmp = r.next
            r.next = l
            l = r
            r = tmp
            i += 1

        reverse_l.next = l
        reverse_r.next = r

        return dump.next




if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    head = Solution().reverseBetween(head, 2, 4)

    while head:
        print("{} -> ".format(head.val), end="")
        head = head.next
        if head == None:
            print(head)