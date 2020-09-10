# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(-1)
        res.next = head
        while head:
            if head.next and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return res.next

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l1.next = l2
l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
# l6.next = l7

a = Solution().deleteDuplicates(l1)
while a:
    print(a.val)
    a = a.next