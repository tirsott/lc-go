# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode(-1)
        new_head_end = new_head
        big_head = ListNode(-1)
        big_head_end = big_head
        while head:
            if not new_head.next and head.val < x:
                new_head.next = head
                new_head_end = head
                head = head.next
                continue
            if not big_head.next and head.val >= x:
                big_head.next = head
                big_head_end = head
                head = head.next
                continue
            if head.val < x:
                new_head_end.next = head
                new_head_end = head
                head = head.next
                continue
            if head.val >= x:
                big_head_end.next = head
                big_head_end = head
                head = head.next
                continue
        new_head_end.next = big_head.next
        big_head_end.next = None
        return new_head.next



l1 =ListNode(2)
l2 =ListNode(4)
l3 =ListNode(3)
l4 =ListNode(2)
l5 =ListNode(5)
l6 =ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
ll = Solution().partition(l1, 3)
while ll:
    print(ll.val)
    ll = ll.next
# 2->4->3->2->5->2