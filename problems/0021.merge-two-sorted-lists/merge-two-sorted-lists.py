# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    res = Solution().mergeTwoLists(l1, l2)
    while res:
        print(res.val)
        res = res.next