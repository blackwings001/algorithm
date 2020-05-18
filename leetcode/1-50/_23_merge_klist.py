# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 使用分治法进行k个链表的合并
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.merge_two_lists(lists[0], lists[1])

        mid = len(lists) // 2
        l1 = lists[:mid]
        l2 = lists[mid:]

        return self.merge_two_lists(self.mergeKLists(l1), self.mergeKLists(l2))

    def merge_two_lists(self, l1, l2):
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
        if l2:
            cur.next = l2

        return dumb.next

