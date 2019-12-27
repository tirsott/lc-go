# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        res = dummy
        while 1:
            self.reverse_k_nodes(dummy, k)
            for i in range(k):
                if not dummy.next:
                    return res.next
                else:
                    dummy = dummy.next

    def reverse_k_nodes(self, head, k):
        temp = head
        for i in range(k):
            if not temp.next:
                return
            temp = temp.next
        next_node = temp.next
        next = head.next
        for i in range(k):
            p = next
            next = next.next
            p.next = next_node
            next_node = p
            head.next = p
        return
