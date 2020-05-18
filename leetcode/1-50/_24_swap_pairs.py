# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        dumb = ListNode(0)
        cur = dumb
        # 初始化三个指针
        l = cur
        cur.next = head
        cur = cur.next
        r = cur.next

        while cur != None and cur.next != None :
            # 节点连接改变
            tmp = r.next
            cur.next = tmp
            r.next = cur
            l.next = r

            # 移动三个指针
            l = cur
            cur = cur.next
            if cur != None:
                r = cur.next

        return dumb.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    result = Solution().swapPairs(head)

    while result != None:
        print(result.val)
        result = result.next