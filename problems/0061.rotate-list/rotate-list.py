# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        p = ListNode(-1)
        p.next = head
        length = 0
        while p.next:
            length += 1
            p = p.next
        k = k % length
        if not k:
            return head
        newlast = head
        for i in range(length - 1 - k):
            newlast = newlast.next
        last = newlast
        while last.next:
            last = last.next
        last.next = head
        newhead = newlast.next
        newlast.next = None
        return newhead

head = ListNode(1)
head.next = ListNode(2)
print(Solution().rotateRight(head, 1).val)