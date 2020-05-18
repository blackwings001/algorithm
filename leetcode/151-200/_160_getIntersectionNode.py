# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        # 找到相差步数
        p_a = headA
        p_b = headB
        while True:
            if not p_a.next:
                m = 0
                flag = "headB"
                while p_b.next:
                    p_b = p_b.next
                    m += 1
                break
            if not p_b.next:
                m = 0
                flag = "headA"
                while p_a.next:
                    p_a = p_a.next
                    m += 1
                break
            p_a = p_a.next
            p_b = p_b.next

        if p_a != p_b:
            return None

        if flag == "headB":
            for _ in range(m):
                headB = headB.next
        elif flag == "headA":
            for _ in range(m):
                headA = headA.next

        while True:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next


if __name__ == '__main__':
       head_a = ListNode(2)
       head_b = ListNode(1)
       head_b.next = ListNode(2)
       head_b.next.next = ListNode(3)

       res = Solution().getIntersectionNode(head_a, head_b)
       print(res)