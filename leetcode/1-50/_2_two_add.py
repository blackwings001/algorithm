# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 使用哑结点，更好处理边界情况
        dummy_node = ListNode(0)
        cur_node = dummy_node
        carry = 0
        # 当l1和l2均为None时,退出循环，l1,l1_value需要根据三元表达式得出
        while l1 != None or l2 != None:
            l1_value = 0 if l1 == None else l1.val
            l2_value = 0 if l2 == None else l2.val
            cur_value = l1_value + l2_value + carry
            carry = cur_value // 10         # 进位值
            cur_value = cur_value % 10      # 当前值

            cur_node.next = ListNode(cur_value)
            cur_node = cur_node.next

            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next

        # 最后判断carry是否为1
        if carry == 1:
            cur_node.next = ListNode(1)

        return dummy_node.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(8)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
