def remove_target_node(head, target):
    # 找到第一个value不是target的节点，循环的条件是head不为None且head.value==target注意顺序不能乱
    while head != None and head.value == target:
        head = head.next
    # 跳出循环有两种情况，1是head==None, 返回None; 2是head.value不是target，此时进入循环
    if head == None:
        return None
    else:
        first_head = head
        while head.next != None:
            if head.next.value == target:
                head.next = head.next.next
            else:
                head = head.next
        return first_head

