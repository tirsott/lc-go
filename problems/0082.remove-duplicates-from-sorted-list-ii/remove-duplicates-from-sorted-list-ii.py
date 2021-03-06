# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1)
        temp = new_head
        last = -9999
        while head:
            print(head.val, last)
            if head.val == last or (head.next and head.val == head.next.val):
                last = head.val
                head = head.next
            else:
                temp.next = ListNode(head.val)
                last = head.val
                head = head.next
                temp = temp.next
        return new_head.next

l1 = ListNode(1)
l2 = ListNode(2)
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
