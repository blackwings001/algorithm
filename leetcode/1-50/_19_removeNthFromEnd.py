# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dumb = ListNode(0)
        dumb.next = head

        l_node = dumb   # 为了应对倒数的n的节点是首节点，让l_node为哑结点
        r_node = head

        for _ in range(n-1):  # r_node先走n-1步，此时l_node和r_node的距离为n
            r_node = r_node.next
            if r_node == None:
                return dumb.next

        while True:
            if r_node.next == None:
                l_node.next = l_node.next.next
                return dumb.next
            r_node = r_node.next
            l_node = l_node.next
