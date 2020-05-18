# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None

        dumb = ListNode(0)
        l = dumb
        cur = head
        r = cur.next
        l.next = cur

        while True:
            # 先判断包括cur以及之后的k个节点是否存在, 不存在则返回
            flag_node = cur
            for _ in range(k):
                if flag_node == None:
                    return dumb.next
                flag_node =  flag_node.next

            # 进行k个一组的翻转过程, 一共k-1步
            new_l = cur
            for _ in range(k - 1):
                tmp = r.next
                r.next = cur
                cur = r
                r = tmp

            # 进行连接和指针位置变换
            l.next = cur
            l = new_l
            cur = r
            l.next = cur
            if cur:
                r = cur.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    result = Solution().reverseKGroup(head, 2)

    while result != None:
        print(result.val)
        result = result.next


