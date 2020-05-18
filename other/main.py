from remove_target_node import remove_target_node
from reverse_linked_list import reverse_linked_list


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    if head == None:
        print(head)
    else:
        print(head.value, end="")
        while head.next != None:
            head = head.next
            print("-->" + str(head.value), end="")
        print("")

def get_head():
    head1 = Node(0)
    head2 = Node(1, Node(2, Node(2, Node(3, Node(4, Node(5))))))
    return head1, head2


if __name__ == '__main__':
    # 移除指定值得节点, 考虑几种情况，1.只有一个节点的链表，2.初始节点的值为target，3.最后节点的值为target
    head1, _ = get_head()
    print_linked_list(remove_target_node(head1, 0))
    head1, _ = get_head()
    print_linked_list(remove_target_node(head1, 1))
    _, head2 = get_head()
    print_linked_list(remove_target_node(head2, 1))
    _, head2 = get_head()
    print_linked_list(remove_target_node(head2, 2))
    _, head2 = get_head()
    print_linked_list(remove_target_node(head2, 5))

    # 翻转链表
    head1, head2 = get_head()
    print_linked_list(reverse_linked_list(head1))
    print_linked_list(reverse_linked_list(head2))





