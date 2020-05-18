# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 边界情况
        if head == None or head.next == None or k <= 0:
            return head

        # 计算链表长度
        length = 0
        dump = ListNode(0)
        dump.next = head
        while head:
            length += 1
            head = head.next
        head = dump.next

        # 计算新链表首节点的位置
        new_head_index = length - k % length

        # 边界情况
        if new_head_index == length:
            return head

        # 一般情况
        index = 0
        while head:
            if index + 1 == new_head_index:
                new_head = head.next
                head.next = None

                new_dump = ListNode(0)
                new_dump.next = new_head
                while new_head:
                    if new_head.next == None:
                        new_head.next = dump.next
                        return new_dump.next
                    new_head = new_head.next
            head = head.next
            index += 1








if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    head = Solution().rotateRight(head, 2)

    while head:
        print("{} -> ".format(head.val), end="")
        head = head.next
        if head == None:
            print(head)
