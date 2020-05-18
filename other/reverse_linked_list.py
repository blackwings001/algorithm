def reverse_linked_list(head):
    if head == None or head.next ==None:
        return head

    before = None   # 对于第一个节点的翻转后next为None
    while head != None:
        #1.记录下head.next, 2.箭头翻转，3.before变为head，4.head变为tmp
        tmp = head.next
        head.next = before
        before = head
        head = tmp

    return before
