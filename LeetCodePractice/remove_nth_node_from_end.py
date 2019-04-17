class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    c = 0
    p1 = head
    p2 = None
    while p1.next != None:
        c += 1
        if c == 1:
            p1 = head
        else:
            p1 = p1.next
        if c == n + 1:
            p2 = head
        if c > n + 1:
            p2 = p2.next

    if p2 == None:
        head = head.next
        return head

    p2.next = p2.next.next
    return head
