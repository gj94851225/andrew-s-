"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_lst = []
    change_to_lst(l1, l1_lst)
    l2_lst = []
    change_to_lst(l2, l2_lst)
    new_lst = []
    if len(l1_lst) > len(l2_lst):
        while len(l1_lst) != len(l2_lst):
            l2_lst.append(0)
    elif len(l1_lst) < len(l2_lst):
        while len(l1_lst) != len(l2_lst):
            l1_lst.append(0)
    else:
        for i in range(len(l1_lst)):
            new_lst.append(l1_lst[i] + l2_lst[i])
    new_lst2 = []
    control = 0
    for i in range(len(new_lst)):
        if control == 0:
            if new_lst[i] >= 10:
                new_lst2.append(new_lst[i] - 10)
                control = 1
            else:
                new_lst2.append(new_lst[i])
        else:
            if new_lst[i] >= 10:
                new_lst2.append(new_lst[i] - 9)
                control = 1
            else:
                new_lst2.append(new_lst[i] + 1)
                control = 0

    ans_node = ListNode(new_lst2[0], None)
    if len(new_lst2) > 1:
        cur = ans_node
        for i in range(len(new_lst2)-1):
            new_node = ListNode(new_lst2[i + 1], None)
            cur.next = new_node
            cur = cur.next
    return ans_node


def change_to_lst(l, l_lst):
    cur = l
    while cur is not None:
        l_lst.append(cur.val)
        cur = cur.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
