# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        res = None
        while dummy and dummy.next:
            if dummy.next.val != val and not res:
                res = dummy.next
            if dummy.next.val == val:
                dummy.next = dummy.next.next
                continue
            dummy = dummy.next
        return res

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
l = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5,
                                                                         ListNode(6)))))))
l1 = Solution().removeElements(l, 6)
while l1:
    print(l1.val)
    l1 = l1.next
