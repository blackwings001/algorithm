class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next =  next

def k_reverse(head, k):
    prev = head
    check = head
    cur = head.next

    # 检测包括head在内的接下来k个节点是否均存在
    check_value = 0
    while check != None and check_value < k:
        check_value += 1
        check = check.next

    if check_value < k:
        return head

    else:
        for _ in range(k-1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        if cur:
            head.next = k_reverse(cur, k)
        else:
            head.next = None

        return prev




if __name__ == '__main__':


    for k in range(1,9):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8,
                                                                                                            ListNode(9,
                                                                                                                     ListNode(
                                                                                                                         10, ))))))))))

        print(k)
        new_head = k_reverse(head, k)
        while new_head != None:
            print(new_head.val, end=" ")
            new_head = new_head.next
        print("\n")
