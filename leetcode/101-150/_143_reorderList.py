# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head

        # step1: 找到中间节点
        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        p = head
        for _ in range(length // 2):
            p = p.next
        mid = p

        # step2: 翻转右链表
        p = p.next
        mid.next = None

        post = p.next
        p.next = None
        while post:
            tmp = post.next
            post.next = p
            p = post
            post = tmp

        # step3: 依次连接各个节点
        head1 = head
        head2 = p
        while head2:
            post1 = head1.next
            post2 = head2.next
            head1.next = head2
            head2.next = post1
            head1 = post1
            head2 = post2

        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)

    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5

    res = Solution().reorderList(node1)

    while res:
        print(res.val)
        res = res.next
