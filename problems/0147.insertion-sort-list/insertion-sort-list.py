from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        while p.next:
            if p.next.val >= p.val:
                p = p.next
                continue
            temp = p.next
            if temp.val < head.val:
                p.next = temp.next
                temp.next = head
                head = temp
            else:
                pos = head
                while pos.val < temp.val and pos.next.val < temp.val:
                    pos = pos.next
                p.next = temp.next
                temp.next = pos.next
                pos.next = temp
        return head

l = ListNode(1, ListNode(2, ListNode(1)))
l = Solution().insertionSortList(l)
while l:
    print(l.val)
    l = l.next

# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5