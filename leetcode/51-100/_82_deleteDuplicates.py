# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        需要考虑的问题重复元素出现在开头，重复元素出现在末尾，循环终止的条件
        """
        dump = ListNode(0)

        i, j = dump, head
        while j != None:
            if j.next == None or j.next.val != j.val:
                i.next = j
                i = i.next  # 指针i移动
                j = j.next
            else:
                duplicate = j.val
                while True:
                    if j == None or j.val != duplicate:
                        break
                    j = j.next

        # 截取末尾重复的元素
        i.next = None

        return dump.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(5)

    head = Solution().deleteDuplicates(head)

    while head:
        print("{} -> ".format(head.val), end="")
        head = head.next
        if head == None:
            print(head)


