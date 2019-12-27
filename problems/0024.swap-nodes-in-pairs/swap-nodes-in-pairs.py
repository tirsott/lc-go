# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        res = dummy
        while dummy.next and dummy.next.next:
            p = dummy.next
            q = dummy.next.next
            p.next = q.next
            dummy.next = q
            q.next = p
            dummy = dummy.next.next
        return res.next
