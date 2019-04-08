# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Input: 1->2->3->4->5->NULL
#        o  e  o  e  o  e

# 1->2->3->4->NULL
# o  e  o  e  o
# Output: 1->3->5->2->4->NULL

def oddEvenList(head):
    if head == None or head.next == None:
        return head
    odd_head = head
    odd = odd_head
    even_head = head.next
    even = even_head

    while True:
        if even == None or odd == None:
            odd.next = even_head
            return odd_head
        if even.next != None:
            odd.next = even.next
            odd = odd.next
        else:
            odd.next = even_head
            return odd_head
        if odd != None:
            even.next = odd.next
            even = even.next
